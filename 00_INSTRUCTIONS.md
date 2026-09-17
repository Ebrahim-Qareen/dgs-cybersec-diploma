# DGS Academy — Cyber Security Diploma — Project Instructions

> Single source of truth. Read this file and `DECISIONS.md` before doing anything else, every session.
> Everything else in the repo references this file and never restates it.
> Items marked **[CONFIRM]** are assumptions waiting for Ebrahim's approval.

---

## Part 0 — Identity

| Field | Value |
|---|---|
| Project | `DGS_CyberSec_Diploma` |
| Academy | DGS Academy |
| Program | Cyber Security Diploma — 6-Month Intensive Professional Program (Blue Team / Security Operations track) |
| Owner / Lead instructor | Ebrahim Mohamed Ahmed |
| Working tree | `E:\Work\DGS Academy\DGS_CyberSec_Diploma` |
| Repo | `github.com/Ebrahim-Qareen/dgs-cybersec-diploma` — **public** |
| Site | GitHub Pages from `docs/` |
| Contract source | `Resources/DGS Academy - Cyber Security Diploma Roadmap.pdf` (6 pages, 6 modules) |
| Superseded source | The older 12-week / 96 h roadmap. **Not the contract.** Kept for reference only. |
| Material language | Professional simple English — all files, pages, labs, quizzes |
| Delivery language | Egyptian Arabic speech, English technical terms |

**Mission:** take a beginner to a job-ready entry-level Blue Team analyst — SOC Analyst T1, Alert Triage, Security Monitoring, Junior Incident Responder — through labs and real investigations.

**Audience:** mixed beginner-to-intermediate. **No prerequisites assumed** — no CCNA, no Linux, no CEH. This overrides the `course-architect` skill default.

---

## Part 1 — Locked Program Facts (published contract)

Fixed unless DGS changes the brochure. These numbers are what the student paid for and must stay true.

| Fact | Value |
|---|---|
| Duration | 6 months |
| Cadence | 2 sessions / week |
| Published sessions | 48 × 4 h |
| Training hours | 192 |
| Practical tasks | 48 |
| Hands-on labs | 79 |
| Projects | 6 |
| Assessment | Labs · real investigations · projects |

### Published modules

| M | Module | Sessions | Hours | Topics | Labs | Project |
|---|---|---|---|---|---|---|
| 1 | Foundation Phase — Computer, OS, Networking & Security Fundamentals | 16 | 64 | 8 | 24 | 1 |
| 2 | Security Operations (SOC) & SIEM | 10 | 40 | 5 | 18 | 1 |
| 3 | Attack Analysis & Detection Engineering | 8 | 32 | 8 | 14 | 1 |
| 4 | Threat Hunting & Threat Intelligence | 6 | 24 | 6 | 10 | 1 |
| 5 | Incident Response & Digital Forensics | 6 | 24 | 6 | 10 | 1 |
| 6 | Malware Analysis for Analysts (triage) | 2 | 8 | 2 | 3 | 1 |
| | **Total** | **48** | **192** | **35** | **79** | **6** |

### Published topic lines (the 35 the brochure sells — every one must be covered)

**M1:** (1) Computer, Operating Systems & Security Fundamentals · (2) Windows Internals & Linux Fundamentals · (3) Networking Fundamentals & Protocol Analysis · (4) PowerShell & Bash for Security Operations · (5) Active Directory & Authentication Fundamentals · (6) Windows, Linux & Web Log Analysis · (7) Web Technologies & Common Attack Awareness · (8) Foundation Investigation & Capstone

**M2:** (1) SOC Operations, Alert Triage & Incident Handling · (2) Log Analysis & Event Correlation · (3) Splunk Investigation & Detection Development · (4) Wazuh Deployment, Monitoring & Detection · (5) Sigma Rules & Cross-SIEM Detection Engineering

**M3:** (1) Detection Engineering Fundamentals · (2) Endpoint Attacks & Detection Techniques · (3) Active Directory Attacks & Detection · (4) Network Attacks & Detection Techniques · (5) Web Attacks & Detection Techniques · (6) Detection Use Cases & Correlation Logic · (7) Alert Tuning & False Positive Reduction · (8) Detection Development Project

