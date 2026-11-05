# DevVault: Developer Knowledge Base (Free)

*an Obsidian-compatible Markdown vault (works with Obsidian & Notion)*

A small, plain-Markdown vault for developers: decisions (ADRs), a daily dev log and a code-snippet library.
Works in Obsidian or any Markdown editor — no plugins required.

## Use
1. Download or clone this folder.
2. In Obsidian: *Open folder as vault* and pick `vault/`.
3. Settings → Core plugins → Templates → set template folder to `Templates`.
4. Start at `Home.md`.

## Structure
```
vault/
  Home.md
  Decisions/   ADRs + index
  Logs/        daily dev log
  Snippets/    reusable code notes
  Templates/   ADR, Dev Log, Snippet
```

Check links and frontmatter: `python tools/check_vault.py vault` (needs PyYAML).

## Want more?
**Pro vault ($7):** projects, meetings, postmortems, learning roadmap, interview prep, release checklist,
weekly review, Dataview-style index pages, sample content, plus a Notion import pack (Markdown + CSV databases).

## Notes
- Independent template, not affiliated with or endorsed by Obsidian (Dynalist Inc.), Notion Labs, Inc., or the authors of the Dataview community plugin (Dataview is optional and not included). Obsidian is a trademark of Dynalist Inc.; Notion is a trademark of Notion Labs, Inc.
- Maintained with AI assistance; links and frontmatter are machine-checked before release.
- License: MIT © 2026 Yarrowpine Studio
