#!/usr/bin/env python3
"""
Compile wiki pages into wiki_context.md for the digital twin agent.

Run this whenever you update your wiki:
    python build_wiki_context.py

The output is committed to the day-4 repo so Railway can access it.
"""
import re
import sys
from pathlib import Path

WIKI_DIR = Path(__file__).parent / "wiki"
OUTPUT_FILE = Path(__file__).parent / "agent" / "wiki_context.md"
SEARCH_DIRS = ["pages", "sources"]


def strip_frontmatter(content: str) -> str:
    """Remove YAML frontmatter block from markdown."""
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            return content[end + 3:].lstrip("\n")
    return content


def get_title(content: str, fallback: str) -> str:
    match = re.search(r"^title:\s*(.+)", content, re.MULTILINE)
    return match.group(1).strip() if match else fallback


pages = []
for subdir in SEARCH_DIRS:
    search_path = WIKI_DIR / subdir
    if not search_path.exists():
        continue
    for path in sorted(search_path.rglob("*.md")):
        raw = path.read_text(encoding="utf-8")
        title = get_title(raw, path.stem)
        body = strip_frontmatter(raw).strip()
        if body:
            pages.append((title, body))

if not pages:
    print("No wiki pages found. Check WIKI_DIR path.", file=sys.stderr)
    sys.exit(1)

sections = [f"## {title}\n\n{body}" for title, body in pages]
output = (
    "# Danning's Personal Wiki\n\n"
    "This is a compiled knowledge base representing what Danning has learned and studied. "
    "Use it to answer questions about topics, people, concepts, and projects Danning has engaged with.\n\n"
    "---\n\n"
    + "\n\n---\n\n".join(sections)
)

OUTPUT_FILE.write_text(output, encoding="utf-8")
print(f"Compiled {len(pages)} wiki pages → {OUTPUT_FILE}")
