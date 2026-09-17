# Session 01 — Guided Lab (in class)

Environment: `DGS-WS01` (Windows), lab network `10.10.10.0/24`. Bring the prepared image ready to boot.

## LAB-L01-A — Get the lab running (LIVE)
1. Open VMware, power on **DGS-WS01**, log in.
2. `ipconfig` → confirm an address on `10.10.10.0/24`.  *Expected:* IPv4 in that range.
3. Take a snapshot named **CLEAN**.  *Expected:* snapshot listed with today's date.
4. `systeminfo`  *Expected:* OS name/version shown. `whoami /priv`  *Expected:* your privilege list.

**Deliverable:** one line stating your IP, OS version, and whether you are admin.

## LAB-L01-B — Normal vs suspicious process (LIVE, finish independently)
1. Open **Process Explorer** as administrator. Find the tree (View → show tree lines).
2. Choose any process. Record four fields: **path**, **company/signature**, **command line**, **parent**.
3. Right-click → **Properties** → check **Image** (path, publisher, hash) and **TCP/IP** (connections).
4. Give a one-line verdict: normal or suspicious, and the evidence for it.

**Expected output:** a short table of 3 processes with the four fields and a verdict each. A clean host shows signed Microsoft binaries from `System32` with sensible parents (e.g. `services.exe → svchost.exe`).

**Instructor answer key (private):** any unsigned binary from `AppData\Temp` / `C:\Users\Public`, or a shell whose parent is an Office app, is the intended "suspicious" find on the seeded image.
