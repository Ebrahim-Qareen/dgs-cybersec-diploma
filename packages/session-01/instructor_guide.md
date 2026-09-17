# Session 01 — Instructor Guide (instructor-private)

Talk-track and demo notes per block. Keep 25% attack demo max; the rest is what the SOC sees.

## Teach A — Security foundations (70)
- **Open with cost, not theory.** WannaCry (300k+ hosts, hospitals) and Equifax (147M records, unpatched Struts). Ask: which broke Availability, which broke Confidentiality? → sets up CIA.
- **CIA via the bank account.** Balance private (C), balance correct (I), ATM works (A). Every attack breaks one — make students name the pillar out loud.
- **V→T→E→R with the house-lock story.** Broken lock = vulnerability, burglar nearby = threat, break-in = exploit, stolen goods = risk.
- **Malware + actors, fast.** Don't lecture the full catalogue — 2 min: virus/worm spread, trojan hides, RAT controls, keylogger steals, ransomware extorts. Psychology: most attacks start with one click; explain *why* people click (urgency, authority, curiosity).
- **Close on the SOC.** 24/7 room whose job is protecting CIA. That's the seat they're training for.
- Common mistakes: confusing threat vs vulnerability; thinking CIA is only about hackers (hardware failure breaks Availability too).

## Guided Lab A (70) — LAB-L01-A + start LAB-L01-B
- Walk the room: everyone powers DGS-WS01, `ipconfig` shows 10.10.10.x, snapshot `CLEAN` taken.
- Demo Process Explorer once on the projector: path, signature, command line, parent. Then they mirror it.
- Watch for: students running tools without admin (missing detail); reading the tree top-down instead of parent→child.

## Teach B — Windows internals (65)
- **Normal first.** Show a clean process tree so abnormal stands out later.
- **Architecture stack** — user vs kernel mode, HAL; malware wants to go lower.
- **Process tree** — draw explorer→winword (ok) vs winword→powershell→cmd (bad) live.
- **Persistence** — the six places, then "Autoruns sees all of them."
- **Evidence** — put the 4688 line on screen; make them read the parent before you interpret. Findings then conclusion.
- **Attack↔detection↔MITRE table** — this is the diploma's spine; every attack has a detection + ATT&CK ID.
- Common mistakes: treating any powershell.exe as bad (context/parent matters); closing 4625 bursts as noise.

## Independent Lab B + Challenge (80)
- Students finish B alone/in pairs (hints only), then run the first-triage challenge on the page. Debrief the model answer: isolate + collect + escalate, never close.

## Wrap-up (25)
- Hand the cheat sheet. Assign the at-home task (persistence hunt, accounts/UAC, WinFund1). Hook L02: "next time the other half of every SOC — Linux, and the shell you'll script triage in."
