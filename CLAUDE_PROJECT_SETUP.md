# Set up the Claude Project — 5 minutes

## 1. Create the project
claude.ai → Projects → **New project** → name: `DGS Cyber Security Diploma`

## 2. Paste these custom instructions

```
Project: DGS Academy Cyber Security Diploma. Published: 6 months, 48 sessions x 4h, 192h, 79 labs, 6 projects, Blue Team/SOC track.
Working tree: E:\Work\DGS Academy\DGS_CyberSec_Diploma  ·  Repo: Ebrahim-Qareen/dgs-cybersec-diploma  ·  Site: ebrahim-qareen.github.io/dgs-cybersec-diploma
Source material: E:\Work\ADA Egypt\Cyber Security (SOC 4-Month diploma + Defensive diploma) and TryHackMe free rooms.
00_INSTRUCTIONS.md is the single source of truth. Read it, PROJECT.md and the step file marked IN PROGRESS before any work.
Delivery is 18 live sessions in 2 months — instructor-private, never written in student material.
All material in simple short English. Diagrams, SVGs, screenshots and icons first, text second. Every attack paired with its detection and MITRE ATT&CK ID.
Outline before HTML. Sessions in order, one approved before the next. No v2 files. DECISIONS.md append-only. Update the step file in the same commit.
Never push without my fresh go-ahead. Replies short: DONE/ISSUE first, then next step, then what I must decide.
```

## 3. Upload these files to project knowledge (7 files)

| File | Why |
|---|---|
| `00_INSTRUCTIONS.md` | the rules |
| `PROJECT.md` | live status |
| `DECISIONS.md` | why things are the way they are |
| `steps/README.md` | which step we are in |
| `design/roadmap_analysis.md` | the 18-session map |
| `design/lab_register.md` | the 79 labs |
| `knowledge_base/00_source_inventory.md` | which source feeds which session |

Re-upload `PROJECT.md`, `DECISIONS.md` and the current step file whenever they change. A ready zip of all seven is beside the repo: `E:\Work\DGS Academy\Claude_Project_Kit.zip`.

## 4. Start every chat with

```
Read 00_INSTRUCTIONS.md, PROJECT.md and steps/README.md. Tell me the current step and continue it.
```

## 5. Say these to move things
- `map approved` — closes Step 2
- `go L01` — Step 4 condenses L01, then Step 5 sends the outline
- `outline approved` — build starts
- `publish` — push to GitHub (I never push without it)
