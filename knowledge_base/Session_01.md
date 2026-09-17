# Session 01 — Security Foundations & Windows Internals

> Condensed intake note (not a copy of the decks). Owner: `dgs-intake`. Feeds Step 5 build of L01.
> Live session L01 · Module 1 · Topics **M1.1** (Computer, OS & Security Fundamentals) + **M1.2a** (Windows Internals).
> Labs: LAB-L01-A/B (LIVE) · C/D (TASK) · E (SELF). Project: none (P1 kicks off at L05).

## Sources used (extracted → `Resources/extract/L01/`)

| Slug | Source | Size | Use |
|---|---|---|---|
| `introduction-to-cyber-security` | SOC-4M · Introduction to Cyber Security.pptx | 89 sl | **Primary** for M1.1 — CIA, terminology, malware, hackers, real attacks, SOC |
| `intro-to-cybersecuirty` | DEF · Intro To CyberSecuirty.pptx (Cisco Ch.1) | 48 sl | CIA reinforcement, hashing/integrity, cyberwarfare, quiz bank |
| `windows` | SOC-4M · Windows.pdf | 87 p | **Primary** for M1.2a — GUI, FS, System32, accounts, UAC, admin tools, Blue-Team tools, Event IDs |
| `chapter-3` | DEF · CyberOps Ch.3 Windows OS | 92 sl | Windows **architecture** — HAL, user/kernel mode, NTFS+ADS, boot, processes/threads/services, handles, registry, WMI, `net` |
| `chapter-1` | DEF · CyberOps Ch.1 The Danger | 30 sl | Opener war-stories (rogue AP, ransomed companies, targeted nations) |
| `process-explorer` | DEF · Process Explorer.pptx | 24 sl | **Lab B** tool — process tree, columns, suspicious-process workflow |
| `autoruns` | DEF · Autoruns.pptx | 21 sl | **Lab C** tool — persistence locations, unsigned/red highlighting |
| `tcpview` | DEF · TCPView.pptx | 22 sl | Endpoint network view — reverse-shell/C2 spotting (demo aid) |
| `virtual-machines` | DEF · Virtual Machines.pptx | 23 sl | **Setup pack** — Type 1/2, VMware, VT-x, adapter modes |
| `windows-labs` | SOC-4M · Windows_Labs_.pdf | 5 p | Attack-chain seed (msfvenom→UAC bypass) — **teach detection side only** |
| `windows-10`, `kali-linux-install-steps` | DEF · setup decks | thin | Setup pack images only |

## Teaching order (8-part in-class; other 4 parts → student pack)

**Block A — M1.1 Security Foundations (Teach A + Guided Lab A)**
1. WHY — WannaCry (2017, 300k+ hosts, NHS) & Equifax (147M records, unpatched Apache Struts) → both preventable, both hit a different CIA pillar.
2. Definition + analogy — security = protecting data/systems; CIA triad via the **bank-account analogy** (private balance / correct balance / ATM available).
3. How it works — C·I·A each with control methods (encryption/ACL/MFA · hashing/checksums/version control · redundancy/backup/DR).
4. Attacker view — terminology chain **Vulnerability → Threat → Exploit → Risk** (house-lock analogy); malware families (virus, worm, trojan, RAT, keylogger, ransomware, adware) mapped to real cases; hacker types (hat colors, skill, motivation).
5. What the SOC sees — map each malware/attack to the CIA pillar it breaks + which analyst tool surfaces it; introduce the SOC as the 24/7 control room protecting CIA.
6. Guided Lab A → **LAB-L01-A** (VM + snapshot + `10.10.10.0/24` connectivity check).
7. Takeaways.
8. Task handout.

**Block B — M1.2a Windows Internals (Teach B + Independent Lab B)**
1. WHY — Windows dominates enterprise → primary target; analyst must know normal vs. abnormal to triage endpoint alerts.
2. Definition + analogy — OS as manager of hardware/users/apps; architecture layers.
3. How it works — **architecture** (HAL, user vs kernel mode, NTFS + Alternate Data Streams, boot/startup, processes→threads→services, handles, **Registry hives** HKLM/HKCU); **GUI/FS** (System32, drive letters, extensions, AppData/Temp); **accounts** (Admin/Standard/Service/Domain, NTFS perms, ACL, groups/inheritance); **UAC** (consent vs credential prompt, elevation).
4. Attacker view — masquerading (`svch0st.exe`), fake extension (`invoice.pdf.exe`), persistence via Run keys / Startup / Scheduled Tasks / Services, abnormal parent→child (`winword.exe → powershell.exe`).
5. What the SOC sees — Security-log **Event IDs** + tools (below); Process Explorer tree, Autoruns persistence, TCPView connections.
6. Independent Lab B → **LAB-L01-B** (process & service inspection, normal vs suspicious, Process Explorer).
7. Takeaways.
8. Task handout (Labs C + D).