**M4:** (1) Threat Hunting Methodology · (2) MITRE ATT&CK & Adversary Behaviors · (3) Endpoint, Network & Log-Based Hunting · (4) IOC Hunting & Threat Intelligence · (5) Threat Intelligence Platforms & Enrichment · (6) Threat Hunting Investigation Project

**M5:** (1) Incident Response Lifecycle · (2) Triage, Scoping & Containment · (3) Live Response & Evidence Collection · (4) Memory Forensics · (5) Windows Forensic Artifacts Analysis · (6) Incident Investigation Case Study

**M6:** (1) Static Malware Analysis & IOC Extraction · (2) Dynamic Analysis, Sandboxing & Malware Triage

### Published tools (every tool must appear in at least one lab)

Splunk · Wazuh · Sigma · TheHive · Sysmon · Windows Event Viewer · Linux audit logs · MITRE ATT&CK Navigator · D3FEND · MISP · AlienVault OTX · VirusTotal · Volatility 3 · Autopsy · PowerShell · Bash · Python

### Published outcomes

- Roles: SOC Analyst T1 · Security Monitoring Analyst · Junior Incident Responder · SIEM Support Analyst
- Practice platforms: LetsDefend · Blue Team Labs Online · CyberDefenders · TryHackMe · Splunk BOTS
- Certs: THM Pre Security / Cyber Security 101 / SOC Level 1 · Cisco Intro to Cyber / Networking Basics / Endpoint Security · then Security+ · SC-200 · BTL1

---

## Part 2 — Delivery Plan (INSTRUCTOR-PRIVATE — never appears in any student material)

> **Hard rule:** no file under `docs/`, `packages/`, `lab/` or `projects/` may mention 2 months, 18 sessions, 6-hour sessions, compression, or "self-study because of time". Students see the published 6-module program only. This section exists so the build fits the real calendar.

**Real delivery:** 2 months · 9 teaching weeks · 2 sessions per week · **6 h per live session [CONFIRM]** → **18 live sessions = 108 live hours**.

The remaining 84 published hours are delivered as **structured self-study packs (SSP)** and post-session task packs that students do between sessions. Total student workload stays at 192 h, so the brochure stays true.

| | Published | Delivered live | Delivered as SSP / task packs |
|---|---|---|---|
| Hours | 192 | 108 | 84 |
| Sessions | 48 × 4 h | 18 × 6 h | — |
| Labs | 79 | ~36 guided in class | ~43 as task packs and self-study |
| Tasks | 48 | 18 task packs (2–3 published tasks each) | — |
| Projects | 6 | kicked off in class, reviewed in class | built at home |

### Live session map (L01–L18) — **[CONFIRM]**

| L | Wk | Module | Live session title | Published topics covered | Project gate |
|---|---|---|---|---|---|
| 01 | 1 | M1 | Security Foundations & Windows Internals | M1.1, M1.2a | — |
| 02 | 1 | M1 | Linux Fundamentals & Scripting for Security Ops | M1.2b, M1.4 | — |
| 03 | 2 | M1 | Networking Fundamentals & Protocol Analysis | M1.3 | — |
| 04 | 2 | M1 | Active Directory & Authentication | M1.5 | — |
| 05 | 3 | M1 | Log Analysis + Web Technologies & Attack Awareness | M1.6, M1.7 | **P1 kickoff** (M1.8) |
| 06 | 3 | M2 | SOC Operations, Alert Triage & Incident Handling | M2.1 | P1 review |
| 07 | 4 | M2 | Log Analysis & Event Correlation | M2.2 | — |
| 08 | 4 | M2 | Splunk Investigation & Detection Development | M2.3 | — |
| 09 | 5 | M2 | Wazuh Deployment, Monitoring & Detection | M2.4 | **P2 kickoff** |
| 10 | 5 | M2/M3 | Sigma, Cross-SIEM Rules & Detection Engineering Fundamentals | M2.5, M3.1 | P2 review |
| 11 | 6 | M3 | Endpoint & Active Directory Attacks and Detection | M3.2, M3.3 | — |
| 12 | 6 | M3 | Network & Web Attacks and Detection | M3.4, M3.5 | — |
| 13 | 7 | M3 | Detection Use Cases, Correlation & Alert Tuning | M3.6, M3.7 | **P3 kickoff** (M3.8) |
| 14 | 7 | M4 | Threat Hunting Methodology, ATT&CK & Hunting Practice | M4.1, M4.2, M4.3 | P3 review |
| 15 | 8 | M4 | IOC Hunting, Threat Intelligence & Enrichment | M4.4, M4.5 | **P4 kickoff** (M4.6) |
| 16 | 8 | M5 | Incident Response Lifecycle, Triage & Live Response | M5.1, M5.2, M5.3 | P4 review |
| 17 | 9 | M5 | Memory Forensics & Windows Forensic Artifacts | M5.4, M5.5 | **P5 kickoff** (M5.6) |
| 18 | 9 | M6 | Malware Triage — Static, Dynamic & IOC Extraction | M6.1, M6.2 | P5 review · **P6 final + presentations** |

