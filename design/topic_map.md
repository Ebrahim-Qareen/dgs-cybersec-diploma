# Topic Map — Topic → Live Session → Labs → Tools

> Owner skill: `dgs-design`. A concept is taught in exactly one session. Later sessions reference, never re-teach.

| Topic ID | Published topic | Module | Live session | Labs | Tools | Taught-once anchor |
|---|---|---|---|---|---|---|
| M1.1 | Computer, Operating Systems & Security Fundamentals | 1 | L01 | LAB-L01-A/B/C | VMware, Windows, CIA triad worksheet | Security concepts, OS architecture |
| M1.2a | Windows Internals | 1 | L01 | LAB-L01-D/E | Process Explorer, Task Manager, Registry Editor | Processes, services, registry |
| M1.2b | Linux Fundamentals | 1 | L02 | LAB-L02-A/B | bash, systemd, journalctl | Linux FS, users, permissions |
| M1.4 | PowerShell & Bash for Security Operations | 1 | L02 | LAB-L02-C/D/E | PowerShell, bash | Scripting for analysts |
| M1.3 | Networking Fundamentals & Protocol Analysis | 1 | L03 | LAB-L03-A…E | Wireshark, ipcalc, tcpdump | OSI, TCP/IP, DNS/HTTP/SMB on the wire |
| M1.5 | Active Directory & Authentication Fundamentals | 1 | L04 | LAB-L04-A…D | AD DS, ADUC, klist | NTLM, Kerberos, LDAP |
| M1.6 | Windows, Linux & Web Log Analysis | 1 | L05 | LAB-L05-A/B/C | Event Viewer, journalctl, Apache logs | Event IDs, log formats |
| M1.7 | Web Technologies & Common Attack Awareness | 1 | L05 | LAB-L05-D/E | Browser dev tools, DVWA | HTTP, OWASP awareness |
| M1.8 | Foundation Investigation & Capstone | 1 | P1 (L05 → L06) | — | All M1 tools | — |
| M2.1 | SOC Operations, Alert Triage & Incident Handling | 2 | L06 | LAB-L06-A…D | TheHive | Triage workflow, TP/FP, severity |
| M2.2 | Log Analysis & Event Correlation | 2 | L07 | LAB-L07-A/B/C | Event Viewer, Sysmon, grep/awk | Correlation across sources |
| M2.3 | Splunk Investigation & Detection Development | 2 | L08 | LAB-L08-A…D | Splunk Free, SPL, BOTS dataset | SPL search language |
| M2.4 | Wazuh Deployment, Monitoring & Detection | 2 | L09 | LAB-L09-A…D | Wazuh, decoders, rules | Agent → decoder → rule → alert |
| M2.5 | Sigma Rules & Cross-SIEM Detection Engineering | 2 | L10 | LAB-L10-A/B/C | Sigma, sigma-cli | Sigma syntax and conversion |
| M3.1 | Detection Engineering Fundamentals | 3 | L10 | LAB-L10-D/E | Sigma, ATT&CK | Detection lifecycle, logic quality |
| M3.2 | Endpoint Attacks & Detection Techniques | 3 | L11 | LAB-L11-A/B | Atomic Red Team, Sysmon, Wazuh | Execution, persistence, defence evasion |
| M3.3 | Active Directory Attacks & Detection | 3 | L11 | LAB-L11-C/D | Kerberoast simulation, Event IDs 4768/4769 | Credential access, lateral movement |
| M3.4 | Network Attacks & Detection Techniques | 3 | L12 | LAB-L12-A/B | Nmap, Wireshark, Suricata alerts | Scanning, MITM, exfil patterns |
| M3.5 | Web Attacks & Detection Techniques | 3 | L12 | LAB-L12-C/D | DVWA, Apache logs, Wazuh web rules | SQLi, XSS, path traversal in logs |
| M3.6 | Detection Use Cases & Correlation Logic | 3 | L13 | LAB-L13-A/B | Wazuh, Splunk | Use-case documentation format |
| M3.7 | Alert Tuning & False Positive Reduction | 3 | L13 | LAB-L13-C/D | Wazuh rule tuning, Splunk lookups | Tuning method and evidence |
| M3.8 | Detection Development Project | 3 | P3 (L13 → L14) | — | Sigma, Splunk, Wazuh | — |
| M4.1 | Threat Hunting Methodology | 4 | L14 | LAB-L14-A | Hunt template | Hypothesis-driven hunting |
| M4.2 | MITRE ATT&CK & Adversary Behaviors | 4 | L14 | LAB-L14-B/C | ATT&CK Navigator, D3FEND | Tactic/technique model, Pyramid of Pain |
| M4.3 | Endpoint, Network & Log-Based Hunting | 4 | L14 | LAB-L14-D/E/F | Splunk, Wazuh, Sysmon | Hunt queries per data source |
| M4.4 | IOC Hunting & Threat Intelligence | 4 | L15 | LAB-L15-A/B | VirusTotal, OTX | IOC types and lifecycle |
| M4.5 | Threat Intelligence Platforms & Enrichment | 4 | L15 | LAB-L15-C/D | MISP, TheHive enrichment | Feeds, sharing, enrichment |
| M4.6 | Threat Hunting Investigation Project | 4 | P4 (L15 → L16) | — | All M4 tools | — |
| M5.1 | Incident Response Lifecycle | 5 | L16 | LAB-L16-A | NIST SP 800-61 playbook template | IR phases |
| M5.2 | Triage, Scoping & Containment | 5 | L16 | LAB-L16-B/C | TheHive, Wazuh active response | Scoping method |
| M5.3 | Live Response & Evidence Collection | 5 | L16 | LAB-L16-D/E | KAPE-style collection scripts, PowerShell | Order of volatility |
| M5.4 | Memory Forensics | 5 | L17 | LAB-L17-A/B/C | Volatility 3 | Memory artefact analysis |
| M5.5 | Windows Forensic Artifacts Analysis | 5 | L17 | LAB-L17-D/E | Autopsy, registry hives, prefetch | Artefact catalogue and timeline |
| M5.6 | Incident Investigation Case Study | 5 | P5 (L17 → L18) | — | All M5 tools | — |
| M6.1 | Static Malware Analysis & IOC Extraction | 6 | L18 | LAB-L18-A | PE inspection, strings, hashing, VirusTotal | Static triage workflow |
| M6.2 | Dynamic Analysis, Sandboxing & Malware Triage | 6 | L18 | LAB-L18-B/C | Sandbox report reading, Sysmon | Behaviour-based triage |

## Tool coverage check

| Tool | First lab | Covered |
|---|---|---|
| Splunk | LAB-L08-A | yes |
| Wazuh | LAB-L09-A | yes |
| Sigma | LAB-L10-A | yes |
| TheHive | LAB-L06-B | yes |
| Sysmon | LAB-L07-B | yes |
| Windows Event Viewer | LAB-L05-A | yes |
| Linux audit / journalctl | LAB-L05-C | yes |
| MITRE ATT&CK Navigator | LAB-L14-B | yes |
| D3FEND | LAB-L14-C | yes |
| MISP | LAB-L15-C | yes |
| AlienVault OTX | LAB-L15-B | yes |
| VirusTotal | LAB-L15-A | yes |
| Volatility 3 | LAB-L17-A | yes |
| Autopsy | LAB-L17-D | yes |
| PowerShell | LAB-L02-C | yes |
| Bash | LAB-L02-D | yes |
| Python | LAB-L02-E | yes |
| Wireshark | LAB-L03-C | yes |