## Attack ↔ Detection ↔ MITRE (R9 — every attack paired)

| Attack behaviour (from decks) | What the SOC sees / detection | MITRE |
|---|---|---|
| Malicious macro spawns PowerShell | `winword.exe → powershell.exe` tree in Process Explorer; Event ID **4688** w/ Base64 cmdline | T1059.001 / T1566.001 |
| Persistence via Run key / Startup / Scheduled Task | Autoruns Logon/Tasks tab; unsigned entry from AppData\Temp | T1547.001 / T1053.005 |
| New backdoor admin account | Event ID **4720** (created) + **4672** (privileged logon) | T1136.001 / T1078 |
| Service masquerading / new service | Event ID **7045** (service installed); unsigned binary in System32 | T1543.003 / T1036.005 |
| Reverse shell / C2 beacon | TCPView: `cmd.exe`/`powershell.exe` → external IP:4444; Sysmon Event ID 3 | T1071 / T1571 |
| UAC bypass / privilege escalation | Event ID **4688** elevated flag + **4624/4672** | T1548.002 / T1068 |
| Ransomware wipes shadow copies | `vssadmin delete shadows` in PowerShell history | T1490 |

Key Event IDs to memorize: **4624** logon · **4625** failed logon · **4672** privileged logon · **4688** process creation · **4720** account created · **7045** service installed.

## Diagram ideas (inline SVG — draw, don't screenshot)
- **CIA triad triangle** with the bank analogy on each edge.
- **Vulnerability → Threat → Exploit → Risk** flow (house-lock icons → computer icons).
- **Windows architecture stack** — hardware → HAL → kernel mode → user mode → apps.
- **Normal vs malicious process tree** side-by-side (`explorer→winword` vs `winword→powershell→cmd`).
- **Persistence map** — Windows box with 6 pins (Run key, Startup folder, Scheduled Task, Service, Driver, DLL) → "Autoruns sees all of these."
- **Attack chain → Event ID timeline** — initial access → exec → privesc → persistence, each stamped with its Event ID.
- **Type 1 vs Type 2 hypervisor** (setup pack).

## Screenshots worth reusing (own lab, not deck images)
Capture fresh on `DGS-WS01`: Process Explorer tree with a benign parent/child; Autoruns Logon tab with unsigned filter on; TCPView with an established connection; Event Viewer Security log showing 4624/4688; `whoami /priv` output; UAC consent prompt.

## Log / evidence samples (real, from lab — R10)
Generate on `DGS-WS01`: 4688 process-creation line for a PowerShell launch; 4625 failed-logon burst; 4720 account-creation event. No invented log lines — pull from the actual lab Security log.

## Lab seeds
- **LAB-L01-A** (LIVE) — VMware: import base image, take `BASE`/`CLEAN-TOOLS` snapshots, verify `10.10.10.0/24` host-only connectivity. Setup pack (VM deck) is prerequisite, done **before** class (C4).
- **LAB-L01-B** (LIVE) — Process Explorer + Task Manager: identify normal vs suspicious process (path, publisher, cmdline, parent). Use the PE "investigate a suspicious process" workflow.
- **LAB-L01-C** (TASK) — Registry autorun keys walkthrough with Autoruns; find a planted persistence entry.
- **LAB-L01-D** (TASK) — Accounts, privileges, UAC on DGS-WS01 (`net user`, `whoami /priv`, UAC levels).
- **LAB-L01-E** (SELF) — CIA-triad & control-mapping worksheet.

## THM rooms (free-tier — verify before linking, R12)
Windows Fundamentals 1 / 2 / 3 · Intro to Offensive/Defensive Security (Intro to Cyber path) · Careers in Cyber. (Assign as self-study, not in class.)

## What to CUT / move (C1, C2, C3)
- **Offensive payload mechanics** (msfvenom, Metasploit handler, Juicy Potato/PrintSpoofer, mimikatz LSASS dump, full privesc vectors from Windows.pdf pp.59–85, windows-labs.pdf) → keep only the **detection** framing here; deep offensive AD/endpoint attacks belong to **L11 (M3.2/M3.3)**.
- BitLocker / VSS deep dive, Windows editions comparison, Cisco Ch.1 planning-guide slides → **SSP-01** self-study (6 h: hardware/boot theory, virtualization theory, security governance, CIA/AAA worksheet).
- Cyberwarfare/Stuxnet, full malware case-study catalogue → student pack case-study section (framework part 5), not lectured.
- Overlapping CIA content between the two intro decks → teach once from the SOC-4M deck; Cisco deck used only for hashing/integrity detail + quiz bank.

## Open dependency notes for Step 5
- Event IDs introduced here are the anchor for L05 (log analysis) and L07 (correlation) — teach-once (C1).
- AD accounts/Kerberos deferred to **L04**; this session covers **local** accounts only.