Coverage check: all 35 published topic lines appear exactly once. All 6 projects have a live kickoff and a live review.

### Compression rules (how the material is written so 4 h of content fits 3 h of class)

| # | Rule |
|---|---|
| C1 | **Teach once.** A concept is taught in exactly one session; later sessions reference it, never re-teach it. `design/topic_map.md` is the authority. |
| C2 | **Just enough to defend.** Foundation content that no later detection/IR/forensics session depends on moves to a self-study pack, not the class. |
| C3 | **Attack from the detection side.** Attack demo ≤ 25 % of a block; the rest is what the SOC sees — log line, Event ID, MITRE ID, detection logic. |
| C4 | **No installs in class.** Students arrive with the prepared lab image. Setup pack ships before L01 and is a prerequisite, not a lesson. |
| C5 | **Split long labs.** Guided core in class, extension at home in the task pack. Each in-class lab ≤ 60 min. |
| C6 | **In-class teaching order is 8 parts** of the 12-part framework: Why → definition + analogy → how it works → how attackers abuse it → what the SOC sees (+ MITRE ID) → guided lab → takeaways → task handout. The other 4 — case study, technical deep dive, quiz, transition — live in the student pack and are assigned, not lectured. |
| C7 | **One dataset per module.** The same lab dataset carries across the sessions of a module so students never re-learn the environment. |
| C8 | **Quizzes are self-marking** on the site, done at home; class time is never spent on quizzes. |

### Pacing risks to watch

- L01 and L02 carry 8 published hours each — the densest points. Setup pack and pre-reading are mandatory.
- L14 and L16 merge three published topics each — build them as three tight blocks, not one long lecture.
- M1 drops from 64 published hours to 30 live hours. Anything cut from class must exist in an SSP file and be listed in `design/self_study_register.md`.

---

## Part 3 — Session Shape (6 h = 360 min) **[CONFIRM]**

| Block | Min | Content |
|---|---|---|
| Recap + previous task review | 20 | 3 questions, walk one student solution |
| Teach block A | 70 | Concept → visual → instructor demo |
| Break | 15 | — |
| Guided lab A | 70 | Students mirror the demo, instructor-led |
| Teach block B | 65 | Second topic, same pattern |
| Break | 15 | — |
| Independent lab B | 80 | Students solve alone or in pairs, hints only |
| Wrap-up | 25 | Takeaways, task pack handout, next session hook |
| **Total** | **360** | Hands-on ≥ 50 % of teaching minutes |

Weave attacker and victim psychology into every topic — why people click, why admins misconfigure, why an analyst closes a true positive as noise.

---

## Part 4 — Lab Environment

One current design, edited in place. No versioned rebuilds. Documented only in `lab/setup_guide.md`.

| VM | OS / role | First used |
|---|---|---|
| `DGS-WS01` | Windows 10/11 — Sysmon, Wazuh agent, Splunk UF — victim endpoint | L01 |
| `DGS-LNX01` | Ubuntu Server — Apache + DVWA + SSH — Linux / web target | L02 |
| `DGS-DC01` | Windows Server 2022 — AD DS domain controller | L04 |
| `DGS-SIEM01` | Ubuntu — Wazuh all-in-one + TheHive | L06 |
| `DGS-SPLK01` | Ubuntu — Splunk Free | L08 |
| `DGS-KALI` | Kali Linux — attack simulation only | L11 |

