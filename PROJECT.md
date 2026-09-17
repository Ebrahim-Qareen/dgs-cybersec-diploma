# PROJECT.md — DGS Academy Cyber Security Diploma

> Live status. `00_INSTRUCTIONS.md` is the source of truth — this file never restates it.

| Field | Value |
|---|---|
| Phase | **3 — Sessions** (L01 package + paged page built and gated; awaiting review) |
| Published program | 6 modules · 48 sessions × 4 h · 192 h · 79 labs · 6 projects |
| Live delivery | 18 sessions × 6 h over 9 weeks (instructor-private) |
| Repo | `Ebrahim-Qareen/dgs-cybersec-diploma` (public) |
| Site | https://ebrahim-qareen.github.io/dgs-cybersec-diploma/ |
| Last updated | 2026-09-18 |

## Build status

| Item | Status |
|---|---|
| Phase 0 — scaffold | DONE |
| Phase 1 — design docs | DONE — awaiting instructor approval |
| Phase 1 — CSS + site skeleton | DONE |
| Phase 2 — lab setup guide | NOT STARTED |
| Phase 3 — sessions L01–L18 | IN PROGRESS — L01 built, awaiting review |
| Phase 4 — projects P1–P6 | NOT STARTED |
| Phase 5 — publish | Pushed to `Ebrahim-Qareen/dgs-cybersec-diploma` (public) · Pages live from `main` /docs |

## Session status

| L | Title | Package | HTML | Labs | Gate | Published |
|---|---|---|---|---|---|---|
| 01 | Security Foundations & Windows Internals | ✓ | ✓ (17 pages) | — | ✓ | — |
| 02 | Linux Fundamentals & Scripting for Security Ops | — | — | — | — | — |
| 03 | Networking Fundamentals & Protocol Analysis | — | — | — | — | — |
| 04 | Active Directory & Authentication | — | — | — | — | — |
| 05 | Log Analysis + Web Technologies & Attack Awareness | — | — | — | — | — |
| 06 | SOC Operations, Alert Triage & Incident Handling | — | — | — | — | — |
| 07 | Log Analysis & Event Correlation | — | — | — | — | — |
| 08 | Splunk Investigation & Detection Development | — | — | — | — | — |
| 09 | Wazuh Deployment, Monitoring & Detection | — | — | — | — | — |
| 10 | Sigma, Cross-SIEM Rules & Detection Engineering Fundamentals | — | — | — | — | — |
| 11 | Endpoint & Active Directory Attacks and Detection | — | — | — | — | — |
| 12 | Network & Web Attacks and Detection | — | — | — | — | — |
| 13 | Detection Use Cases, Correlation & Alert Tuning | — | — | — | — | — |
| 14 | Threat Hunting Methodology, ATT&CK & Hunting Practice | — | — | — | — | — |
| 15 | IOC Hunting, Threat Intelligence & Enrichment | — | — | — | — | — |
| 16 | Incident Response Lifecycle, Triage & Live Response | — | — | — | — | — |
| 17 | Memory Forensics & Windows Forensic Artifacts | — | — | — | — | — |
| 18 | Malware Triage — Static, Dynamic & IOC Extraction | — | — | — | — | — |

## Folder map (paths that exist today)

```
00_INSTRUCTIONS.md · PROJECT.md · DECISIONS.md · README.md · CLAUDE_PROJECT_SETUP.md · .gitignore
steps/              README.md · 01_scaffold … 07_handover — one file per step (Goal · Done · Doing · Next)
Resources/          source PDFs (gitignored)
design/             session01_body.html (page source, tokenised) · roadmap_analysis.md · topic_map.md · lab_register.md · self_study_register.md · design_system.md · session_template.html
knowledge_base/     00_source_inventory.md · Session_01.md
lab/                (empty)
packages/           session-01/ (session_plan · instructor_guide · student_guide · guided_lab · task_pack · self_study · quiz · cheat_sheet · challenge · build_log)
projects/           (empty)
docs/               index.html · assets/svg/L01/ (8 SVGs) · assets/img/L01/logos/ (7) · assets/L01_ASSET_LICENSES.md · assets/js/session.js · index.html · roadmap.html · labs/ · projects/ · resources/tools.html · resources/practice.html · assets/css/dgs.css · downloads/ · .nojekyll
testing/            verify.py (quality gate)
tools/              build_site.py · extract_source.py · extract_all.py · extract_manifest.txt
```

## Open decisions

| # | Question | Status |
|---|---|---|
| Q1 | Approve the 18-session live map in `design/roadmap_analysis.md` | OPEN |
| Q2 | Confirm 6 h per live session (or state the real length) | OPEN |
| Q3 | Exact DGS brand hex values (current palette is sampled from the brochure) | OPEN |
| Q4 | Student hardware floor 16 GB RAM — or run SIEM VMs on the instructor host | OPEN |
| Q5 | Class size and team size for P6 | OPEN |
