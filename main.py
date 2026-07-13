#!/usr/bin/env python3
"""Fetch docs as Markdown via pluggable fetchers (jina / tavily)."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from threading import Lock

from tqdm import tqdm

from fetchers import Fetcher, create_fetcher


def load_dotenv(path: Path) -> None:
    """Load KEY=VALUE pairs from a .env file into os.environ (no overwrite)."""
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def title_to_path(title: str, output_dir: Path) -> Path:
    """
    Convert a title key to a markdown file path.

    Examples:
        产品动态 -> output_dir/产品动态.md
        产品简介>Agent Runtime 概述 -> output_dir/产品简介/Agent Runtime 概述.md
    """
    parts = [p.strip() for p in title.split(">") if p.strip()]
    if not parts:
        raise ValueError(f"Empty title: {title!r}")
    *dirs, filename = parts
    return output_dir.joinpath(*dirs, f"{filename}.md")


@dataclass(frozen=True)
class Job:
    title: str
    url: str
    out_path: Path
    rel: str


@dataclass
class JobResult:
    rel: str
    ok: bool
    message: str


def _fetch_one(
    fetcher: Fetcher,
    job: Job,
    *,
    delay: float,
    write_lock: Lock,
) -> JobResult:
    try:
        content = fetcher.fetch(job.url)
        header = (
            f"<!-- source: {job.url} -->\n"
            f"<!-- fetcher: {fetcher.name} -->\n\n"
        )
        with write_lock:
            job.out_path.parent.mkdir(parents=True, exist_ok=True)
            job.out_path.write_text(header + content, encoding="utf-8")
        if delay > 0:
            time.sleep(delay)
        return JobResult(job.rel, True, f"{len(content)} chars")
    except Exception as e:
        if delay > 0:
            time.sleep(delay)
        return JobResult(job.rel, False, str(e))


def fetch_all(
    urls_path: Path,
    *,
    backend: str = "jina",
    delay: float = 0.0,
    concurrency: int = 4,
    skip_existing: bool = False,
    tavily_depth: str = "advanced",
) -> None:
    if not urls_path.is_file():
        print(f"Error: file not found: {urls_path}", file=sys.stderr)
        sys.exit(1)

    if concurrency < 1:
        print("Error: --concurrency must be >= 1", file=sys.stderr)
        sys.exit(1)

    output_dir = urls_path.parent
    with urls_path.open(encoding="utf-8") as f:
        mapping: dict[str, str] = json.load(f)

    if not isinstance(mapping, dict):
        print("Error: urls.json must be an object of {title: url}", file=sys.stderr)
        sys.exit(1)

    jobs: list[Job] = []
    skipped = 0
    for title, url in mapping.items():
        out_path = title_to_path(title, output_dir)
        rel = str(out_path.relative_to(output_dir))
        if skip_existing and out_path.is_file() and out_path.stat().st_size > 0:
            skipped += 1
            continue
        jobs.append(Job(title=title, url=url, out_path=out_path, rel=rel))

    total = len(mapping)
    print(f"Output directory: {output_dir}")
    print(f"Total: {total}  to_fetch: {len(jobs)}  skipped: {skipped}")
    print(
        f"Backend: {backend}  concurrency: {concurrency}  "
        f"delay: {delay}s  tavily_depth: {tavily_depth}\n"
    )

    if not jobs:
        print("Nothing to fetch.")
        return

    write_lock = Lock()
    ok, failed = 0, 0
    failures: list[JobResult] = []
    workers = min(concurrency, len(jobs))

    with create_fetcher(
        backend,
        concurrency=concurrency,
        tavily_depth=tavily_depth,
    ) as fetcher:
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {
                executor.submit(
                    _fetch_one,
                    fetcher,
                    job,
                    delay=delay,
                    write_lock=write_lock,
                ): job
                for job in jobs
            }
            with tqdm(
                total=len(jobs),
                desc=f"Fetching[{fetcher.name}]",
                unit="doc",
                dynamic_ncols=True,
            ) as pbar:
                for future in as_completed(futures):
                    result = future.result()
                    if result.ok:
                        ok += 1
                        pbar.set_postfix_str(f"ok {result.rel}", refresh=False)
                    else:
                        failed += 1
                        failures.append(result)
                        pbar.set_postfix_str(f"fail {result.rel}", refresh=False)
                    pbar.update(1)

    print(f"\nDone. ok={ok} skipped={skipped} failed={failed} total={total}")
    if failures:
        print("\nFailed:", file=sys.stderr)
        for item in failures:
            print(f"  - {item.rel}: {item.message}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    load_dotenv(Path(__file__).resolve().parent / ".env")

    parser = argparse.ArgumentParser(
        description="Fetch docs from urls.json and save as Markdown (jina / tavily).",
    )
    parser.add_argument(
        "urls_json",
        type=Path,
        help="Path to urls.json (Markdown is written next to this file)",
    )
    parser.add_argument(
        "-b",
        "--backend",
        choices=("jina", "tavily"),
        default="jina",
        help="Fetch backend (default: jina)",
    )
    parser.add_argument(
        "-c",
        "--concurrency",
        type=int,
        default=4,
        metavar="N",
        help="Number of concurrent requests (default: 4)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Seconds to sleep after each request (per worker, default: 0)",
    )
    parser.add_argument(
        "--depth",
        choices=("basic", "advanced"),
        default="advanced",
        help="Tavily extract_depth only (default: advanced)",
    )
    parser.add_argument(
        "--skip-existing",
        action="store_true",
        help="Skip titles whose .md file already exists and is non-empty",
    )
    args = parser.parse_args()
    fetch_all(
        args.urls_json.resolve(),
        backend=args.backend,
        delay=args.delay,
        concurrency=args.concurrency,
        skip_existing=args.skip_existing,
        tavily_depth=args.depth,
    )


if __name__ == "__main__":
    main()