- Network: host-only `10.10.10.0/24`; NAT only on the attacker VM when a lab needs it.
- Snapshots: `BASE` after install, `CLEAN-TOOLS` after tooling, one per session when state changes.
- Student hardware floor: 16 GB RAM **[CONFIRM]**. Heavy VMs (SIEM, Splunk) may run on the instructor host with students connecting by browser.
- No real malware in student VMs. Simulations only — Atomic Red Team, EICAR, scripted attacks. M6 dynamic analysis runs on an isolated instructor-hosted sandbox.
- Public evidence sets (CyberDefenders, Volatility samples, BOTS data) are **linked, never rehosted**.
- Every file a lab or task needs is published under `docs/downloads/` with a SHA-256 in the page, so students download it in one click.

---

## Part 5 — Per-Session Package (fixed set)

`packages/session-NN/` contains exactly these files — NN is the **live** session number (01–18):

| File | Purpose |
|---|---|
| `session_plan.md` | Objectives, 360-min timing table, published topics covered, labs, dependencies |
| `instructor_guide.md` | What to say per block, demo steps, questions to ask, common student mistakes |
| `student_guide.md` | Clean reference notes — includes the 4 framework parts moved out of class |
| `guided_lab.md` | Step-by-step labs with expected output |
| `task_pack.md` | Post-session practical tasks (2–3 published tasks) with expected output |
| `self_study.md` | The SSP for this session — content moved out of class, with links and a time estimate |
| `quiz.md` | 10 MCQ + 2 practical, with answer key |
| `build_log.md` | What was built, sources used, verification results, open issues |

`instructor_guide.md`, answer keys and project answer keys are **instructor-private** — never copied into `docs/`.

**Lab IDs:** `LAB-LNN-X` (e.g. `LAB-L08-B`). The register `design/lab_register.md` must always total **79** and tag each lab `LIVE` / `TASK` / `SELF`.

---

## Part 6 — Projects

| P | Live gate | Scope | Deliverable |
|---|---|---|---|
| P1 | kickoff L05, review L06 | M1 — foundation investigation | Written investigation report from a provided log set |
| P2 | kickoff L09, review L10 | M2 — SOC & SIEM | Triage 5 alerts end to end in Wazuh + TheHive case |
| P3 | kickoff L13, review L14 | M3 — detection development | 5 working detections (Sigma → Splunk + Wazuh) with test evidence |
| P4 | kickoff L15, review L16 | M4 — threat hunt | Hunt hypothesis, queries, findings, IOC report |
| P5 | kickoff L17, review L18 | M5 — incident investigation | Full incident report with timeline and evidence |
| P6 | L18 | Whole program | Multi-source investigation + 10-min presentation |

Rules: fictional company and users, documentation IP ranges only, no real PII. Answer keys live in `projects/` and are **never published** to `docs/`. Rubric for every project: Method · Findings · Evidence · Detection quality · Communication.

---

## Part 7 — Visual System

- Dark DGS theme. Palette **[CONFIRM exact brand hex]**: Navy `#061A33` · Deep `#0A2547` · Primary blue `#0B5CC7` · Sky `#1AA3E0` · Accent orange `#F5821F` · Text `#E6EEF8` · Muted `#8FA6C0`.
- One shared stylesheet `docs/assets/css/dgs.css`. No per-page `<style>` blocks beyond page-specific overrides, no external CSS/JS/fonts, no remote images.
- Diagrams are **inline SVG only**. Screenshots must be from our own lab or clearly licensed.
- Every session page: header → objectives → visual flow → callout boxes (Why it matters · Attacker view · Analyst view · Red flag · Lab) → evidence boxes (real log/packet + one SOC sentence) → quiz → next-session link.
- Mobile responsive; wide tables scroll inside their own container.

**Site map (`docs/`):** `index.html` · `roadmap.html` · `m{M}/unit-NN/index.html` × 18 · `labs/index.html` · `projects/index.html` · `resources/tools.html` · `resources/practice.html` · `downloads/` · `.nojekyll`

