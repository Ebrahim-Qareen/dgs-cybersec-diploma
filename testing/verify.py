#!/usr/bin/env python3
"""DGS diploma quality gate. Run from the repo root:  python3 testing/verify.py"""
import hashlib, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
fail = []
def chk(ok, msg):
    print(("  PASS  " if ok else "  FAIL  ") + msg)
    if not ok: fail.append(msg)

print("\n== design integrity ==")
reg = (ROOT/"design/lab_register.md").read_text(encoding="utf-8")
ids = re.findall(r'\| (LAB-L\d\d-[A-F]) \|', reg)
chk(len(ids) == 79, f"lab register has 79 labs (found {len(ids)})")
chk(len(set(ids)) == len(ids), "lab IDs are unique")
rows = re.findall(r'\| LAB-L\d\d-[A-F] \| L\d\d \| .+? \| (LIVE|TASK|SELF) \|', reg)
counts = {t: rows.count(t) for t in ("LIVE","TASK","SELF")}
chk(counts == {"LIVE":36,"TASK":25,"SELF":18}, f"lab tags 36/25/18 (found {counts})")

tm = (ROOT/"design/topic_map.md").read_text(encoding="utf-8")
topics = {t.rstrip('ab') for t in re.findall(r'\| (M[1-6]\.\d[ab]?) \|', tm)}
chk(len(topics) == 35, f"topic map covers 35 published topics (found {len(topics)})")

ra = (ROOT/"design/roadmap_analysis.md").read_text(encoding="utf-8")
sessions = re.findall(r'^\| (\d\d) \| \d \| M', ra, re.M)
chk(len(sessions) == 18, f"roadmap analysis maps 18 live sessions (found {len(sessions)})")

print("\n== tool coverage ==")
tools = ["Splunk","Wazuh","Sigma","TheHive","Sysmon","Event Viewer","journalctl",
         "ATT&CK Navigator","D3FEND","MISP","OTX","VirusTotal","Volatility 3",
         "Autopsy","PowerShell","bash","Python","Wireshark"]
for t in tools:
    chk(t in reg or t in tm, f"tool used in a lab: {t}")

print("\n== no secrets / no private leakage in docs/ ==")
pat = re.compile(r'(?i)(password\s*[:=]|api[_-]?key|secret\s*[:=]|BEGIN [A-Z ]*PRIVATE KEY|xox[baprs]-|AKIA[0-9A-Z]{16})')
leak = re.compile(r'(?i)(2 month|two month|two-month|6[- ]hour session|compress|because of time)')
ip = re.compile(r'\b(?!10\.10\.10\.)(?!127\.0\.0\.1)(?!0\.0\.0\.0)(?:\d{1,3}\.){3}\d{1,3}\b')
for p in sorted((ROOT/"docs").rglob("*.html")):
    txt = p.read_text(encoding="utf-8")
    rel = p.relative_to(ROOT)
    chk(not pat.search(txt), f"no credentials in {rel}")
    chk(not leak.search(txt), f"no private delivery details in {rel}")
    chk(not ip.search(txt), f"no out-of-range IPs in {rel}")

print("\n== session pages ==")
sess = sorted((ROOT/"docs").glob("session-*/index.html"))
chk(len(sess) == 18, f"18 session pages exist (found {len(sess)})")
for i in range(1, 19):
    chk((ROOT/f"docs/session-{i:02d}/index.html").exists(), f"docs/session-{i:02d}/index.html")

print("\n== html links ==")
for p in sorted((ROOT/"docs").rglob("*.html")):
    for href in re.findall(r'href="([^"#?]+)"', p.read_text(encoding="utf-8")):
        if href.startswith(("http://","https://","mailto:")): continue
        if href.startswith("/"): continue          # 404.html uses site-absolute paths
        chk((p.parent/href).resolve().exists(), f"{p.relative_to(ROOT)} -> {href}")
    for src in re.findall(r'src="([^"#?]+)"', p.read_text(encoding="utf-8")):
        if src.startswith(("http://","https://","data:")):
            chk(False, f"external asset in {p.relative_to(ROOT)}: {src}")

print("\n== file manifest (sha256) ==")
for p in sorted(ROOT.rglob("*")):
    if p.is_dir() or ".git" in p.parts or "Resources" in p.parts: continue
    h = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
    print(f"  {h}  {p.stat().st_size:>8}  {p.relative_to(ROOT)}")

print("\n== result ==")
print(f"  {'FAILED: ' + str(len(fail)) + ' check(s)' if fail else 'ALL CHECKS PASSED'}")
sys.exit(1 if fail else 0)
