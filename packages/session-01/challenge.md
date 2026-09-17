# Session 01 — Challenge: First Triage (instructor-private key)

## Scenario (given to students on the page)
Alert on DGS-WS01. User opened `invoice.docx`. Minutes later:
- Tree: `WINWORD.EXE → powershell.exe → cmd.exe`
- 4688: powershell.exe with a long `-enc` command line
- Autoruns: unsigned `update.exe` in `C:\Users\Public`
- 4720: new local account `svc-helper`

Questions: which CIA pillars are at risk? which ATT&CK techniques? what next — close or escalate?

## Model answer (key)
- **CIA:** Confidentiality + Integrity at risk (remote control + new account); Availability could follow (ransomware).
- **Chain:** phishing **T1566.001** → PowerShell **T1059.001** → persistence **T1547** (Public-folder autostart) → new account **T1136.001** → privileged use **T1078**.
- **Action:** do NOT close. Isolate host; capture live processes + connections (Process Explorer, TCPView); collect 4688/4720; **escalate** as a live intrusion. Document findings separately from conclusion.

## Marking (5 pts)
CIA named (1) · ≥3 correct techniques (1) · recognises it as an attack chain not noise (1) · correct next steps incl. isolate+collect+escalate (1) · findings/interpretation kept separate (1).