**Naming rule:** the repo uses `packages/session-NN/` internally, but the **site never numbers sessions** — pages are *Unit NN* inside a module, and the site presents the published 6 modules / 35 topics. Page template: `design/session_template.html`.

---

## Part 8 — Build Workflow (per session)

1. Intake sources → `knowledge_base/` (condensed notes, never full copies).
2. Outline gate — page-by-page outline approved before any HTML exists.
3. Build the Part 5 markdown package.
4. Build `docs/session-NN/index.html` from the approved package.
5. Build and test the labs in the real lab VMs.
6. Run the Part 9 quality gate.
7. Ebrahim reviews → approve or revise.
8. Publish (Part 11) — only with a fresh explicit go-ahead.
9. Update `PROJECT.md` status and append to `DECISIONS.md`.

Sessions are built **in order**. The next session does not start until the current one is approved.

---

## Part 9 — Quality Gate (must pass before publish)

- [ ] Every published topic mapped to this session is covered — verified by term search
- [ ] `lab_register.md` still totals 79 and this session's labs exist
- [ ] Every tool claimed for this session is actually used in a lab
- [ ] The 8-part in-class order is present for each major topic; the other 4 parts exist in `student_guide.md`
- [ ] Every attack shown is paired with its detection and a MITRE ATT&CK ID
- [ ] Findings (fact) are visually separated from Interpretation (analysis) in every investigation
- [ ] Quiz has an answer key; every task has expected output
- [ ] No credentials, real PII, API keys, or IPs outside `10.10.10.0/24`
- [ ] No mention of the 2-month / 18-session delivery anywhere outside this file and `DECISIONS.md`
- [ ] HTML: no broken links, no external assets, renders on mobile
- [ ] Verification recorded in `build_log.md`: file list, SHA-256 hashes, element counts

---

## Part 10 — Skills

| Skill | One job | Status |
|---|---|---|
| `dgs-intake` | One source → one condensed `knowledge_base/` note; owns `design/topic_map.md` | To build |
| `dgs-design` | Owns `design/roadmap_analysis.md`, `lab_register.md`, `self_study_register.md`; places and re-sequences topics | To build |
| `dgs-session-package` | The Part 5 file set, including projects | To build |
| `dgs-session-html` | Session page from the approved package, using `design_system.md` | To build |
| `dgs-lab-build` | Lab VMs, `lab/setup_guide.md` — one current design | To build |
| `dgs-publish` | Pre-commit secret + PII scan, stage explicit paths, commit, Pages check | To build |
| `course-architect` | Roadmap analysis and balancing | Reuse — override its CCNA/CEH audience assumption |
| `ceh-web-research`, `ceh-chrome-extract` | Online research and platform extraction | Reuse as-is |

**Trap:** a `.skill` file delivered in chat is **not** installed. Verify by listing skills with keyword `dgs` and counting — never trust a "delivered" status row.

Never run two extractors on the same source.

---

## Part 11 — Environment & Publishing Constraints

- The device mount **writes but cannot delete** without explicit permission — build generators and scratch files in the cloud container, never inside the project tree.
- Use python read-modify-write, not `sed -i`, on mounted files.
- Never run git commands that remove refs or objects on the mount. `gc.auto=0` is set at init.
- After every commit on the mount, clear the leftovers git could not delete:
  `rm -f .git/*.lock .git/objects/*.lock && find .git -name 'tmp_obj_*' -delete` — request delete permission for
  `E:\Work\DGS Academy` once per session first, or the next commit fails on `index.lock`.
- `git push` has **no credentials** here. Commit locally; Ebrahim pushes from GitHub Desktop or PowerShell.
- **Never push without a fresh explicit go-ahead from Ebrahim**, for every push.
- Pre-commit credential + PII scan is a release gate.
- A parallel session may edit the same files — re-read `DECISIONS.md` before appending.

---

## Part 12 — Standing Rules

