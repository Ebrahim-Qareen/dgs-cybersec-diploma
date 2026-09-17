# Step 4 — Intake  ·  IN PROGRESS

**Goal** — know the source material, pick what feeds each session, and turn it into short notes with diagram ideas, screenshots and lab seeds.

**Done**
- Both ADA trees scanned (589 files, 332 teaching docs) → `knowledge_base/00_source_inventory.md`: sources per session with real page/slide counts, THM rooms per session, what is not used and why, load estimate per session
- `tools/extract_source.py` + `tools/extract_manifest.txt` (≈90 documents) — pptx/pdf/html → text, notes, images under `Resources/extract/LNN/` (gitignored)
- L01 sources extracted: 13 of 13 (complete)
- `knowledge_base/Session_01.md` written — condensed L01 note (topics in teaching order, attack↔detection↔MITRE table, diagram ideas, lab seeds, THM rooms, cut list)

**Doing**
- L01 note done. Next: extract + condense L02 sources into `knowledge_base/Session_02.md`

**Next — per session, in order (L01 → L18)**
1. Extract that session's sources (1–2 min per deck, run in small batches)
2. Read them and write `knowledge_base/Session_NN.md` — one page: topics in teaching order · diagram ideas (what to draw) · screenshots worth reusing (file + slide) · log/packet samples · lab seeds · THM rooms (free-tier checked) · what to cut
3. Hand the note to Step 5

**Rule** — `knowledge_base/` holds condensed notes only, never copies of the decks.
