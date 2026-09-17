# Source Inventory — What feeds each DGS session

> Owner skill: `dgs-intake`. Built 2026-09-17 from a full scan of the two source trees. Page/slide counts are real.
> Raw extractions land in `Resources/extract/<session>/` (gitignored); condensed notes go to `knowledge_base/Session_NN_*.md`.

## Source trees

| Tag | Path | Files | Teaching docs |
|---|---|---|---|
| `SOC-4M` | `E:\Work\ADA Egypt\Cyber Security\Soc Analysis Diploma - 4 Months` | 236 | 8 modules across 4 months, HTML interactive lectures, pcap labs |
| `DEF` | `E:\Work\ADA Egypt\Cyber Security\Cyber secuirty Diplom\Definsife` | 353 | Cisco CyberOps 18 chapters, Security+ 21 chapters, Cisco NetSec, tools decks, tasks, projects |
| `WEB` | TryHackMe rooms (free tier only, verified at extraction time — R12) | — | Labs and the "student practice" source |
| `OWN` | `github.com/Ebrahim-Qareen` — Wazuh-SIEM-Integration, Network-Attack-Simulation-Lab, ecdfp-diploma | — | Instructor's own labs, reused as-is |

Where the same deck exists as `.pptx` and `.pdf`, extract the **pptx** (text + speaker notes + images) and use the pdf only for page-level screenshots.

## Priority rules for extraction

1. **Interactive HTML lectures first** — they already carry the diagram ideas (`web_attacks_lecture.html`, `digital_forensics_lecture.html`, `phishing_guide.html`, `ckc_part0–4`, the Wi-Fi steppers).
2. Then the instructor's own decks (SOC-4M and DEF `Matrial/`) — these hold the teaching order he already uses.
3. Then vendor material (Cisco CyberOps chapters, Security+ chapters) only to fill gaps and check coverage — never copied.
4. Tasks, projects and pcaps are lab and project seeds, extracted last.

---

## Session map

### L01 — Security Foundations & Windows Internals  (M1.1, M1.2a)

| Source | File | Size |
|---|---|---|
| SOC-4M | `First Month/Intro to Cyber secuirty/Matrial/Introduction to Cyber Security.pptx` | 89 slides |
| SOC-4M | `First Month/Intro to Cyber secuirty/Matrial/intro-to-cybersecurity.html` | 61 KB |
| SOC-4M | `First Month/Opreating System/Matrial/Windows.pdf` | 86 p |
| SOC-4M | `First Month/Opreating System/Lab/Windows Lab/Windows_Labs_.pdf` | 4 p — lab seed |
| DEF | `Intro to cybersecurity/Intro To CyberSecuirty.pptx` | 48 slides |
| DEF | `Tools/Matrial/Virtual Machines.pptx` · `Process Explorer.pptx` · `Autoruns.pptx` · `TCPView.pptx` | 23 · 24 · 21 · 22 |
| DEF | `Tools/Tool/Windows 10 .pptx` · `CyberOps/install/Kali Linux Install Steps.pptx` | setup pack |
| DEF | `CyberOps/Matrial/Chapter 1.pptx` (The Danger) · `Chapter 3.pptx` (Windows OS) | 30 · 92 |
| WEB | THM: *Windows Fundamentals 1, 2, 3* · *Intro to Cyber Security* path · *Careers in Cyber* | labs |

### L02 — Linux Fundamentals & Scripting for Security Ops  (M1.2b, M1.4)

| Source | File | Size |
|---|---|---|
| SOC-4M | `First Month/Opreating System/Matrial/Linux Opreating System Fundamentals .pdf` | 105 p |
| DEF | `Tools/Tool/Ubuntu.pptx` · `Tools/Tool/Kali linux.pptx` | 4 · 4 |
| DEF | `CyberOps/Sites/Linux_Shell.pdf` | 4 p |
| DEF | `CyberOps/Matrial/Chapter 4.pptx` (Linux Overview) | 82 |
| DEF | `Tools/Matrial/OSQuery.pptx` | 21 |
| WEB | THM: *Linux Fundamentals 1, 2, 3* · *Windows PowerShell* · *Bash Scripting* · *Python Basics* | labs |

