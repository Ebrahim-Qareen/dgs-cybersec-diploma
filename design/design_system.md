# Design System — DGS Cyber Security Diploma Site

> Owner skill: `dgs-session-html`. One stylesheet: `docs/assets/css/dgs.css`. No page may define its own colours.

## Palette (sampled from the DGS brochure — **[CONFIRM exact brand hex]**)

| Token | Hex | Use |
|---|---|---|
| `--navy` | `#061A33` | Page background |
| `--deep` | `#0A2547` | Card / panel background |
| `--line` | `#123A66` | Borders, dividers |
| `--blue` | `#0B5CC7` | Primary actions, links, module accents |
| `--sky` | `#1AA3E0` | Highlights, diagram strokes, hover |
| `--orange` | `#F5821F` | Accent — attacker view, warnings, active nav |
| `--green` | `#27C08A` | Analyst view, correct answer, success |
| `--red` | `#E5484D` | Red flag, false positive, danger |
| `--text` | `#E6EEF8` | Body text |
| `--muted` | `#8FA6C0` | Secondary text, captions |

Contrast: body text on `--navy` ≥ 12:1; muted text ≥ 4.5:1. Never use `--orange` as a text colour on `--navy` below 16 px.

## Typography

- System stack only — no remote fonts: `-apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`.
- Code: `"Cascadia Code", "Consolas", "SF Mono", monospace`.
- Scale: h1 2.2rem · h2 1.6rem · h3 1.2rem · body 1rem/1.7 · caption 0.85rem.
- Line length capped at 78 characters in prose blocks.

## Layout

- Max content width 1100 px, 16 px side gutter on phones.
- Session page order: header → objectives → visual flow → content sections → labs → quiz → next-session link.
- Wide tables scroll inside `.table-wrap`; the page itself never scrolls sideways.
- Sticky top nav with the module colour bar; sticky section index on screens ≥ 1000 px.

## Callout boxes (fixed set — never invent a new one)

| Class | Label | Colour | Use |
|---|---|---|---|
| `.box-why` | Why it matters | blue | Opens every topic |
| `.box-attacker` | Attacker view | orange | How the technique is abused |
| `.box-analyst` | Analyst view | green | What the SOC does about it |
| `.box-flag` | Red flag | red | Indicator to look for |
| `.box-lab` | Lab | sky | Hands-on step block |
| `.box-evidence` | Evidence | deep + mono | Real log line, packet or Event ID + one SOC sentence |
| `.box-note` | Note | muted | Side information |

## Evidence blocks

Every technique ends with an evidence block: real log line or packet row, the source (`Sysmon EID 1`, `Apache access.log`), the MITRE ATT&CK ID, and one sentence of what the analyst concludes. **Findings and interpretation are visually separated** — the log is in mono on `--deep`, the interpretation is in the `.box-analyst` below it.

## Diagrams

- Inline SVG only. No images from the internet, no icon fonts.
- Stroke `--sky` 2 px, fills from the palette at 12 % opacity, labels in `--text` 13 px.
- Every flow reads left to right or top to bottom, numbered steps, one idea per node.
- Every diagram has a one-line caption under it that states the takeaway.

## Quiz

Self-marking MCQ blocks — inline `<details>` for the answer, no external JS. 10 MCQ + 2 practical per session.

## Rules

1. One stylesheet; page-specific CSS is a bug.
2. No external assets of any kind — the site must render with no internet.
3. Every page passes: no broken internal link, no console error, readable at 360 px width.
4. Screenshots come from our own lab, never from a vendor site.
