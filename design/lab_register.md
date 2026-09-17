# Lab Register — 79 Labs

> Owner skill: `dgs-design`. **Must always total 79.** Tag meanings:
> `LIVE` = guided in class · `TASK` = post-session task pack · `SELF` = self-study pack.

| ID | Live session | Lab | Tag | Primary tool | ATT&CK |
|---|---|---|---|---|---|
| LAB-L01-A | L01 | Lab verification — VMs, snapshots, `10.10.10.0/24` connectivity check | LIVE | VMware | — |
| LAB-L01-B | L01 | Windows process and service inspection — normal vs suspicious | LIVE | Task Manager, Process Explorer | — |
| LAB-L01-C | L01 | Registry walkthrough — autorun keys and what they tell an analyst | TASK | Registry Editor | T1547 |
| LAB-L01-D | L01 | Accounts, privileges and UAC behaviour on DGS-WS01 | TASK | Windows local users | T1078 |
| LAB-L01-E | L01 | CIA triad and security control mapping worksheet | SELF | — | — |
| LAB-L02-A | L02 | Linux filesystem, users and permissions on DGS-LNX01 | LIVE | bash | — |
| LAB-L02-B | L02 | PowerShell for analysts — processes, services, event log queries | LIVE | PowerShell | — |
| LAB-L02-C | L02 | Service and log inspection with `systemctl` and `journalctl` | TASK | journalctl | — |
| LAB-L02-D | L02 | Bash triage one-liners on `auth.log` | SELF | bash | T1110 |
| LAB-L02-E | L02 | Python script to parse an alert CSV | SELF | Python | — |
| LAB-L03-A | L03 | IP addressing and subnet plan for the DGS lab | LIVE | ipcalc | — |
| LAB-L03-B | L03 | Capture and dissect a TCP handshake and HTTP request | LIVE | Wireshark | — |
| LAB-L03-C | L03 | DNS and DHCP traffic analysis from a provided capture | TASK | Wireshark | T1071.004 |
| LAB-L03-D | L03 | Identify SMB and RDP sessions in traffic | TASK | Wireshark | T1021 |
| LAB-L03-E | L03 | OSI layer mapping drill with tcpdump filters | SELF | tcpdump | — |
| LAB-L04-A | L04 | Domain join and AD object tour — users, groups, OUs, GPO | LIVE | AD DS, ADUC | — |
| LAB-L04-B | L04 | Kerberos authentication observed — `klist` and Event IDs 4768/4769 | LIVE | Event Viewer | — |
| LAB-L04-C | L04 | NTLM vs Kerberos from captured authentication logs | TASK | Event Viewer | T1550 |
| LAB-L04-D | L04 | LDAP queries and enumeration awareness | SELF | ldapsearch | T1087.002 |
| LAB-L05-A | L05 | Windows logon investigation — 4624 / 4625 / 4672 | LIVE | Event Viewer | T1078 |
| LAB-L05-B | L05 | HTTP anatomy and web server log reading | LIVE | Apache logs, dev tools | — |
| LAB-L05-C | L05 | Linux authentication and syslog investigation | TASK | journalctl | T1110 |
| LAB-L05-D | L05 | Spot the attack in a provided web access log | TASK | Apache logs | T1190 |
| LAB-L05-E | L05 | OWASP Top 10 awareness map — attack to log evidence | SELF | DVWA | T1190 |
| LAB-L06-A | L06 | Triage workflow on five sample alerts | LIVE | Wazuh alerts | — |
| LAB-L06-B | L06 | TheHive case creation — observables, tasks, closure | LIVE | TheHive | — |
| LAB-L06-C | L06 | TP / FP classification of ten alerts with justification | TASK | TheHive | — |
| LAB-L06-D | L06 | Severity and escalation matrix exercise | SELF | — | — |
| LAB-L07-A | L07 | Sysmon event inspection and process tree reconstruction | LIVE | Sysmon | T1059 |
| LAB-L07-B | L07 | Correlate an authentication failure burst across Windows, Linux and web logs | LIVE | Event Viewer, journalctl | T1110 |
| LAB-L07-C | L07 | Build a 60-minute timeline from three log sources | TASK | — | — |
| LAB-L08-A | L08 | Splunk data onboarding — index, sourcetype, field extraction | LIVE | Splunk | — |
| LAB-L08-B | L08 | SPL fundamentals — search, stats, timechart on lab data | LIVE | Splunk SPL | — |
| LAB-L08-C | L08 | Investigate a brute-force scenario in a public BOTS dataset | TASK | Splunk | T1110 |
| LAB-L08-D | L08 | Build a failed-logon dashboard | SELF | Splunk | — |
| LAB-L09-A | L09 | Wazuh agent enrolment and log flow verification | LIVE | Wazuh | — |
| LAB-L09-B | L09 | Decoder and custom rule creation with alert test | LIVE | Wazuh | — |
| LAB-L09-C | L09 | Write three Wazuh rules for lab attack simulations | TASK | Wazuh | T1059, T1110 |
| LAB-L09-D | L09 | Wazuh dashboards and alert triage view | SELF | Wazuh | — |
| LAB-L10-A | L10 | Sigma rule anatomy — write one from a log sample | LIVE | Sigma | — |
| LAB-L10-B | L10 | Convert Sigma to SPL and to Wazuh, test both | LIVE | sigma-cli | — |
| LAB-L10-C | L10 | Convert and validate three public Sigma rules | TASK | sigma-cli | — |
| LAB-L10-D | L10 | Detection logic quality review of five rules | TASK | — | — |
| LAB-L10-E | L10 | Detection lifecycle documentation exercise | SELF | — | — |
| LAB-L11-A | L11 | Atomic Red Team execution and its Sysmon evidence | LIVE | Atomic Red Team, Sysmon | T1059.001 |
| LAB-L11-B | L11 | Persistence — run key and scheduled task, with detection | LIVE | Sysmon, Wazuh | T1547.001, T1053.005 |
| LAB-L11-C | L11 | Kerberoasting simulation and 4769 detection | TASK | Event Viewer, Wazuh | T1558.003 |
| LAB-L11-D | L11 | Credential access awareness — LSASS handle events in logs | SELF | Sysmon | T1003.001 |
| LAB-L12-A | L12 | Nmap scan against the lab and its detection in packets and logs | LIVE | Nmap, Wireshark | T1046 |
| LAB-L12-B | L12 | SQL injection on DVWA and its access-log fingerprint | LIVE | DVWA, Apache logs | T1190 |
| LAB-L12-C | L12 | Detect exfiltration patterns in a provided capture | TASK | Wireshark | T1048 |
| LAB-L12-D | L12 | XSS and path traversal log signatures | SELF | Apache logs | T1190 |
| LAB-L13-A | L13 | Write a full detection use case document from one alert | LIVE | — | — |
| LAB-L13-B | L13 | Tune a noisy Wazuh rule with before/after evidence | LIVE | Wazuh | — |
| LAB-L13-C | L13 | Reduce false positives on three provided rules and document it | TASK | Wazuh, Splunk | — |
| LAB-L13-D | L13 | Multi-event correlation rule design exercise | SELF | Splunk | — |
| LAB-L14-A | L14 | Build a hunt hypothesis from a threat report | LIVE | Hunt template | — |
| LAB-L14-B | L14 | ATT&CK Navigator coverage map of the lab detections | LIVE | ATT&CK Navigator | — |
| LAB-L14-C | L14 | D3FEND countermeasure mapping for five techniques | TASK | D3FEND | — |
| LAB-L14-D | L14 | Endpoint hunt in Sysmon data | TASK | Splunk, Sysmon | T1059 |
| LAB-L14-E | L14 | Network hunt — beaconing detection drill | SELF | Splunk | T1071 |
| LAB-L14-F | L14 | Log-based hunt for rare parent-child process pairs | SELF | Wazuh | T1055 |
| LAB-L15-A | L15 | VirusTotal enrichment of hashes, domains and IPs from a case | LIVE | VirusTotal | — |
| LAB-L15-B | L15 | OTX pulse review and IOC extraction to a watchlist | LIVE | AlienVault OTX | — |
| LAB-L15-C | L15 | MISP event creation and attribute tagging | TASK | MISP | — |
| LAB-L15-D | L15 | Turn a threat intel report into hunt queries | SELF | — | — |
| LAB-L16-A | L16 | IR lifecycle walkthrough on a live lab incident | LIVE | Playbook template | — |
| LAB-L16-B | L16 | Triage and scoping — how far did it spread | LIVE | Wazuh, TheHive | — |
| LAB-L16-C | L16 | Containment decision exercise with Wazuh active response | TASK | Wazuh | — |
| LAB-L16-D | L16 | Live response collection run and output review | TASK | PowerShell | T1005 |
| LAB-L16-E | L16 | Order of volatility and chain of custody exercise | SELF | — | — |
| LAB-L17-A | L17 | Memory triage with Volatility 3 — pslist, netscan, malfind | LIVE | Volatility 3 | T1055 |
| LAB-L17-B | L17 | Windows artefact analysis in Autopsy — prefetch, registry, MFT | LIVE | Autopsy | — |
| LAB-L17-C | L17 | Build a forensic timeline from artefacts | TASK | Autopsy | — |
| LAB-L17-D | L17 | Extract and analyse persistence from a registry hive | TASK | Registry Explorer | T1547 |
| LAB-L17-E | L17 | USB and user activity artefacts exercise | SELF | Autopsy | T1091 |
| LAB-L18-A | L18 | Static triage — hashes, strings, PE inspection, IOC extraction | LIVE | strings, PE viewer, VirusTotal | — |
| LAB-L18-B | L18 | Dynamic behaviour reading from a sandbox report and Sysmon | LIVE | Sandbox report, Sysmon | T1204 |
| LAB-L18-C | L18 | Full triage report on a provided simulated sample | TASK | All M6 tools | — |

## Totals — must stay true

| Tag | Count |
|---|---|
| LIVE | 36 |
| TASK | 25 |
| SELF | 18 |
| **Total** | **79** |

| Module | Labs | Published labs | Match |
|---|---|---|---|
| M1 (L01–L05) | 24 | 24 | yes |
| M2 (L06–L10 A/B/C) | 18 | 18 | yes |
| M3 (L10 D/E, L11–L13) | 14 | 14 | yes |
| M4 (L14–L15) | 10 | 10 | yes |
| M5 (L16–L17) | 10 | 10 | yes |
| M6 (L18) | 3 | 3 | yes |
| **Total** | **79** | **79** | yes |
