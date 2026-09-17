# Session 01 — Quiz + Answer Key (instructor-private)

10 MCQ + 2 practical. On the student page the answers are hidden in `<details>`; keys below.

1. CIA pillar ransomware hits most directly? → **Availability**
2. Burglar nearby, broken lock — threat vs vulnerability? → burglar = **threat**, broken lock = **vulnerability**
3. Why is `WINWORD.EXE → powershell.exe` suspicious? → a document should not spawn a shell (T1059.001)
4. Event ID for new process? → **4688** (shows parent)
5. Many 4625 in a short time? → failed logons = **brute force / password guessing**
6. Tool that shows all auto-start locations? → **Autoruns**
7. Unsigned `C:\Users\Public\update.exe` verdict? → **suspicious** (odd path + unsigned); investigate before deciding
8. What does `whoami /priv` show, why care? → account privileges; powerful ones enable escalation/cred dumping
9. 4720 then 4672 story? → new account created then used with admin rights = **likely backdoor, escalate**
10. Why separate findings from interpretation? → facts stay trustable and reasoning stays checkable

**Practical 1:** find one 4624 and one 4688 in Event Viewer → record account, logon type, parent.
**Practical 2:** in Process Explorer, a process from a user folder → path, publisher, command line, parent + verdict.
