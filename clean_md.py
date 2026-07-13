#!/usr/bin/env python3
"""Strip Tencent Cloud site chrome from Jina-extracted Markdown files.

Typical noise removed:
  - top global nav / 近期搜索热词 / product mega-menu
  - left product TOC (#### 产品动态 / 产品简介 / ...)
  - share widgets, empty image links
  - ## 本页目录
  - footer: 上一篇/下一篇, 相关文档, copyright, AI 助手 chrome
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# Keep leading HTML comments we inject at fetch time.
COMMENT_RE = re.compile(r"^<!--.*?-->\s*$")

# Real document H1 (Jina emits: "# 快速入门")
H1_RE = re.compile(r"^#\s+\S")

# Update timestamp line right under title.
UPDATED_RE = re.compile(r"^最近更新时间[：:]")

# Page TOC block.
TOC_HEADING_RE = re.compile(r"^##\s*本页目录\s*[:：]?\s*$")

# Content ends when footer chrome starts.
FOOTER_START_RE = re.compile(
    r"("
    r"上一篇\s*:"
    r"|下一篇\s*:"
    r"|###\s*.*相关文档\s*$"
    r"|Copyright\s*©"
    r"|All Rights Reserved"
    r"|^搜索结果\s*$"
    r"|^问 AI 助手\s*$"
    r"|^正在为您收集信息\s*$"
    r"|文档反馈官"
    r")"
)

# Lines that are pure chrome even inside the body window.
DROP_LINE_RE = re.compile(
    r"("
    r"^关闭搜索\s*$"
    r"|^###\s*近期搜索热词\s*$"
    r"|^###\s*热门搜索\s*$"
    r"|javascript:void\s*0"
    r"|^链接复制成功\s*$"
    r"|^复制成功\s*$"
    r"|^复制\s*$"
    r"|微信扫一扫"
    r"|新浪微博"
    r"|_我的收藏_"
    r"|^\[\]\([^)]*\)\s*$"  # empty-image / empty-link lines
    r"|^\[\]\([^)]*\)(\[\]\([^)]*\))+\s*$"  # consecutive empty links
    r"|blob:http://localhost/"
    r")"
)

# Normalize "### [](javascript:;)标题" -> "### 标题"
EMPTY_ANCHOR_HEADING_RE = re.compile(
    r"^(#{1,6})\s*\[\]\(javascript:[^)]*\)\s*"
)

# Share / social lines like "*   [QQ](...)" right under title.
SHARE_BULLET_RE = re.compile(
    r"^\*\s+\[(QQ|新浪微博|复制链接|微信)\]",
)

# Breadcrumb chrome
BREADCRUMB_RE = re.compile(r"文档中心.*>_.*")


def extract_header_comments(lines: list[str]) -> tuple[list[str], int]:
    """Return (comment_lines, index_after_comments)."""
    comments: list[str] = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if not s:
            i += 1
            continue
        if COMMENT_RE.match(s):
            comments.append(s)
            i += 1
            continue
        break
    return comments, i


def find_content_start(lines: list[str], begin: int) -> int | None:
    """Index of real H1 title, or None."""
    # Prefer the last H1-looking line before "最近更新时间" or "本页目录",
    # because site chrome rarely has a bare "# title" before the article.
    candidates: list[int] = []
    for i in range(begin, len(lines)):
        if H1_RE.match(lines[i]):
            candidates.append(i)
        # Once we passed a solid content marker, stop collecting later H1s from footers.
        if i > begin and UPDATED_RE.match(lines[i].strip()):
            break
        if TOC_HEADING_RE.match(lines[i].strip()):
            break
        if FOOTER_START_RE.search(lines[i]):
            break

    if not candidates:
        # Fallback: first H1 anywhere
        for i in range(begin, len(lines)):
            if H1_RE.match(lines[i]):
                return i
        return None

    # Use the last candidate before content markers — usually the article title.
    return candidates[-1]


def find_content_end(lines: list[str], start: int) -> int:
    """Exclusive end index of real content."""
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if FOOTER_START_RE.search(line):
            return i
        # Product-doc sidebar heading pattern near end is rare; also stop at
        # duplicated site footer product mega-lists that start with known chrome.
        if line.strip() == "搜索结果":
            return i
    return len(lines)


def drop_toc_block(lines: list[str]) -> list[str]:
    """Remove '## 本页目录' section until next real heading at same/higher level."""
    out: list[str] = []
    i = 0
    while i < len(lines):
        if TOC_HEADING_RE.match(lines[i].strip()):
            i += 1
            while i < len(lines):
                s = lines[i].strip()
                # TOC is only list items / blanks until next ## heading (not 本页目录).
                if s.startswith("## ") and not TOC_HEADING_RE.match(s):
                    break
                if s.startswith("# ") and not s.startswith("##"):
                    break
                i += 1
            continue
        out.append(lines[i])
        i += 1
    return out


def drop_noise_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    for line in lines:
        s = line.strip()
        if not s:
            out.append("")
            continue
        # ### [](javascript:;)标题  ->  ### 标题
        line = EMPTY_ANCHOR_HEADING_RE.sub(r"\1 ", line)
        s = line.strip()
        if DROP_LINE_RE.search(line):
            continue
        if SHARE_BULLET_RE.match(s):
            continue
        if BREADCRUMB_RE.search(s):
            continue
        # Lone social QQ line without bullet
        if re.fullmatch(r"\[QQ\]\([^)]+\)", s):
            continue
        if re.fullmatch(r"\[复制链接\]\([^)]+\).*", s):
            continue
        out.append(line)
    return out


def collapse_blank_lines(lines: list[str], max_blank: int = 2) -> list[str]:
    out: list[str] = []
    blanks = 0
    for line in lines:
        if line.strip() == "":
            blanks += 1
            if blanks <= max_blank:
                out.append("")
        else:
            blanks = 0
            out.append(line.rstrip())
    # Trim leading/trailing blanks
    while out and out[0] == "":
        out.pop(0)
    while out and out[-1] == "":
        out.pop()
    return out


def clean_markdown(text: str, *, keep_toc: bool = False) -> str:
    # Normalize newlines
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")

    comments, after_comments = extract_header_comments(lines)
    start = find_content_start(lines, after_comments)
    if start is None:
        # Could not locate article title — return lightly cleaned original.
        body = drop_noise_lines(lines[after_comments:])
        body = collapse_blank_lines(body)
        parts = comments + ([""] if comments and body else []) + body
        return "\n".join(parts) + ("\n" if parts else "")

    end = find_content_end(lines, start)
    body = lines[start:end]

    # Keep title + optional 最近更新时间, drop chrome between title and body.
    cleaned: list[str] = []
    if body:
        cleaned.append(body[0])  # H1
        i = 1
        # optional blank + 最近更新时间
        while i < len(body) and body[i].strip() == "":
            i += 1
        if i < len(body) and UPDATED_RE.match(body[i].strip()):
            cleaned.append("")
            cleaned.append(body[i].strip())
            i += 1
        rest = body[i:]
        rest = drop_noise_lines(rest)
        if not keep_toc:
            rest = drop_toc_block(rest)
        cleaned.extend(rest)

    cleaned = collapse_blank_lines(cleaned)
    parts = comments + ([""] if comments and cleaned else []) + cleaned
    return "\n".join(parts) + "\n"


def process_file(path: Path, *, dry_run: bool, keep_toc: bool) -> tuple[int, int]:
    original = path.read_text(encoding="utf-8")
    cleaned = clean_markdown(original, keep_toc=keep_toc)
    before, after = len(original), len(cleaned)
    if not dry_run and cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
    return before, after


def iter_md_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(target.rglob("*.md"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Remove Tencent Cloud nav/footer noise from fetched Markdown.",
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Markdown file or directory (recursive)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only report size change, do not write",
    )
    parser.add_argument(
        "--keep-toc",
        action="store_true",
        help="Keep '## 本页目录' section",
    )
    args = parser.parse_args()
    target = args.path.resolve()
    if not target.exists():
        print(f"Error: not found: {target}", file=sys.stderr)
        sys.exit(1)

    files = iter_md_files(target)
    if not files:
        print("No .md files found.")
        return

    total_before = total_after = 0
    changed = 0
    for path in files:
        before, after = process_file(path, dry_run=args.dry_run, keep_toc=args.keep_toc)
        total_before += before
        total_after += after
        rel = path
        try:
            rel = path.relative_to(Path.cwd())
        except ValueError:
            pass
        delta = before - after
        flag = "changed" if after != before else "same"
        if after != before:
            changed += 1
        print(f"[{flag}] {rel}: {before} -> {after} (-{delta} bytes, -{delta/before*100:.1f}%)")

    print(
        f"\nFiles: {len(files)}  changed: {changed}  "
        f"total: {total_before} -> {total_after} "
        f"(-{total_before - total_after} bytes, "
        f"-{(total_before - total_after) / total_before * 100:.1f}%)"
    )
    if args.dry_run:
        print("(dry-run: no files written)")


if __name__ == "__main__":
    main()