### L03 — Networking Fundamentals & Protocol Analysis  (M1.3)

| Source | File | Size |
|---|---|---|
| SOC-4M | `Second Month/Intro to Network/Introduction to Computer Networks.pdf` | 62 p |
| SOC-4M | `Second Month/Introduction to OSI Model/Introduction to OSI Model.pdf` | 31 p |
| SOC-4M | `Second Month/OSI Model Journey/Matrial/OSI Model Journey.pptx` | 58 |
| SOC-4M | `Second Month/Layer 2  (Data Link Layer)/Matrial/Layer 2  (Data Link Layer).pptx` | 85 |
| SOC-4M | `Second Month/Layer 3 (Network Layer)/Matrial/Layer 3 (Network Layer).pptx` | 134 |
| SOC-4M | `Second Month/Layer 4 ( Transport Layer )/Matrial/Layer 4 (Transport Layer).pptx` | 105 |
| SOC-4M | `Second Month/Layer 7 ( Application )/Matrial/Layer 7 (Application Layer).pptx` | 33 |
| SOC-4M | `Second Month/Layer 4 ( Transport Layer )/Task/Netwrok.pcapng` · `123.pcap` | lab seeds |
| SOC-4M | `Second Month/Tools/Matrial/WireShark.pptx` | 64 |
| DEF | `Protocols/Doc/Protocols.pdf` | 69 p |
| DEF | `Networking/Power Point/OSI Model Full.pptx` | 168 — reference only |
| WEB | THM: *Networking Concepts* · *Networking Essentials* · *Networking Core Protocols* · *Wireshark: The Basics* · *Packets & Frames* | labs |

Layers 1, 5, 6 (53 + 31 + 52 pages) go to the self-study pack, not the class.

### L04 — Active Directory & Authentication  (M1.5)

| Source | File | Size |
|---|---|---|
| SOC-4M | `First Month/Opreating System/Matrial/Active Directory Fundamentals.pdf` | 229 p — the main source |
| DEF | `Network Security/Matrial/ComTIA Security+/07- Implementing Authentication Controls.pdf` · `08- Identity and Account Management.pdf` | 49 · 31 |
| WEB | THM: *Active Directory Basics* · *Windows Fundamentals 2* (AD parts) | labs |

### L05 — Log Analysis, Web Technologies & Attack Awareness  (M1.6, M1.7)

| Source | File | Size |
|---|---|---|
| DEF | `CyberOps/Matrial/Logs/Logs.pptx` | 39 |
| DEF | `CyberOps/Matrial/Logs/Lab Log Universe/Log_Universe.pdf` | 36 p — lab seed |
| SOC-4M | `web_attacks_lecture.html` | 206 KB — interactive, diagram ideas |
| SOC-4M | `phishing_guide.html` | 76 KB |
| DEF | `CyberOps/Matrial/Chapter 5.pptx` (Network Protocols) · `Chapter 10.pptx` (Network Services) | 59 · 57 |
| WEB | THM: *Windows Event Logs* · *Intro to Logs* · *Web Application Basics* · *OWASP Top 10* · *HTTP in Detail* | labs |
| P1 seed | DEF `Intro to cybersecurity/Project/` · SOC-4M `First Month/Opreating System/Project/` | project briefs |

### L06 — SOC Operations, Alert Triage & Incident Handling  (M2.1)

| Source | File | Size |
|---|---|---|
| DEF | `Security Controls/Matrial/Blue Team Report.pptx` | 77 |
| DEF | `Security Controls/Matrial/Preparation for Security control.pptx` | 45 |
| DEF | `Network Security/Matrial/Comparing Security Roles and Security Controls.pptx` | 35 |
| DEF | `CyberOps/Matrial/Chapter 2.pptx` (Fighters in the War Against Cybercrime — SOC roles) | 31 |
| SOC-4M | `Webinar/WebinarFile-SOC Analysis-G012.pdf` | 13 p |
| SOC-4M | `SOC.Analysis-Diploma2025-2026.pdf` | 24 p — program framing |
| WEB | THM: *Junior Security Analyst Intro* · *Security Operations* · *TheHive Project* · *Phishing Analysis Fundamentals* | labs |

