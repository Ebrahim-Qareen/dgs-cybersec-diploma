# Step 5 — Build the sessions  ·  IN PROGRESS

**Goal** — 18 sessions students can learn from and you can deliver from, each heavy on diagrams, SVGs, screenshots and icons, in simple short English.

**Per session, in this order**
1. **Outline gate** — one page: sections, diagrams to draw, labs, task. You approve before any HTML.
2. **Package** — `packages/session-NN/` (session_plan · instructor_guide · student_guide · guided_lab · task_pack · self_study · quiz · build_log)
3. **Page** — `docs/session-NN/index.html` from the builder: 8-part in-class order, evidence boxes, every attack paired with detection + ATT&CK ID
4. **Labs** — tested in the real VMs, files published under `docs/downloads/` with SHA-256
5. **Gate** — `testing/verify.py` + Part 9 checklist
6. You review → approve → publish → next session

**Done**
- **L01** — package (`packages/session-01/`, 10 files incl. cheat_sheet + challenge) · paged student page (`docs/session-01/index.html`, 17 pages, left agenda, prev/next, 7 inline SVGs, labs A/B in class, free at-home task, challenge, cheat sheet, 10+2 quiz) · gate: ALL CHECKS PASSED · rendered at 1400 and 480

**Doing** — L01 awaiting your review (outline gate + content in one pass, per your "build it all" instruction). Labs not yet tested on real VMs (Phase 2).

**Next** — your L01 review → fixes → then L02 (intake note first).