| # | Rule |
|---|---|
| R1 | No `v2` / `final` / `new` files — edit in place, log the change in `DECISIONS.md` |
| R2 | Delete superseded material; never archive it in the tree |
| R3 | Strict folder separation — each folder has one owner skill |
| R4 | `DECISIONS.md` is append-only (D1, D2, …) |
| R5 | `PROJECT.md` lists only paths that exist |
| R6 | No secrets, no real PII, no malware samples, no evidence bytes in the repo |
| R7 | Outline approved before HTML |
| R8 | Sessions built in order, one approved before the next |
| R9 | Every attack shown is paired with its detection |
| R10 | Real evidence only — log lines, Event IDs, packets come from a real capture or real lab log, never invented |
| R11 | Legal targets only — local lab or named training platforms |
| R12 | Free tiers only when linking platform rooms; verify the tier before linking |
| R13 | Students never see internal file names (`task_pack.md`, `self_study.md`) — the site exposes downloads and pages, not the repo layout |
| R14 | Chat replies stay short: **DONE / ISSUE first**, then next step, then what Ebrahim must decide. Detail belongs in the files |
| R15 | Verify before declaring done: hashes, counts, checklist |

---

## Part 13 — Folder Structure

```
DGS_CyberSec_Diploma/
├── 00_INSTRUCTIONS.md          ← this file (instructor-private)
├── PROJECT.md                  ← live status + folder map
├── DECISIONS.md                ← append-only D-log
├── README.md                   ← public landing text
├── .gitignore
├── Resources/                  ← source PDFs (gitignored)
├── design/
│   ├── roadmap_analysis.md     ← published 48 → live 18 mapping
│   ├── topic_map.md            ← topic → session → lab → tool
│   ├── lab_register.md         ← 79 labs, IDs, delivery tag
│   ├── self_study_register.md  ← every hour moved out of class
│   └── design_system.md
├── knowledge_base/             ← condensed source notes
├── lab/setup_guide.md
├── packages/session-01 … session-18/
├── projects/                   ← briefs, datasets, answer keys (never published)
├── docs/                       ← GitHub Pages site
├── testing/                    ← gate scripts
└── tools/                      ← scaffold + scan scripts
```

Create a folder only when first used and update `PROJECT.md` in the same commit.

---

## Part 14 — Phase Plan

| Phase | Output | Exit gate |
|---|---|---|
| 0 — Scaffold | Folders, `PROJECT.md`, `DECISIONS.md`, `.gitignore`, `git init` | Repo exists, zero secrets |
| 1 — Design | `roadmap_analysis.md`, `topic_map.md`, `lab_register.md` (=79), `self_study_register.md`, `design_system.md`, CSS + base template | Ebrahim approves the 18-session map |
| 2 — Lab | 6 VMs built, snapshots, `lab/setup_guide.md`, setup pack published | Every Part 1 tool launches in the lab |
| 3 — Sessions | L01 → L18 per Part 8 | Each passes Part 9 |
| 4 — Projects | 6 briefs, datasets, answer keys staged and tested | Answer key reproduces from the evidence |
| 5 — Publish | Full site live on GitHub Pages | All pages and links verified live |

---

## Part 15 — Kick-off Prompt (paste at the start of a new chat)

```
Read 00_INSTRUCTIONS.md and DECISIONS.md fully before anything else.
Tell me which phase we are in from PROJECT.md, then continue from there.
Never mention the 2-month delivery in any student-facing file.
Keep replies short: DONE/ISSUE first, then the next step, then what I must decide.
Verify with hashes and counts before calling anything done.
```

## Part 16 — Claude Project Custom Instructions (paste into Project settings)

```
Project: DGS Academy Cyber Security Diploma — published as 6 months, 48 sessions x 4h, 192h, 79 labs, 6 projects, Blue Team/SOC track.
00_INSTRUCTIONS.md is the single source of truth. Read it and DECISIONS.md before any work.
Delivery is compressed to 18 live sessions — instructor-private, never written in student material.
Audience: beginners to intermediate, no prerequisites. All material in professional simple English.
Follow the 8-part in-class teaching order; pair every attack with its detection and MITRE ATT&CK ID.
Outline before HTML. Sessions in order. No v2 files. DECISIONS.md is append-only.
Never push to GitHub without a fresh explicit go-ahead.
Replies short: DONE/ISSUE first, then next step, then what I must decide. Detail goes in files, not chat.
Verify with hashes and counts before calling anything done.
```