### L07 — Log Analysis & Event Correlation  (M2.2)

| Source | File | Size |
|---|---|---|
| DEF | `Tools/Matrial/Sysmon.pptx` | 20 |
| DEF | `CyberOps/Matrial/Incident Response Lifecycle & Event IDs/…pptx` (Event IDs half) | 63 |
| DEF | `CyberOps/Matrial/Chapter 11.pptx` (Network Security Data) · `Chapter 12.pptx` (Evaluating Alerts) | 58 · 56 |
| WEB | THM: *Sysmon* · *Windows Event Logs* · *Log Analysis / Intro to Log Analysis* · *Investigating Windows* | labs |

### L08 — Splunk Investigation & Detection Development  (M2.3)

| Source | File | Size |
|---|---|---|
| DEF | `Security Controls/Matrial/SIEM (Security Information and Event Management).pptx` (Splunk half) | 107 |
| DEF | `Security Controls/Task/Splunk Exploring Lab.pptx` · `Splunk 3.pptx` · `Project/Splunk Certificate.pptx` | 5 · 5 · 8 |
| WEB | THM: *Splunk: Basics* · *Splunk: Exploring SPL* · *Investigating with Splunk* · *Benign* · Splunk BOTS v1/v3 | labs |

### L09 — Wazuh Deployment, Monitoring & Detection  (M2.4)

| Source | File | Size |
|---|---|---|
| DEF | `Security Controls/Matrial/SIEM (...).pptx` (Wazuh half) | — |
| OWN | `Wazuh-SIEM-Integration` repo — Sysmon, FIM + VirusTotal, Suricata, active response, DVWA rules | instructor labs |
| WEB | THM: *Wazuh* · *Intro to SIEM* | labs |
| P2 seed | DEF `CyberOps/Task/Task 4–6` (alert investigation tasks) | tasks |

### L10 — Sigma, Cross-SIEM Rules & Detection Engineering Fundamentals  (M2.5, M3.1)

| Source | File | Size |
|---|---|---|
| OWN | `Wazuh-SIEM-Integration` custom PCRE2 rules mapped to ATT&CK · CyberTalents/SimulationLabs rule work (structure only, no client data) | rules |
| DEF | `Security Controls/Matrial/SOAR (...).pptx` (automation context) | 65 |
| WEB | THM: *Sigma* · *Intro to Detection Engineering* · *Detection Engineering* path · *YARA* | labs |

### L11 — Endpoint & Active Directory Attacks and Detection  (M3.2, M3.3)

| Source | File | Size |
|---|---|---|
| DEF | `CyberOps/Matrial/Attacks/Attack Lab.pptx` | 17 |
| SOC-4M | `First Month/Opreating System/Lab/DLL Hijacking.rar` | 65 MB — lab seed |
| DEF | `CyberOps/Matrial/Chapter 14.pptx` (Common Threats and Attacks) · `Chapter 15.pptx` (Network Attacks) | 57 · 31 |
| DEF | `Network Security/Matrial/ComTIA Security+/04- Social Engineering and Malware.pdf` | 43 p |
| WEB | THM: *Atomic Red Team* · *Windows Attacks & Defense* (free parts) · *Attacktive Directory* (awareness only) · *Kerberoasting* concept via *Attacking Kerberos* | labs |

### L12 — Network & Web Attacks and Detection  (M3.4, M3.5)

