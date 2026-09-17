# Design System — DGS Cyber Security Diploma Site

> Owner skill: `dgs-session-html`. One stylesheet: `docs/assets/css/dgs.css`. No page may define its own colours.

## Palette — sampled from the DGS Academy logo

The logo is the source of truth: letter navy `#0C3060`, circuit blue `#185490`/`#18609C`, swoosh orange
`#E48424`. Surfaces are darker than the logo navy so the logo reads on top of them.

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#060E1C` | Page background |
| `--bg-alt` | `#0A1729` | Footer, inset bands |
| `--panel` | `#0E2140` | Cards, boxes, tables |
| `--panel-2` | `#12305A` | Table headers, raised rows |
| `--line` / `--line-soft` | `#1B3A66` / `#27528C` | Borders, dividers |
| `--navy` | `#0C3060` | The logo's letter navy |
| `--orange` | `#E48424` | **Primary brand accent** — kickers, active nav, "why it matters", primary button |
| `--orange-soft` / `--orange-dim` | `#F7A94A` / `#B9691A` | Hover, gradient end |
| `--blue` | `#2E86DE` | Module 1, secondary accent |
| `--sky` | `#4FB8F0` | Links, stat numbers, lab boxes, diagram strokes |
| `--green` | `#2DD4A0` | Analyst view, verified, correct answer |
| `--red` | `#FF5C6C` | Attacker view, red flag, danger |
| `--purple` | `#A78BFA` | Activities, ATT&CK IDs |
| `--amber` | `#FBBF24` | Key takeaway |
| `--text` / `--text-2` / `--text-3` / `--text-4` | `#E6EEF8` / `#A8BBD6` / `#7E93B5` / `#5C7096` | Text ramp |

**Module colours** (rails, tags): M1 blue · M2 sky · M3 orange · M4 green · M5 purple · M6 red.

## Logo rules

- Files: `docs/assets/img/dgs-logo.png` (760 px wide, transparent) and `favicon.png` (128 px).
- The logo's letters are navy, so it **never sits directly on a dark surface** — always inside a white
  plate (`.plate`, radius 10 px, 5–8 px padding) or the white hero badge.
- Never recolour, rotate, outline or stretch the logo. Minimum width 78 px.
- The logo is the only raster asset on the site; everything else is CSS or inline SVG.

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

## Build rule

Pages under `docs/` are **generated** by `tools/build_site.py` from this system plus the `design/` data
files — never hand-edited. Change the content in the builder, run it, then run `testing/verify.py`.

## Rules

1. One stylesheet; page-specific CSS is a bug.
2. No external assets of any kind — the site must render with no internet.
3. Every page passes: no broken internal link, no console error, readable at 360 px width.
4. Screenshots come from our own lab, never from a vendor site.
