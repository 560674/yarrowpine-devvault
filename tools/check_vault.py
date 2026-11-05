#!/usr/bin/env python3
"""Validate an Obsidian-style vault: every [[wikilink]] resolves and every frontmatter block is valid YAML.

Usage: python check_vault.py <vault_dir>     exit code 0 = OK, 1 = problems found
Rules: links resolve by note name (file stem) or relative path, case-insensitive; supports
[[Note|alias]], [[Note#Heading]], ![[embeds]]; links inside fenced code blocks are ignored.
"""
import re
import sys
from pathlib import Path

import yaml

LINK = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FENCE = re.compile(r"^(```|~~~).*?^\1", re.S | re.M)


def check(vault: Path) -> list[str]:
    notes = list(vault.rglob("*.md"))
    names = {p.stem.lower() for p in notes} | {str(p.relative_to(vault).with_suffix("")).lower() for p in notes}
    names |= {p.name.lower() for p in vault.rglob("*") if p.is_file()}
    errors = []
    for p in notes:
        text = p.read_text(encoding="utf-8")
        rel = p.relative_to(vault)
        if text.startswith("---\n"):
            end = text.find("\n---", 4)
            if end == -1:
                errors.append(f"{rel}: frontmatter not closed")
            else:
                try:
                    data = yaml.safe_load(text[4:end])
                    if data is not None and not isinstance(data, dict):
                        errors.append(f"{rel}: frontmatter is not a mapping")
                except yaml.YAMLError as e:
                    errors.append(f"{rel}: invalid YAML frontmatter: {e}".splitlines()[0])
        body = FENCE.sub("", text)
        for m in LINK.finditer(body):
            target = m.group(1).strip()
            if target.lower() not in names and target.lower().removesuffix(".md") not in names:
                errors.append(f"{rel}: unresolved link [[{target}]]")
    return errors


def main() -> int:
    vault = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    errs = check(vault)
    n = len(list(vault.rglob("*.md")))
    for e in errs:
        print("ERROR", e)
    print(f"checked {n} notes: {'OK' if not errs else str(len(errs)) + ' problem(s)'}")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
