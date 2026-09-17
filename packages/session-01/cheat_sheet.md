# Session 01 — Cheat Sheet (one page)

## Commands
| Command | Shows |
|---|---|
| `systeminfo` | OS, version, patches |
| `tasklist` | running processes |
| `whoami /priv` | your privileges |
| `net user` | local accounts |
| `net localgroup administrators` | who is admin |
| `Get-Process` | processes (PowerShell) |
| `Get-WinEvent -LogName Security` | read the Security log |
| Ctrl+Shift+Esc | open Task Manager |

## Event IDs
4624 logon ok · 4625 logon failed · 4672 admin logon · 4688 new process · 4720 new account · 7045 new service.

## Suspicious paths
`AppData\Temp` · `C:\Users\Public` · `ProgramData\<random>` · anything unsigned dressed as a system file.

## Triage tools
Process Explorer (tree) · Autoruns (persistence) · TCPView (connections) · Event Viewer (the log).

## Golden rule
Findings first (the log line), conclusion second. Every attack has a detection and a MITRE ATT&CK ID.
