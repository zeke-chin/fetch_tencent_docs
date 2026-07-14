#!/usr/bin/env python3
"""Generate a document index under a datas/* directory for agent navigation.

Default format is token-efficient nested groups (no repeated path prefixes).
Optional ASCII tree is available for humans via --style tree.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

TZ_CN = ZoneInfo("Asia/Shanghai")

# Files that should not appear in the index.
SKIP_NAMES = frozenset(
    {
        "urls.json",
        "AGENTS.md",
        "CLAUDE.md",
        "INDEX.md",
        "TREE.md",
        "README.md",
        ".DS_Store",
    }
)

DEFAULT_OUTPUT_NAME = "AGENTS.md"
CLAUDE_LINK_NAME = "CLAUDE.md"


@dataclass
class Node:
    name: str
    is_file: bool = False
    children: dict[str, Node] = field(default_factory=dict)

    def child(self, name: str, *, is_file: bool = False) -> Node:
        if name not in self.children:
            self.children[name] = Node(name=name, is_file=is_file)
        return self.children[name]


def collect_md_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        if path.name in SKIP_NAMES:
            continue
        if any(part.startswith(".") for part in path.relative_to(root).parts):
            continue
        files.append(path)
    return files


def build_tree(root: Path, files: list[Path]) -> Node:
    tree = Node(name=root.name)
    for path in files:
        rel_parts = path.relative_to(root).parts
        node = tree
        for i, part in enumerate(rel_parts):
            node = node.child(part, is_file=(i == len(rel_parts) - 1))
    return tree


def count_files(node: Node) -> int:
    if node.is_file:
        return 1
    return sum(count_files(c) for c in node.children.values())


def sort_nodes(nodes: list[Node]) -> list[Node]:
    """Sort siblings: pair overview.md with same-named dir; file before dir."""

    def key(n: Node) -> tuple[str, int, str]:
        base = n.name[:-3] if n.is_file and n.name.endswith(".md") else n.name
        # 0 = file first, 1 = directory after its overview.md
        return (base.casefold(), 0 if n.is_file else 1, n.name.casefold())

    return sorted(nodes, key=key)


def render_tree(node: Node, prefix: str = "", is_last: bool = True, is_root: bool = True) -> list[str]:
    lines: list[str] = []
    if is_root:
        lines.append(node.name)
        kids = sort_nodes(list(node.children.values()))
        for i, child in enumerate(kids):
            lines.extend(render_tree(child, "", i == len(kids) - 1, is_root=False))
        return lines

    connector = "└── " if is_last else "├── "
    lines.append(f"{prefix}{connector}{node.name}")
    if node.is_file:
        return lines

    kids = sort_nodes(list(node.children.values()))
    extension = "    " if is_last else "│   "
    for i, child in enumerate(kids):
        lines.extend(
            render_tree(child, prefix + extension, i == len(kids) - 1, is_root=False)
        )
    return lines


def render_paths(root: Path, files: list[Path]) -> list[str]:
    """Flat relative paths — cheapest for agents that want grep-friendly lists."""
    return [str(p.relative_to(root)).replace("\\", "/") for p in files]


def render_nested_bullets(node: Node, indent: int = 0) -> list[str]:
    """Render directory children as nested markdown bullets.

    Directory rows look like ``- Go SDK 常见问题/ (99)`` so the parent name
    appears once; children are indented underneath (no repeated prefixes).
    """
    lines: list[str] = []
    pad = "  " * indent
    for child in sort_nodes(list(node.children.values())):
        if child.is_file:
            lines.append(f"{pad}- {child.name}")
        else:
            n = count_files(child)
            lines.append(f"{pad}- {child.name}/ ({n})")
            lines.extend(render_nested_bullets(child, indent + 1))
    return lines


def render_grouped(root: Path, files: list[Path]) -> list[str]:
    """Nested groups under ``## top-level`` sections.

    Avoids repeating parent path prefixes on every line
    (e.g. writing ``Go SDK 常见问题/`` hundreds of times).

    Full path = ``Section/`` + join nested bullet segments
    (strip trailing ``/ (n)`` counts from directory rows).
    """
    tree = build_tree(root, files)
    lines: list[str] = []

    root_files = [c for c in tree.children.values() if c.is_file]
    root_dirs = [c for c in tree.children.values() if not c.is_file]

    if root_files:
        lines.append("## /")
        for f in sort_nodes(root_files):
            lines.append(f"- {f.name}")
        lines.append("")

    for d in sort_nodes(root_dirs):
        n = count_files(d)
        lines.append(f"## {d.name} ({n})")
        lines.extend(render_nested_bullets(d, 0))
        lines.append("")
    return lines


def build_index_markdown(
    root: Path,
    files: list[Path],
    *,
    style: str,
) -> str:
    now = datetime.now(TZ_CN).isoformat(timespec="seconds")
    # Prefer repo-relative root path when possible (portable in git).
    try:
        root_display = str(root.relative_to(Path.cwd())).replace("\\", "/")
    except ValueError:
        root_display = root.name

    header = [
        f"# AGENTS.md — {root.name}",
        "",
        "<!-- auto-generated by gen_index.py; do not edit -->",
        "",
        f"- generated_at: `{now}`",
        f"- root: `{root_display}`",
        f"- files: **{len(files)}**",
        f"- style: `{style}`",
        "",
    ]

    if style == "grouped":
        header.extend(
            [
                "Paths are relative to this directory. Reconstruct a full path as:",
                "",
                "- `## Section` + `- file.md` → `Section/file.md`",
                "- Nested bullets: `- dir/ (n)` + `  - a.md` → `Section/dir/a.md`",
                "- Deeper nesting keeps adding segments; ignore the `(n)` counts",
                "- `## /` bullets are files in this directory itself",
                "",
            ]
        )
    else:
        header.extend(
            [
                "Paths below are relative to this directory (same folder as this file).",
                "Open docs using these relative paths.",
                "",
            ]
        )

    if style == "tree":
        tree = build_tree(root, files)
        body = ["```text", *render_tree(tree), "```", ""]
    elif style == "paths":
        body = ["```text", *render_paths(root, files), "```", ""]
    elif style == "grouped":
        body = render_grouped(root, files)
    else:
        raise ValueError(f"Unknown style: {style}")

    return "\n".join(header + body).rstrip() + "\n"


def ensure_claude_symlink(agents_path: Path) -> Path:
    """Create CLAUDE.md as a relative symlink to AGENTS.md (same directory)."""
    link = agents_path.parent / CLAUDE_LINK_NAME
    target_name = agents_path.name  # relative target, e.g. "AGENTS.md"

    if link.is_symlink() or link.exists():
        link.unlink()

    # Relative symlink: CLAUDE.md -> AGENTS.md
    link.symlink_to(target_name)
    return link


def write_index(
    root: Path,
    *,
    style: str = "grouped",
    output: Path | None = None,
    claude: bool = False,
) -> Path:
    """
    Write AGENTS.md under *root* (or *output*).

    Returns the path of the written index file.
    """
    root = root.resolve()
    if not root.is_dir():
        raise NotADirectoryError(f"not a directory: {root}")

    files = collect_md_files(root)
    text = build_index_markdown(root, files, style=style)

    out = (output.resolve() if output is not None else root / DEFAULT_OUTPUT_NAME)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {out} ({len(files)} files, style={style}, {len(text)} chars)")

    if claude:
        link = ensure_claude_symlink(out)
        print(f"Linked {link.name} -> {out.name}")

    return out


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate AGENTS.md for agent-friendly doc navigation.",
    )
    parser.add_argument(
        "path",
        type=Path,
        help="Directory containing fetched Markdown (e.g. datas/sandbox)",
    )
    parser.add_argument(
        "--style",
        choices=("grouped", "paths", "tree"),
        default="grouped",
        help=(
            "grouped = nested sections without repeated prefixes (default); "
            "paths = flat relative paths; "
            "tree = ASCII tree (human-readable)"
        ),
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help=f"Output file (default: <path>/{DEFAULT_OUTPUT_NAME})",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print to stdout instead of writing a file",
    )
    parser.add_argument(
        "--claude",
        action="store_true",
        help=(
            f"Also create a relative symlink {CLAUDE_LINK_NAME} -> {DEFAULT_OUTPUT_NAME} "
            "(default: off)"
        ),
    )
    args = parser.parse_args()

    root = args.path.resolve()
    if not root.is_dir():
        print(f"Error: not a directory: {root}", file=sys.stderr)
        sys.exit(1)

    if args.stdout:
        files = collect_md_files(root)
        sys.stdout.write(build_index_markdown(root, files, style=args.style))
        return

    write_index(
        root,
        style=args.style,
        output=args.output,
        claude=args.claude,
    )


if __name__ == "__main__":
    main()
