#!/usr/bin/env python3
"""Run extract_source.py over tools/extract_manifest.txt, skipping finished items. Logs to Resources/extract/_log.txt."""
import subprocess, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_source import OUT, slug, ROOT
log = OUT / "_log.txt"; OUT.mkdir(parents=True, exist_ok=True)
for line in (ROOT / "tools/extract_manifest.txt").read_text(encoding="utf-8").splitlines():
    if "|" not in line: continue
    sess, f = line.split("|", 1); src = Path(f)
    dest = OUT / sess / slug(src.stem)
    if (dest / "text.md").exists(): continue
    t = time.time()
    r = subprocess.run([sys.executable, str(ROOT / "tools/extract_source.py"), sess, f], capture_output=True, text=True)
    with log.open("a", encoding="utf-8") as fh:
        fh.write(f"{time.strftime('%H:%M:%S')} {int(time.time()-t):4d}s {r.stdout.strip() or r.stderr.strip()[-200:]}\n")
with log.open("a", encoding="utf-8") as fh: fh.write("ALL DONE\n")