| Source | File | Size |
|---|---|---|
| DEF | `Tools/Tasks/Team Task – MiTM (ARP Spoofing Poisoning) Attack.pptx` · `DNS Spoofing Attack.pptx` · `DoS Attack Simulation.pptx` | 6 · 6 · 6 |
| DEF | `Security Controls/Task/DNS Spoofing … pfSense & Snort.pptx` · `Detecting and Blocking DoS … pfSense Firewall and Snort IDS.pptx` | 7 · 7 |
| SOC-4M | `Thierd Month/Second Month ( Security Control )/Project/` — MiTM, DNS spoofing, DoS: attack + detection + response | 12 · 12 · 12 |
| SOC-4M | `Thierd Month/…/IDS&IPS/Matrial/IDS & IPS.pptx` · `Firewall/Matrial/Firewall.pptx` (detection side) | 84 · 108 |
| SOC-4M | `Second Month/Tools/Labs/` — CyberDefenders pcaps: *TomcatTakeover* · *WebInvestigation* · *DanaBot* · *psexec-hunt* | 4 pcaps |
| SOC-4M | `web_attacks_lecture.html` (attack side) | — |
| OWN | `Network-Attack-Simulation-Lab` — 8 scenarios with Snort rules mapped to ATT&CK | instructor labs |
| WEB | THM: *Nmap* · *Snort* · *Snort Challenge* · *Web Attacks / SQL Injection Lab* · *Wireshark: Traffic Analysis* | labs |

### L13 — Detection Use Cases, Correlation & Alert Tuning  (M3.6, M3.7)

| Source | File | Size |
|---|---|---|
| DEF | `Security Controls/Matrial/NDR, EDR, and XDR.pptx` · `IDS & IPS.pptx` (tuning parts) | 59 · 50 |
| DEF | `CyberOps/Matrial/Chapter 12.pptx` (Evaluating Alerts — TP/FP/TN/FN) | 56 |
| OWN | Detection-engineering field notes — rule conflicts, FP reduction | notes |
| WEB | THM: *Intro to SIEM* (use cases) · *Splunk: Dashboards and Reports* · *Wazuh* (rule tuning) | labs |
| P3 seed | Five detections across both SIEMs — brief to be written | — |

### L14 — Threat Hunting Methodology, ATT&CK & Hunting Practice  (M4.1, M4.2, M4.3)

| Source | File | Size |
|---|---|---|
| SOC-4M | `Fourth Month/Cyber Threat Intelligence (C.T.I)/Matrial/ckc_part0_story.html` … `ckc_part4_other_projects.html` | 5 interactive pages — kill chain, ATT&CK, CAR, D3FEND |
| OWN | ADA lecture series — Threat Intelligence / MITRE ATT&CK track | HTML lectures |
| DEF | `CyberOps/Matrial/Chapter 13.pptx` (Attackers and Their Tools) | 36 |
| WEB | THM: *Cyber Kill Chain* · *Unified Kill Chain* · *Pyramid of Pain* · *MITRE* · *Threat Hunting: Introduction / Foothold / Pivoting* · *Hunt Me I* | labs |

### L15 — IOC Hunting, Threat Intelligence & Enrichment  (M4.4, M4.5)

| Source | File | Size |
|---|---|---|
| SOC-4M | `Fourth Month/Cyber Threat Intelligence (C.T.I)/Matrial/Cyber Threat Intelligence (C.T.I).pptx` | 124 — the main source |
| DEF | `Network Security/Matrial/Explaining Threat Actors and Threat Intelligence.pptx` | 30 |
| SOC-4M | `phishing_guide.html` (email IOC extraction) · `Thierd Month/…/Email Security/Matrial/Email Security.pptx` | 76 KB · 105 |
| WEB | THM: *Intro to Cyber Threat Intel* · *Threat Intelligence Tools* · *MISP* · *OpenCTI* · *Phishing Emails 1–3* | labs |
| P4 seed | Hunt from a published threat report — brief to be written | — |

### L16 — Incident Response Lifecycle, Triage & Live Response  (M5.1, M5.2, M5.3)

| Source | File | Size |
|---|---|---|
| DEF | `CyberOps/Matrial/Incident Response Lifecycle & Event IDs/…pptx` (IR half) | 63 |
| DEF | `Network Security/Matrial/ComTIA Security+/17- Performing Incident Response.pdf` | 41 p |
| DEF | `CyberOps/Matrial/Chapter 16.pptx` (Digital Forensics and IR Analysis) | 43 |
| DEF | `Final Project/Final project Blue Team.pptx` | 21 — P6 seed |
| DEF | `Security Controls/Matrial/SOAR (...).pptx` (response automation) | 65 |
| WEB | THM: *Incident Response Process* · *Preparation* · *Identification & Scoping* · *Threat Intel & Containment* · *Eradication & Remediation* · *Lessons Learned* | labs |

