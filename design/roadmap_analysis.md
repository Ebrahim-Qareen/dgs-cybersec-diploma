# Roadmap Analysis — Published 48 Sessions → Live 18 Sessions

> Owner skill: `dgs-design`. Source of truth for sequencing. Instructor-private.
> Student-facing material describes the published program only (Part 1 of `00_INSTRUCTIONS.md`).

## 1. What the brochure promises

192 h · 48 sessions × 4 h · 48 practical tasks · 79 labs · 6 projects · 6 modules · 35 topic lines.

## 2. What is actually delivered

| | Published | Live in class | Outside class |
|---|---|---|---|
| Hours | 192 | 108 | 84 |
| Sessions | 48 × 4 h | 18 × 6 h over 9 weeks | — |
| Labs | 79 | 36 guided | 25 task packs + 18 self-study |
| Tasks | 48 | — | 18 task packs, each holding 2–3 published tasks |
| Projects | 6 | kickoff + review in class | built at home |

Student workload still totals 192 h. Nothing promised is dropped — content is moved, not deleted, and every moved hour is recorded in `self_study_register.md`.

## 3. Compression method

| Step | What was done |
|---|---|
| 1 | Listed the 35 published topic lines and mapped each to exactly one live session |
| 2 | Merged topics that share a dataset, a tool or a mental model (e.g. endpoint + AD attacks) |
| 3 | Moved every foundation item that no later session depends on into a self-study pack |
| 4 | Converted the 4-hour session shape into a 6-hour shape with two teach/lab pairs |
| 5 | Cut the in-class teaching order from 12 parts to 8; the other 4 became student-pack reading |
| 6 | Pulled all tool installation out of class into a pre-course setup pack |
| 7 | Verified every published tool still appears in at least one lab, and the lab register still totals 79 |

## 4. Live session map

| L | Wk | Module | Live session | Published topics | Hours replaced | Labs | Project gate |
|---|---|---|---|---|---|---|---|
| 01 | 1 | M1 | Security Foundations & Windows Internals | M1.1, M1.2a | 12 | 5 | — |
| 02 | 1 | M1 | Linux Fundamentals & Scripting for Security Ops | M1.2b, M1.4 | 12 | 5 | — |
| 03 | 2 | M1 | Networking Fundamentals & Protocol Analysis | M1.3 | 8 | 5 | — |
| 04 | 2 | M1 | Active Directory & Authentication | M1.5 | 8 | 4 | — |
| 05 | 3 | M1 | Log Analysis + Web Technologies & Attack Awareness | M1.6, M1.7 | 16 | 5 | P1 kickoff |
| 06 | 3 | M2 | SOC Operations, Alert Triage & Incident Handling | M2.1 | 8 | 4 | P1 review |
| 07 | 4 | M2 | Log Analysis & Event Correlation | M2.2 | 8 | 3 | — |
| 08 | 4 | M2 | Splunk Investigation & Detection Development | M2.3 | 8 | 4 | — |
| 09 | 5 | M2 | Wazuh Deployment, Monitoring & Detection | M2.4 | 8 | 4 | P2 kickoff |
| 10 | 5 | M2/M3 | Sigma, Cross-SIEM Rules & Detection Engineering Fundamentals | M2.5, M3.1 | 12 | 5 | P2 review |
| 11 | 6 | M3 | Endpoint & Active Directory Attacks and Detection | M3.2, M3.3 | 8 | 4 | — |
| 12 | 6 | M3 | Network & Web Attacks and Detection | M3.4, M3.5 | 8 | 4 | — |
| 13 | 7 | M3 | Detection Use Cases, Correlation & Alert Tuning | M3.6, M3.7 | 8 | 4 | P3 kickoff |
| 14 | 7 | M4 | Threat Hunting Methodology, ATT&CK & Hunting Practice | M4.1, M4.2, M4.3 | 12 | 6 | P3 review |
| 15 | 8 | M4 | IOC Hunting, Threat Intelligence & Enrichment | M4.4, M4.5 | 8 | 4 | P4 kickoff |
| 16 | 8 | M5 | Incident Response Lifecycle, Triage & Live Response | M5.1, M5.2, M5.3 | 12 | 5 | P4 review |
| 17 | 9 | M5 | Memory Forensics & Windows Forensic Artifacts | M5.4, M5.5 | 8 | 5 | P5 kickoff |
| 18 | 9 | M6 | Malware Triage — Static, Dynamic & IOC Extraction | M6.1, M6.2 | 8 | 3 | P5 review · P6 final |
| | | | **Total** | **35 topics** | **176 + 16 project h** | **79** | **6** |

## 5. Dependency edges — never break in a re-sequence

- L05 log analysis ← L01 Windows internals + L02 Linux + L04 AD (4624/4625/4768/4769 need NTLM and Kerberos first)
- L07 correlation ← L05
- L08 Splunk and L09 Wazuh ← L07
- L10 Sigma ← L08 + L09 (a rule needs both back ends to convert to)
- L11–L12 attack detection ← L10 (detection logic before attack catalogue)
- L13 tuning ← L11 + L12 (you cannot tune rules you have not written)
- L14 hunting ← L08 + L09 + L13
- L16 IR ← L06 (triage) ; L17 forensics ← L16 (evidence preservation)
- L18 malware triage ← L17 (memory artefacts) and L15 (IOC extraction)
- P6 introduces **no new technique**

## 6. Density risks

| Risk | Where | Mitigation |
|---|---|---|
| Heaviest compression (12 published h → 6 live h) | L01, L02, L05, L10, L14, L16 | Mandatory pre-reading; three tight blocks instead of two; largest self-study packs |
| M1 drops 64 h → 30 h | Whole of M1 | Only foundation content later sessions depend on stays in class; the rest is SSP-01…SSP-05 |
| Students arriving with no IT background | L01–L03 | Setup pack + "day zero" primer published before week 1 |
| Tool install eating class time | L08, L09, L17, L18 | Pre-built VM image and snapshots; installs never demonstrated live |
| Project pile-up in weeks 7–9 | P3, P4, P5 | Each project is scoped to one evening of work and reviewed in the next session |

## 7. Coverage proof

- 35 / 35 published topic lines mapped, each exactly once.
- 79 / 79 labs registered in `lab_register.md`.
- 48 published practical tasks → 18 task packs; mapping in `self_study_register.md`.
- 6 / 6 projects with a live kickoff and a live review.
- Every published tool appears in at least one lab — checked in `topic_map.md` column *Tools*.
