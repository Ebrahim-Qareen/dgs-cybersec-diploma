# Session 01 — Student Guide

Clean reference notes for after class. Includes the parts we did not lecture: the case study, the deeper "how it works", and the transition to next session. The quiz is on the session page.

## 1. Security in one idea
Security protects three things about data — keep it **private (C)**, **correct (I)**, **reachable (A)**. That is the CIA triad. Every attack breaks at least one. Bank account: only you see the balance (C), the balance is right (I), the ATM works (A).

## 2. The four words
**Vulnerability** = a weakness. **Threat** = who might use it. **Exploit** = the actual attack. **Risk** = the harm if it works.

## 3. Malware, briefly
Virus/worm spread; trojan hides in something you trust; RAT gives remote control; keylogger steals keystrokes; ransomware encrypts for money. Attackers range from script kiddies to criminal crews and nation-states. Most attacks start with one click — that is why awareness matters as much as tools.

## 4. Windows, the parts that matter
- **User mode** runs your apps; **kernel mode** + drivers run below via the **HAL**. Malware wants to go lower to hide.
- **Process** = a running program; its **parent** started it. The **process tree** shows the chain. Trusted names, wrong shape = red flag.
- **Persistence** = surviving reboot: Run keys, Startup folder, Scheduled Tasks, Services, drivers, DLL hijack. **Autoruns** checks them all.

## 5. Case study (read at home) — WannaCry, 2017
A worm using the EternalBlue SMB exploit spread across unpatched Windows machines, encrypting files and demanding Bitcoin. It hit the NHS, Renault, Telefónica. It broke **Availability** first. Lessons: patch fast, segment networks, keep offline backups, have an IR plan. Marcus Hutchins' sinkhole domain acted as a kill switch.

## 6. Technical deep dive (read at home) — the Security log
The Windows Security log records who did what. Six IDs matter most: **4624** logon ok, **4625** logon failed, **4672** privileged logon, **4688** new process (with parent), **4720** account created, **7045** service installed. Sysmon adds richer process, network and registry events (you meet it in L07).

## 7. Six Event IDs (memorise)
4624 · 4625 · 4672 · 4688 · 4720 · 7045.

## 8. Next session
L02 — Linux fundamentals and the shell (Bash/PowerShell) you will use to script triage. You will meet the other half of nearly every SOC environment.