### L17 — Memory Forensics & Windows Forensic Artifacts  (M5.4, M5.5)

| Source | File | Size |
|---|---|---|
| SOC-4M | `digital_forensics_lecture.html` | 70 KB — interactive |
| DEF | `Network Security/Matrial/ComTIA Security+/18- Explaining Digital Forensics.pdf` | 10 p |
| OWN | `ecdfp-diploma` — memory and Windows artefact pages, reused at analyst depth | site |
| WEB | THM: *Intro to Digital Forensics* · *Windows Forensics 1 & 2* · *Volatility* · *Autopsy* · *Memory Forensics* | labs |
| P5 seed | One incident from first alert to lessons learned — brief to be written | — |

### L18 — Malware Triage — Static, Dynamic & IOC Extraction  (M6.1, M6.2)

| Source | File | Size |
|---|---|---|
| DEF | `Network Security/Matrial/ComTIA Security+/04- Identifying Social Engineering and Malware.pdf` (malware types) | 43 p |
| DEF | `CyberOps/Matrial/Chapter 14.pptx` (malware section) | — |
| WEB | THM: *Intro to Malware Analysis* · *Basic Static Analysis* · *Basic Dynamic Analysis* · *MalBuster* · *Dunkle Materie* (challenge) | labs |
| P6 seed | DEF `Final Project/Final project Blue Team.pptx` · SOC-4M `Second Month/Network Forensics CTF Project/` pcaps | project |

---

## Not used (and why)

| Source | Reason |
|---|---|
| DEF `Matrial/الشبكة.pptx` (362 slides, Arabic networking) | Duplicates L03 sources; Arabic — material language is English |
| DEF `Cybersecurity Architecture/`, `Security Controls/Governance & Regulation`, Security+ 19–21 | GRC / architecture — out of the Blue Team scope |
| SOC-4M `Wi-Fi Security/`, `VPN/` | Not in the published 35 topics |
| DEF `Network Security/Matrial/Cisco CybSec/` Network Security v1.0 modules | Firewall/VPN engineering depth — beyond analyst scope; kept as reference only |
| SOC-4M `Thierd Month/…/Firewall/Tool/the-pfsense-documentation.pdf` (2,472 p) | Vendor manual — link, never extract |
| Attendance / performance sheets, Discord, Egyptian law PDF | Admin, not curriculum |

## Load estimate per session (raw source pages that must be condensed)

| L | Main decks (slides/pages) | Interactive HTML | Verdict |
|---|---|---|---|
| 01 | 89 + 86 + 48 + 90 (tools) | 1 | Heavy — pre-reading mandatory |
| 02 | 105 + 82 + 21 | — | Medium |
| 03 | 62 + 31 + 58 + 85 + 134 + 105 + 33 + 64 + 69 | — | **Heaviest** — layers 1/5/6 already moved out; L2–L4 must be cut to what a SOC analyst reads in a packet |
| 04 | 229 + 80 | — | Heavy — one source, deep; cut to auth flows + Event IDs |
| 05 | 39 + 36 + 116 | 2 | Medium — the HTML lectures carry it |
| 06 | 77 + 45 + 35 + 31 + 13 | — | Medium |
| 07 | 20 + 63 + 114 | — | Medium |
| 08 | 107 (half) + 18 | — | Light — lab-driven |
| 09 | 107 (half) + own repo | — | Light — lab-driven |
| 10 | 65 + own rules | — | Light — lab-driven |
| 11 | 17 + 88 + 43 + rar lab | — | Medium |
| 12 | 18 + 14 + 36 + 192 + own repo + 4 pcaps | 1 | Heavy — but mostly labs already built |
| 13 | 109 + 56 | — | Medium |
| 14 | 36 + own lecture series | 5 | Medium — HTML carries it |
| 15 | 124 + 30 + 105 | 1 | Heavy — CTI deck is the spine |
| 16 | 63 + 41 + 43 + 21 + 65 | — | Medium |
| 17 | 10 + own eCDFP pages | 1 | Light — reuse |
| 18 | 43 (part) + THM | — | Light — THM-driven |
