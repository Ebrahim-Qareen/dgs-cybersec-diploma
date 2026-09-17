#!/usr/bin/env python3
"""Build every page under docs/ from one layout + the design/ data files.
Run from the repo root:  python3 tools/build_site.py
Owner skill: dgs-session-html. Never hand-edit a generated page — edit here."""
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
# every page links the stylesheet with its content hash, so a redeploy never serves stale CSS
CSS_VER = hashlib.sha256((ROOT / "docs/assets/css/dgs.css").read_bytes()).hexdigest()[:8]

NAV = [("Home", "index.html", "home"), ("Curriculum", "roadmap.html", "roadmap"),
       ("Sessions", "sessions.html", "sessions"),
       ("Labs", "labs/index.html", "labs"), ("Projects", "projects/index.html", "projects"),
       ("Tools", "resources/tools.html", "tools"), ("Practice", "resources/practice.html", "practice")]

MODULES = [
    (1, "Foundation Phase", "Computer, OS, networking &amp; security fundamentals", 64, 16, 24,
     "Computers, operating systems, networking, PowerShell and Bash, Active Directory, log analysis and "
     "web technology — the ground every analyst stands on."),
    (2, "Security Operations &amp; SIEM", "SOC workflow, triage, Splunk, Wazuh, Sigma", 40, 10, 18,
     "How a SOC runs: alert triage, incident handling, event correlation, then Splunk and Wazuh end to end "
     "and one Sigma rule that runs on both."),
    (3, "Detection Engineering", "Attack analysis &amp; detection development", 32, 8, 14,
     "Endpoint, Active Directory, network and web attacks — each one paired with the detection that catches "
     "it, then use cases, correlation and alert tuning."),
    (4, "Threat Hunting &amp; Intelligence", "Hunting methodology, ATT&amp;CK, CTI", 24, 6, 10,
     "Hypothesis-driven hunting, MITRE ATT&amp;CK and adversary behaviour, IOC hunting and enrichment with "
     "MISP, OTX and VirusTotal."),
    (5, "Incident Response &amp; Forensics", "IR lifecycle, live response, DFIR", 24, 6, 10,
     "The IR lifecycle under pressure: triage, scoping, containment, live response, memory forensics and "
     "Windows artefact analysis."),
    (6, "Malware Triage", "Static, dynamic and IOC extraction", 8, 2, 3,
     "Malware analysis at the level an analyst actually needs: safe static triage, sandbox behaviour and a "
     "written verdict."),
]

def layout(title, desc, active, depth, body, wide_footer=True):
    p = depth
    CSS_VER = globals()["CSS_VER"]
    CUR = ' aria-current="page"'
    nav = "\n".join(
        '      <a href="{}{}"{}>{}</a>'.format(p, href, CUR if key == active else "", label)
        for label, href, key in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{p}assets/img/favicon.png" type="image/png">
<link rel="stylesheet" href="{p}assets/css/dgs.css?v={CSS_VER}">
</head>
<body>
<header class="topbar">
  <div class="wrap topbar-inner">
    <a class="brand" href="{p}index.html">
      <span class="plate"><img src="{p}assets/img/dgs-logo-dark.png" alt="DGS Academy"></span>
      <span class="brand-text"><b>Cyber Security Diploma</b><span>DGS Academy</span></span>
    </a>
    <nav class="nav" aria-label="Main">
{nav}
    </nav>
  </div>
</header>

{body}

<footer class="site-footer">
  <div class="wrap footer-inner">
    <span class="plate"><img src="{p}assets/img/dgs-logo-dark.png" alt="DGS Academy"></span>
    <span>Cyber Security Diploma &middot; Blue Team / Security Operations track</span>
    <span>Instructor: Ebrahim Mohamed Ahmed</span>
  </div>
</footer>
<script>
(function(){{document.documentElement.classList.add('js');var els=document.querySelectorAll('.reveal');if(!('IntersectionObserver' in window)){{els.forEach(function(e){{e.classList.add('in')}});return;}}
var io=new IntersectionObserver(function(en){{en.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('in');io.unobserve(x.target);}}}})}},{{threshold:.15}});
els.forEach(function(e){{io.observe(e)}});}})();
</script>
</body>
</html>
"""

def write(rel, html):
    path = DOCS / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print(f"  wrote docs/{rel}  ({len(html):,} bytes)")

# ---------------------------------------------------------------- home
def build_home():
    cards = "\n".join(f"""    <article class="card">
      <span class="rail m{m}-rail"></span>
      <span class="tag m{m}">Module {m}</span>
      <h3>{name}</h3>
      <p class="meta">{hours} hours &middot; {sess} sessions &middot; {labs} labs &middot; 1 project</p>
      <p>{blurb}</p>
      <a class="more" href="roadmap.html#m{m}">View topics &rarr;</a>
    </article>""" for m, name, _sub, hours, sess, labs, blurb in MODULES)

    body = f"""<main>
<section class="wrap hero">
  <span class="kicker">Professional Diploma</span>
  <h1>Cyber Security Diploma<br><span class="accent">Blue Team &amp; Security Operations</span></h1>
  <p class="lead">A hands-on, career-focused program that trains you to monitor, detect, investigate and
  respond to real cyber threats — built entirely around practical labs and real investigations. You finish
  with detections you wrote yourself and investigations you can show an interviewer.</p>
  <div class="badges">
    <span class="badge">6 months</span><span class="badge">2 sessions / week</span>
    <span class="badge">No prerequisites</span><span class="badge">Portfolio on graduation</span>
  </div>
  <div class="cta-row">
    <a class="btn btn-primary" href="sessions.html">Open the sessions</a>
    <a class="btn" href="roadmap.html">Explore the curriculum</a>
    <a class="btn" href="labs/index.html">See the 79 labs</a>
  </div>
</section>

<section class="wrap section-sm">
  <div class="stats">
    <div class="stat"><div class="n">192</div><div class="l">Training hours</div></div>
    <div class="stat"><div class="n">48</div><div class="l">Live sessions</div></div>
    <div class="stat"><div class="n">79</div><div class="l">Practical labs</div></div>
    <div class="stat"><div class="n">6</div><div class="l">Real projects</div></div>
  </div>
</section>

<section class="wrap section">
  <div class="sec-head"><h2>The learning journey</h2>
    <span class="note">Six modules, 35 topics, every one practised in the lab</span></div>
  <div class="grid">
{cards}
  </div>
</section>

<section class="wrap section">
  <div class="sec-head"><h2>How every topic is taught</h2>
    <span class="note">The same shape, every session — so nothing stays abstract</span></div>
  <div class="grid grid-2">
    <div class="box box-why"><div class="box-title">Why it matters</div>
      The real impact first — a breach, a number, a case. You never learn a control before you know what it costs to skip it.</div>
    <div class="box box-attacker"><div class="box-title">Attacker view</div>
      How the technique is abused, and the human reason it works: why people click, why admins misconfigure, why alerts get closed too fast.</div>
    <div class="box box-evidence"><div class="box-title">Evidence &mdash; Sysmon EID 1 &mdash; T1059.001</div>
      ParentImage=WINWORD.EXE &rarr; Image=powershell.exe CommandLine="powershell -enc ..."</div>
    <div class="box box-analyst"><div class="box-title">Analyst view</div>
      What the SOC concludes from that evidence, what it does next, and the detection that would have caught it earlier.</div>
    <div class="box box-lab"><div class="box-title">Lab</div>
      You run it yourself. Every attack shown is paired with its detection and its MITRE ATT&amp;CK technique.</div>
    <div class="box box-take"><div class="box-title">Key takeaways</div>
      Then a practical task on data you have not seen before — because recognising an attack is a skill, not a fact.</div>
  </div>
</section>

<section class="wrap section">
  <div class="sec-head"><h2>What you graduate with</h2></div>
  <div class="grid">
    <div class="card"><span class="rail m2-rail"></span><h3>Jobs you can apply for</h3>
      <p>SOC Analyst — Tier 1<br>Security Monitoring Analyst<br>Junior Incident Responder<br>SIEM Support Analyst</p></div>
    <div class="card"><span class="rail m3-rail"></span><h3>Tools you will master</h3>
      <p>Splunk &middot; Wazuh &middot; Sigma &middot; TheHive &middot; Sysmon &middot; Windows Event Viewer &middot; Linux audit logs &middot;
      MITRE ATT&amp;CK Navigator &middot; D3FEND &middot; MISP &middot; AlienVault OTX &middot; VirusTotal &middot; Volatility 3 &middot;
      Autopsy &middot; PowerShell &middot; Bash &middot; Python</p>
      <a class="more" href="resources/tools.html">Full tool stack &rarr;</a></div>
    <div class="card"><span class="rail m4-rail"></span><h3>Your portfolio</h3>
      <p>Six completed investigations, detection rules you wrote and tested yourself, and a full incident
      report — the evidence an interviewer actually asks for.</p>
      <a class="more" href="projects/index.html">See the projects &rarr;</a></div>
  </div>
</section>
</main>"""
    write("index.html", layout("Cyber Security Diploma — DGS Academy",
        "DGS Academy Cyber Security Diploma — Blue Team and Security Operations track. "
        "192 training hours, 79 hands-on labs, 6 real projects.", "home", "", body))

# ------------------------------------------------------------ curriculum
TOPICS = {
 1: [("Computer, Operating Systems &amp; Security Fundamentals", "How a machine boots and runs, virtualization, the CIA triad, authentication and authorization, and the language security teams use every day."),
     ("Windows Internals &amp; Linux Fundamentals", "Processes, services, the registry and privileges on Windows; the filesystem, users, permissions and services on Linux."),
     ("Networking Fundamentals &amp; Protocol Analysis", "IP addressing and subnetting, the OSI and TCP/IP models, encapsulation, and reading DNS, HTTP, SMB and RDP on the wire."),
     ("PowerShell &amp; Bash for Security Operations", "The commands an analyst actually uses: querying processes, services and event logs, and automating repetitive triage."),
     ("Active Directory &amp; Authentication Fundamentals", "Domains, objects and group policy; how NTLM, Kerberos and LDAP authenticate a user and what each writes to the logs."),
     ("Windows, Linux &amp; Web Log Analysis", "The Event IDs that matter, syslog and journald, and web server access and error logs — where the evidence lives."),
     ("Web Technologies &amp; Common Attack Awareness", "HTTP end to end, the modern web stack, and the OWASP Top 10 seen from the defender's side."),
     ("Foundation Investigation &amp; Capstone", "Your first full investigation across Windows, Linux and web evidence, written up as a report.")],
 2: [("SOC Operations, Alert Triage &amp; Incident Handling", "How a security operations centre runs, how an alert becomes a case, true positive versus false positive, severity and escalation, case work in TheHive."),
     ("Log Analysis &amp; Event Correlation", "Reconstructing a process tree from Sysmon, and correlating one event across endpoint, network and web sources."),
     ("Splunk Investigation &amp; Detection Development", "Indexing and sourcetypes, SPL from first search to statistics and dashboards, investigating a real attack dataset."),
     ("Wazuh Deployment, Monitoring &amp; Detection", "Agents, decoders, rules and alerts — building the pipeline end to end and testing your own detections against it."),
     ("Sigma Rules &amp; Cross-SIEM Detection Engineering", "Writing one rule once and running it everywhere: Sigma syntax, conversion to SPL and Wazuh, and validating both.")],
 3: [("Detection Engineering Fundamentals", "The detection lifecycle, what makes rule logic good or fragile, and how coverage is measured."),
     ("Endpoint Attacks &amp; Detection Techniques", "Execution, persistence and defence evasion simulated in the lab, each traced back to its Sysmon and event-log evidence."),
     ("Active Directory Attacks &amp; Detection", "Credential access and lateral movement inside a domain, and the authentication events that expose them."),
     ("Network Attacks &amp; Detection Techniques", "Scanning, interception and exfiltration patterns as they appear in packets, firewall logs and IDS alerts."),
     ("Web Attacks &amp; Detection Techniques", "Injection, cross-site scripting and traversal — what each leaves behind in a web server log."),
     ("Detection Use Cases &amp; Correlation Logic", "Turning a threat into a documented use case, and writing logic that needs more than one event to fire."),
     ("Alert Tuning &amp; False Positive Reduction", "Making a noisy rule useful with evidence before and after, and proving you did not break the detection."),
     ("Detection Development Project", "Build, test and document a set of working detections across both SIEM platforms.")],
 4: [("Threat Hunting Methodology", "Hypothesis, data, query, finding — hunting as a repeatable method rather than a search for luck."),
     ("MITRE ATT&amp;CK &amp; Adversary Behaviors", "Tactics, techniques and procedures, the Pyramid of Pain, ATT&amp;CK Navigator and D3FEND countermeasures."),
     ("Endpoint, Network &amp; Log-Based Hunting", "Practical hunts per data source: rare process ancestry, beaconing patterns, anomalous authentication."),
     ("IOC Hunting &amp; Threat Intelligence", "Indicator types and their lifetime, enrichment with VirusTotal and OTX, and turning intel into watchlists."),
     ("Threat Intelligence Platforms &amp; Enrichment", "MISP events and attributes, feed quality, and wiring enrichment into the triage workflow."),
     ("Threat Hunting Investigation Project", "Run a full hunt from a published threat report and document what you found.")],
 5: [("Incident Response Lifecycle", "Preparation, detection, analysis, containment, eradication, recovery and lessons learned — with playbooks you can follow under pressure."),
     ("Triage, Scoping &amp; Containment", "Deciding how far an incident spread and what to isolate first, without destroying the evidence."),
     ("Live Response &amp; Evidence Collection", "Order of volatility, collecting from a running system, and chain of custody done properly."),
     ("Memory Forensics", "Volatility 3 against a real memory image: processes, network connections and injected code."),
     ("Windows Forensic Artifacts Analysis", "Prefetch, registry hives, the MFT, user activity and USB traces — building a timeline that holds up."),
     ("Incident Investigation Case Study", "A complete incident, investigated and reported from first alert to lessons learned.")],
 6: [("Static Malware Analysis &amp; IOC Extraction", "Hashes, strings, file structure and imports — what you can learn safely before anything runs."),
     ("Dynamic Analysis, Sandboxing &amp; Malware Triage", "Reading a sandbox report like an analyst, matching behaviour to endpoint telemetry, and writing the triage verdict.")],
}

MOD_COLOR = {1: "#2E86DE", 2: "#4FB8F0", 3: "#E48424", 4: "#2DD4A0", 5: "#A78BFA", 6: "#FF5C6C"}
MOD_SHORT = {1: "Foundation", 2: "SOC &amp; SIEM", 3: "Detection", 4: "Hunting &amp; CTI",
             5: "IR &amp; Forensics", 6: "Malware triage"}

# simple inline icons, one per module (24x24 grid, stroked)
MOD_ICON = {
 1: '<rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/>',
 2: '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/><path d="M12 3v4M12 17v4M3 12h4M17 12h4"/>',
 3: '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>',
 4: '<circle cx="10" cy="10" r="6"/><path d="M14.5 14.5L21 21"/><path d="M8 10h4M10 8v4"/>',
 5: '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5l8-3z"/><path d="M12 8v6M9 11h6"/>',
 6: '<rect x="7" y="8" width="10" height="12" rx="5"/><path d="M12 8V5M9 5l3 3 3-3M3 12h4M17 12h4M4 18l3-2M20 18l-3-2M4 7l3 2M20 7l-3 2"/>',
}
def icon(m):
    return ('<span class="mod-icon"><svg viewBox="0 0 24 24" fill="none" stroke="{}" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round">{}</svg></span>').format(MOD_COLOR[m], MOD_ICON[m])

def journey_svg():
    xs = [110, 310, 510, 710, 910, 1110]; ys = [300, 262, 224, 186, 148, 110]
    d = "M{} {}".format(xs[0], ys[0])
    for i in range(1, 6):
        cx = (xs[i-1] + xs[i]) / 2
        d += " C{} {} {} {} {} {}".format(cx, ys[i-1], cx, ys[i], xs[i], ys[i])
    nodes = []
    for i, (m, name, sub, hours, sess, labs, _b) in enumerate(MODULES):
        x, y, c = xs[i], ys[i], MOD_COLOR[m]
        nodes.append("""
  <a class="node" href="#m{m}" style="color:{c}">
    <circle cx="{x}" cy="{y}" r="34" fill="{c}" fill-opacity=".14" class="pulse"/>
    <circle class="core" cx="{x}" cy="{y}" r="24" fill="#0E2140" stroke="{c}" stroke-width="3"/>
    <text x="{x}" y="{y}" dy="6" text-anchor="middle" fill="{c}" font-size="18" font-weight="700" class="mono">{m}</text>
    <text x="{x}" y="{ly}" text-anchor="middle" fill="#E6EEF8" font-size="14" font-weight="650">{short}</text>
    <text x="{x}" y="{ly2}" text-anchor="middle" fill="#7E93B5" font-size="12" class="mono">{hours} h &middot; {labs} labs</text>
  </a>""".format(m=m, c=c, x=x, y=y, ly=y+52, ly2=y+70, short=MOD_SHORT[m], hours=hours, labs=labs))
    return """<figure class="diagram reveal">
<svg viewBox="0 0 1220 400" role="img" aria-label="The six modules as one rising path from foundation to malware triage">
  <defs>
    <linearGradient id="jg" x1="0" x2="1"><stop offset="0" stop-color="#2E86DE"/><stop offset="1" stop-color="#E48424"/></linearGradient>
  </defs>
  <path d="{d}" fill="none" stroke="#1B3A66" stroke-width="10" stroke-linecap="round"/>
  <path d="{d}" fill="none" stroke="url(#jg)" stroke-width="4" stroke-linecap="round" opacity=".9"/>
  <path d="{d}" fill="none" stroke="#E6EEF8" stroke-width="2.5" stroke-linecap="round" class="flow" opacity=".8"/>
  <text x="60" y="360" fill="#7E93B5" font-size="12" class="mono">START &middot; no prerequisites</text>
  <text x="1160" y="60" text-anchor="end" fill="#F7A94A" font-size="12" class="mono">JOB-READY &middot; SOC ANALYST T1</text>{nodes}
</svg>
<figcaption>Six modules, one climb. Each module only uses what the one before it taught — click a node to jump to it.</figcaption>
</figure>""".format(d=d, nodes="".join(nodes))

def loop_svg():
    import math
    steps = [("Detect", "#4FB8F0", "SIEM alert, hunt hit, user report"),
             ("Triage", "#E48424", "True or false positive? How bad?"),
             ("Investigate", "#A78BFA", "Logs, packets, memory — what happened"),
             ("Respond", "#FF5C6C", "Contain, eradicate, recover"),
             ("Improve", "#2DD4A0", "New detection, tuned rule, lesson")]
    cx, cy, r = 300, 210, 140
    out = []
    pts = []
    for i, (name, c, sub) in enumerate(steps):
        a = -math.pi/2 + i * 2*math.pi/5
        x, y = cx + r*math.cos(a), cy + r*math.sin(a)
        pts.append((x, y))
        tx = x + 62*math.cos(a); ty = y + 62*math.sin(a)
        anchor = "middle" if abs(math.cos(a)) < .3 else ("start" if math.cos(a) > 0 else "end")
        out.append("""
  <g class="node" style="color:{c}">
    <circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="{c}" fill-opacity=".12"/>
    <circle class="core" cx="{x:.0f}" cy="{y:.0f}" r="30" fill="#0E2140" stroke="{c}" stroke-width="3"/>
    <text x="{x:.0f}" y="{y:.0f}" dy="5" text-anchor="middle" fill="{c}" font-size="13" font-weight="700">{name}</text>
    <text x="{tx:.0f}" y="{ty:.0f}" text-anchor="{anchor}" fill="#A8BBD6" font-size="11.5">{sub}</text>
  </g>""".format(c=c, x=x, y=y, tx=tx, ty=ty, anchor=anchor, name=name, sub=sub))
    ring = 'M{:.0f} {:.0f} '.format(*pts[0]) + " ".join(
        "A{r} {r} 0 0 1 {:.0f} {:.0f}".format(*pts[(i+1) % 5], r=r) for i in range(5))
    return """<figure class="diagram reveal">
<svg viewBox="0 0 600 420" role="img" aria-label="The analyst loop: detect, triage, investigate, respond, improve">
  <path d="{ring}" fill="none" stroke="#1B3A66" stroke-width="8"/>
  <path d="{ring}" fill="none" stroke="#4FB8F0" stroke-width="2.5" class="flow" opacity=".85"/>
  <text x="{cx}" y="{cy}" dy="-6" text-anchor="middle" fill="#E6EEF8" font-size="15" font-weight="700">The analyst loop</text>
  <text x="{cx}" y="{cy}" dy="14" text-anchor="middle" fill="#7E93B5" font-size="11.5">every module feeds one step</text>{nodes}
</svg>
<figcaption>Modules 2–5 each own one step of this loop; Module 1 gives you the ground to stand on and Module 6 sharpens the verdict.</figcaption>
</figure>""".format(ring=ring, cx=cx, cy=cy, nodes="".join(out))

def deps_svg():
    rows = [("Windows &amp; Linux internals", 1, "Event IDs, Sysmon, log analysis", 2),
            ("Kerberos &amp; NTLM", 1, "4768 / 4769 / 4624 detections", 3),
            ("Wireshark &amp; protocols", 1, "Network attack detection", 3),
            ("Splunk &amp; Wazuh pipelines", 2, "Sigma → SPL / Wazuh conversion", 3),
            ("Detections you tuned", 3, "Hunting with your own coverage", 4),
            ("Triage &amp; case work", 2, "Incident response under pressure", 5),
            ("Evidence preservation", 5, "Memory &amp; artefact forensics", 5),
            ("IOC extraction", 4, "Malware triage verdicts", 6)]
    g = []
    for i, (a, ma, b, mb) in enumerate(rows):
        y = 34 + i*44
        g.append("""
  <g class="reveal in">
    <rect x="20" y="{y0}" width="300" height="32" rx="8" fill="{ca}" fill-opacity=".12" stroke="{ca}" stroke-width="1.5"/>
    <text x="34" y="{yt}" fill="#E6EEF8" font-size="12.5" font-weight="600">{a}</text>
    <path d="M330 {yc} H 400" stroke="#4FB8F0" stroke-width="2" class="flow" marker-end="url(#arr)"/>
    <rect x="410" y="{y0}" width="330" height="32" rx="8" fill="{cb}" fill-opacity=".12" stroke="{cb}" stroke-width="1.5"/>
    <text x="424" y="{yt}" fill="#E6EEF8" font-size="12.5" font-weight="600">{b}</text>
    <text x="760" y="{yt}" fill="#7E93B5" font-size="11" class="mono">M{ma} → M{mb}</text>
  </g>""".format(y0=y, yt=y+21, yc=y+16, a=a, b=b, ca=MOD_COLOR[ma], cb=MOD_COLOR[mb], ma=ma, mb=mb))
    return """<figure class="diagram reveal">
<svg viewBox="0 0 840 {h}" role="img" aria-label="What each later skill depends on">
  <defs><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
    <path d="M0 0L10 5L0 10z" fill="#4FB8F0"/></marker></defs>
  <text x="20" y="18" fill="#7E93B5" font-size="11" class="mono">YOU LEARN FIRST</text>
  <text x="410" y="18" fill="#7E93B5" font-size="11" class="mono">SO THAT LATER YOU CAN</text>{g}
</svg>
<figcaption>Nothing is taught twice and nothing arrives before what it needs — this is the order for a reason.</figcaption>
</figure>""".format(h=34 + len(rows)*44 + 6, g="".join(g))

MOD_TOOLS = {1: ["VMware", "Windows", "Linux", "PowerShell", "Bash", "Wireshark", "Event Viewer", "AD DS"],
             2: ["TheHive", "Sysmon", "Splunk", "Wazuh", "Sigma"],
             3: ["Atomic Red Team", "Nmap", "DVWA", "Suricata", "sigma-cli"],
             4: ["ATT&amp;CK Navigator", "D3FEND", "VirusTotal", "OTX", "MISP"],
             5: ["Wazuh active response", "PowerShell", "Volatility 3", "Autopsy"],
             6: ["strings", "PE viewer", "VirusTotal", "Sandbox report", "Sysmon"]}

def build_roadmap():
    secs = []
    for m, name, sub, hours, sess, labs, _blurb in MODULES:
        nodes = "\n".join("""    <div class="node"><span class="n">Topic {}</span>
      <h3>{}</h3><p>{}</p></div>""".format(i, tt, td) for i, (tt, td) in enumerate(TOPICS[m], 1))
        tools = "".join("<span>{}</span>".format(x) for x in MOD_TOOLS[m])
        secs.append("""<section class="wrap section" id="m{m}">
  <div class="sec-head sh-m{m} with-icon">{icon}<span class="tag m{m}">Module {m}</span><h2>{name}</h2>
    <span class="note">{hours} hours &middot; {sess} sessions &middot; {labs} labs &middot; 1 project</span></div>
  <p class="lead">{sub}</p>
  <div class="split">
    <div class="rail-list reveal">
{nodes}
    </div>
    <div>
      <div class="box box-lab reveal"><div class="box-title">Tools you meet here</div><div class="tool-band">{tools}</div></div>
      <div class="box box-take reveal"><div class="box-title">You leave able to</div>{outcome}</div>
    </div>
  </div>
</section>""".format(m=m, icon=icon(m), name=name, hours=hours, sess=sess, labs=labs, sub=sub,
                      nodes=nodes, tools=tools, outcome=MOD_OUTCOME[m]))
    body = """<main>
<section class="wrap hero">
  <span class="kicker">Curriculum</span>
  <h1>From foundations to incident response</h1>
  <p class="lead">Six modules, 35 topics, 79 labs. Each attack you learn is paired with the detection that
  catches it and its MITRE ATT&amp;CK technique — and nothing is taught twice.</p>
  <div class="cta-row"><a class="btn btn-primary" href="sessions.html">Open the sessions</a>
    <a class="btn" href="labs/index.html">See the labs</a></div>
  <div class="jump">
    <a href="#m1">01 Foundation</a><a href="#m2">02 SOC &amp; SIEM</a><a href="#m3">03 Detection</a>
    <a href="#m4">04 Hunting</a><a href="#m5">05 IR &amp; Forensics</a><a href="#m6">06 Malware</a>
  </div>
</section>

<section class="wrap section-sm">
  <div class="sec-head"><h2>The climb</h2><span class="note">one path, six modules, one job at the top</span></div>
{journey}
</section>

<section class="wrap section-sm">
  <div class="split">
    <div>
      <div class="sec-head"><h2>What an analyst actually does</h2></div>
      <p class="lead">Every alert goes round this loop. The diploma is built so that by the end you have done
      each step yourself, on real evidence, more than once.</p>
      <div class="box box-why"><div class="box-title">Why it matters</div>
      Most junior analysts can name the steps. Very few have <em>run</em> them under time pressure with a
      manager waiting for an answer. That is the gap this program closes.</div>
    </div>
{loop}
  </div>
</section>

<section class="wrap section-sm">
  <div class="sec-head"><h2>Why this order</h2><span class="note">each skill unlocks the next</span></div>
{deps}
</section>
{secs}
<section class="wrap section-sm">
  <div class="box box-note"><div class="box-title">Note</div>
  Every module ends with a project. Projects use fictional companies, documentation IP ranges and simulated
  attacks — no real malware and no real personal data.</div>
</section>
</main>""".format(journey=journey_svg(), loop=loop_svg(), deps=deps_svg(), secs="".join(secs))
    write("roadmap.html", layout("Curriculum — DGS Cyber Security Diploma",
        "Full curriculum of the DGS Academy Cyber Security Diploma — six modules, 35 topics, 79 labs, 6 projects.",
        "roadmap", "", body))

MOD_OUTCOME = {
 1: "Read a Windows event, a Linux log line and a packet capture and say what happened; explain how Kerberos and NTLM log a login; build and run your own lab.",
 2: "Triage an alert to a defensible verdict, open and close a case in TheHive, search both Splunk and Wazuh, and write one Sigma rule that runs on both.",
 3: "Simulate an endpoint, AD, network or web attack in the lab, find its evidence, write the detection that catches it, and tune it until it stays quiet on normal traffic.",
 4: "Turn a threat report into a hunt, map your coverage on ATT&amp;CK, enrich indicators with VirusTotal, OTX and MISP, and report what you found.",
 5: "Run an incident from first alert to lessons learned, collect evidence without destroying it, and pull the story out of a memory image and Windows artefacts.",
 6: "Give a safe static and behavioural verdict on a suspicious file, extract its indicators, and hand the SOC something it can block.",
}

# ----------------------------------------------------------------- labs
def build_labs():
    reg = (ROOT / "design/lab_register.md").read_text(encoding="utf-8")
    rows = re.findall(r'\| (LAB-L(\d\d)-[A-F]) \| L\d\d \| (.+?) \| (LIVE|TASK|SELF) \| (.+?) \| (.+?) \|', reg)
    kind = {"LIVE": ("Guided", "guided"), "TASK": ("Practical task", "task"), "SELF": ("Self-paced", "self")}
    buckets = {i: [] for i in range(1, 7)}
    for lid, ln, title, tag, tool, att in rows:
        n = int(ln)
        m = 1 if n <= 5 else 2 if n <= 9 else (2 if lid[-1] in "ABC" else 3) if n == 10 else \
            3 if n <= 13 else 4 if n <= 15 else 5 if n <= 17 else 6
        buckets[m].append((title, kind[tag], tool, att))
    total = sum(len(v) for v in buckets.values())
    assert total == 79, f"lab register must total 79, got {total}"

    secs = []
    for m, name, _sub, _h, _s, _l, _b in MODULES:
        def _cell_tool(v):
            return "&mdash;" if v.strip() == "\u2014" else v
        def _cell_att(v):
            return "&mdash;" if v.strip() == "\u2014" else '<span class="att">' + v + '</span>'
        trs = "\n".join(
            '      <tr><td>{}</td><td>{}</td><td><span class="pill {}">{}</span></td><td>{}</td><td>{}</td></tr>'
            .format(i, t, cls, label, _cell_tool(tool), _cell_att(att))
            for i, (t, (label, cls), tool, att) in enumerate(buckets[m], 1))
        secs.append(f"""<section class="wrap section-sm" id="m{m}">
  <div class="sec-head sh-m{m}"><span class="tag m{m}">Module {m}</span><h2>{name}</h2>
    <span class="note">{len(buckets[m])} labs</span></div>
  <div class="table-wrap"><table>
    <thead><tr><th>#</th><th>Lab</th><th>Format</th><th>Primary tool</th><th>ATT&amp;CK</th></tr></thead>
    <tbody>
{trs}
    </tbody></table></div>
</section>""")
    body = f"""<main>
<section class="wrap hero">
  <span class="kicker">Hands-on</span>
  <h1>79 practical labs</h1>
  <p class="lead">Every topic in the diploma is practised, not just explained. Labs run in your own local lab
  environment or against public training datasets — never against systems you do not own.</p>
</section>
<section class="wrap section-sm">
  <div class="stats">
    <div class="stat"><div class="n">79</div><div class="l">Labs</div></div>
    <div class="stat"><div class="n">36</div><div class="l">Guided in class</div></div>
    <div class="stat"><div class="n">6</div><div class="l">Lab machines</div></div>
    <div class="stat"><div class="n">100%</div><div class="l">Legal targets</div></div>
  </div>
  <div class="jump">
    <a href="#m1">01 Foundation</a><a href="#m2">02 SOC &amp; SIEM</a><a href="#m3">03 Detection</a>
    <a href="#m4">04 Hunting</a><a href="#m5">05 IR &amp; Forensics</a><a href="#m6">06 Malware</a>
  </div>
</section>
{"".join(secs)}
<section class="wrap section-sm">
  <div class="box box-lab"><div class="box-title">Lab files</div>
  Lab files, datasets and captures are published on this site with a SHA-256 hash, so you can verify what you
  downloaded before you open it.</div>
</section>
</main>"""
    write("labs/index.html", layout("Labs — DGS Cyber Security Diploma",
        "All 79 hands-on labs of the DGS Academy Cyber Security Diploma, grouped by module.",
        "labs", "../", body))

# ------------------------------------------------------------- projects
PROJECTS = [
 (1, "Foundation Investigation", "Individual &middot; written report",
  "Investigate a provided set of Windows, Linux and web evidence. Establish what happened, when, and what proves it."),
 (2, "SOC Triage Case Work", "Individual &middot; TheHive case",
  "Take five alerts from raw detection to closed case: triage, enrich, decide true or false positive, document the reasoning."),
 (3, "Detection Development", "Individual &middot; rule set + evidence",
  "Write, convert and test detections across both SIEM platforms, then prove each one fires on the attack and stays quiet otherwise."),
 (4, "Threat Hunting Investigation", "Individual &middot; hunt report",
  "Turn a published threat report into a hypothesis, hunt for it in real data, and report your findings and indicators."),
 (5, "Incident Investigation", "Individual &middot; incident report",
  "Work a full incident from first alert through containment to lessons learned, with a defensible timeline."),
 (6, "End-to-End Investigation", "Team &middot; report + presentation",
  "A staged multi-source attack: phishing, execution, lateral movement and exfiltration. Investigate it, detect it, present it."),
]

def build_projects():
    cards = "\n".join(f"""    <article class="card"><span class="rail m{m}-rail"></span>
      <span class="tag m{m}">{"Final" if m == 6 else f"Module {m}"}</span>
      <h3>{name}</h3><p class="meta">{meta}</p><p>{blurb}</p></article>"""
      for m, name, meta, blurb in PROJECTS)
    body = f"""<main>
<section class="wrap hero">
  <span class="kicker">Assessment</span>
  <h1>Six real projects</h1>
  <p class="lead">Each module ends with work you do yourself, on evidence you have not seen before, written
  up the way a security team would expect to receive it.</p>
</section>
<section class="wrap section-sm">
  <div class="grid">
{cards}
  </div>
</section>
<section class="wrap section">
  <div class="sec-head"><h2>How projects are marked</h2></div>
  <div class="table-wrap"><table>
    <thead><tr><th>Criterion</th><th>What is assessed</th></tr></thead><tbody>
    <tr><td>Method</td><td>A logical, repeatable approach — not guessing</td></tr>
    <tr><td>Findings</td><td>What actually happened, stated as fact</td></tr>
    <tr><td>Evidence</td><td>Every finding traced to a log line, packet or artefact</td></tr>
    <tr><td>Detection quality</td><td>Rules that fire on the attack and stay quiet on normal activity</td></tr>
    <tr><td>Communication</td><td>A report a manager can act on and an analyst can reproduce</td></tr>
    </tbody></table></div>
  <div class="box box-note" style="margin-top:20px"><div class="box-title">Note</div>
  Findings and interpretation stay separated in every report you write: what the evidence shows, then what
  you conclude from it. That habit is what makes an analyst trusted.</div>
</section>
</main>"""
    write("projects/index.html", layout("Projects — DGS Cyber Security Diploma",
        "The six real projects of the DGS Academy Cyber Security Diploma.", "projects", "../", body))

# ---------------------------------------------------------------- tools
def build_tools():
    stack = [("SIEM &amp; analytics", "Splunk &middot; Wazuh &middot; Sigma", "Module 2"),
             ("Case management", "TheHive", "Module 2"),
             ("Endpoint &amp; logs", "Sysmon &middot; Windows Event Viewer &middot; Linux audit logs &middot; journalctl", "Module 1"),
             ("Network analysis", "Wireshark &middot; tcpdump &middot; Nmap", "Module 1"),
             ("Detection frameworks", "MITRE ATT&amp;CK Navigator &middot; D3FEND &middot; Sigma", "Module 3"),
             ("Threat intelligence", "MISP &middot; AlienVault OTX &middot; VirusTotal", "Module 4"),
             ("Digital forensics", "Volatility 3 &middot; Autopsy", "Module 5"),
             ("Scripting &amp; automation", "PowerShell &middot; Bash &middot; Python", "Module 1")]
    vms = [("Windows workstation", "Victim endpoint with Sysmon and SIEM agents"),
           ("Ubuntu server", "Linux and web target"),
           ("Windows Server", "Active Directory domain controller"),
           ("SIEM server", "Wazuh and TheHive"),
           ("Splunk server", "Second SIEM for cross-platform work"),
           ("Attack machine", "Controlled attack simulation only")]
    t1 = "\n".join(f"    <tr><td>{c}</td><td>{t}</td><td>{w}</td></tr>" for c, t, w in stack)
    t2 = "\n".join(f"    <tr><td>{n}</td><td>{r}</td></tr>" for n, r in vms)
    body = f"""<main>
<section class="wrap hero">
  <span class="kicker">Tool stack</span>
  <h1>Tools you will master</h1>
  <p class="lead">Every tool here is used in at least one lab — nothing is mentioned and skipped.</p>
</section>
<section class="wrap section-sm">
  <div class="table-wrap"><table>
    <thead><tr><th>Category</th><th>Tools</th><th>First used</th></tr></thead><tbody>
{t1}
    </tbody></table></div>
</section>
<section class="wrap section">
  <div class="sec-head"><h2>Your lab environment</h2>
    <span class="note">Six machines on an isolated network</span></div>
  <div class="table-wrap"><table>
    <thead><tr><th>Machine</th><th>Role</th></tr></thead><tbody>
{t2}
    </tbody></table></div>
  <div class="box box-flag" style="margin-top:20px"><div class="box-title">Red flag</div>
  Every technique in this diploma is practised inside your own lab or on platforms that invite it. Scanning,
  testing or attacking anything else is illegal, and it ends your place on the program.</div>
</section>
</main>"""
    write("resources/tools.html", layout("Tools — DGS Cyber Security Diploma",
        "The tool stack and lab environment used across the DGS Academy Cyber Security Diploma.",
        "tools", "../", body))

# ------------------------------------------------------------- practice
def build_practice():
    plats = [("LetsDefend", "Blue team &middot; SOC simulation", "An alert queue close to a real SOC console — the best place to build triage speed.", "https://letsdefend.io"),
             ("Blue Team Labs Online", "Investigations &middot; challenges", "Investigation challenges with a marked answer path, so you learn where your reasoning broke.", "https://blueteamlabs.online"),
             ("CyberDefenders", "DFIR &middot; packet &amp; memory", "Real evidence sets for forensics and network investigation.", "https://cyberdefenders.org"),
             ("TryHackMe", "Guided rooms", "Start with Pre Security and Cyber Security 101, then SOC Level 1.", "https://tryhackme.com"),
             ("Splunk BOTS", "Public datasets", "Boss of the SOC datasets — the best free SPL practice there is.", None)]
    def _link(u):
        if not u:
            return ""
        return '<a class="more" href="' + u + '" rel="noopener">' + u.split("//")[1] + ' &rarr;</a>'
    cards = "\n".join(f"""    <article class="card"><span class="rail m{(i % 6) + 1}-rail"></span>
      <h3>{n}</h3><p class="meta">{sub}</p><p>{d}</p>
      {_link(u)}</article>"""
      for i, (n, sub, d, u) in enumerate(plats))
    certs = [("Foundation", "TryHackMe — Pre Security", "Free"), ("Foundation", "TryHackMe — Cyber Security 101", "Free"),
             ("Foundation", "TryHackMe — SOC Level 1", "Free path"), ("Foundation", "Cisco — Introduction to Cyber Security", "Free"),
             ("Foundation", "Cisco — Networking Basics", "Free"), ("Foundation", "Cisco — Endpoint Security", "Free"),
             ("Career growth", "CompTIA Security+", "Paid"), ("Career growth", "Microsoft SC-200", "Paid"),
             ("Career growth", "Blue Team Level 1 (BTL1)", "Paid")]
    rows = "\n".join(f"    <tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in certs)
    body = f"""<main>
<section class="wrap hero">
  <span class="kicker">Keep practising</span>
  <h1>Practice platforms &amp; next steps</h1>
  <p class="lead">Skill decays fast. These are the places to keep it sharp between sessions and after
  graduation.</p>
</section>
<section class="wrap section-sm">
  <div class="grid">
{cards}
  </div>
</section>
<section class="wrap section">
  <div class="sec-head"><h2>Recommended certifications</h2></div>
  <div class="table-wrap"><table>
    <thead><tr><th>Track</th><th>Certification</th><th>Cost</th></tr></thead><tbody>
{rows}
    </tbody></table></div>
  <div class="box box-analyst" style="margin-top:20px"><div class="box-title">Analyst view</div>
  Two solved investigations a week, written up properly, will do more for your first interview than any extra
  certificate.</div>
</section>
</main>"""
    write("resources/practice.html", layout("Practice — DGS Cyber Security Diploma",
        "Where to keep practising: platforms, free rooms and the certifications to aim for next.",
        "practice", "../", body))

# ------------------------------------------------------------- sessions
# (session number, module, title, [(module, topic index)], gate note)
SESSIONS = [
 (1,  1, "Security Foundations &amp; Windows Internals", [(1,1),(1,2)], ""),
 (2,  1, "Linux Fundamentals &amp; Scripting for Security Operations", [(1,2),(1,4)], ""),
 (3,  1, "Networking Fundamentals &amp; Protocol Analysis", [(1,3)], ""),
 (4,  1, "Active Directory &amp; Authentication", [(1,5)], ""),
 (5,  1, "Log Analysis, Web Technologies &amp; Attack Awareness", [(1,6),(1,7)], "Project 1 starts"),
 (6,  2, "SOC Operations, Alert Triage &amp; Incident Handling", [(2,1)], "Project 1 review"),
 (7,  2, "Log Analysis &amp; Event Correlation", [(2,2)], ""),
 (8,  2, "Splunk Investigation &amp; Detection Development", [(2,3)], ""),
 (9,  2, "Wazuh Deployment, Monitoring &amp; Detection", [(2,4)], "Project 2 starts"),
 (10, 2, "Sigma, Cross-SIEM Rules &amp; Detection Engineering", [(2,5),(3,1)], "Project 2 review"),
 (11, 3, "Endpoint &amp; Active Directory Attacks and Detection", [(3,2),(3,3)], ""),
 (12, 3, "Network &amp; Web Attacks and Detection", [(3,4),(3,5)], ""),
 (13, 3, "Detection Use Cases, Correlation &amp; Alert Tuning", [(3,6),(3,7)], "Project 3 starts"),
 (14, 4, "Threat Hunting Methodology, ATT&amp;CK &amp; Hunting Practice", [(4,1),(4,2),(4,3)], "Project 3 review"),
 (15, 4, "IOC Hunting, Threat Intelligence &amp; Enrichment", [(4,4),(4,5)], "Project 4 starts"),
 (16, 5, "Incident Response Lifecycle, Triage &amp; Live Response", [(5,1),(5,2),(5,3)], "Project 4 review"),
 (17, 5, "Memory Forensics &amp; Windows Forensic Artifacts", [(5,4),(5,5)], "Project 5 starts"),
 (18, 6, "Malware Triage — Static, Dynamic &amp; IOC Extraction", [(6,1),(6,2)], "Project 5 review &middot; final project"),
]

def _labs_by_session():
    reg = (ROOT / "design/lab_register.md").read_text(encoding="utf-8")
    rows = re.findall(r'\| LAB-L(\d\d)-([A-F]) \| L\d\d \| (.+?) \| (LIVE|TASK|SELF) \| (.+?) \| (.+?) \|', reg)
    kind = {"LIVE": ("Guided", "guided"), "TASK": ("Practical task", "task"), "SELF": ("Self-paced", "self")}
    out = {}
    for n, letter, title, tag, tool, att in rows:
        out.setdefault(int(n), []).append((letter, title, kind[tag], tool, att))
    return out

def _cell(v):
    return "&mdash;" if v.strip() == "—" else v

def build_sessions_index():
    cards = []
    for n, m, title, topics, gate in SESSIONS:
        cards.append(
            '    <a class="sess-card" href="session-{:02d}/index.html"><span class="rail m{}-rail"></span>'
            '<span class="num">{:02d}</span><span class="tag m{}">Module {}</span>'
            '<h3>{}</h3><p class="meta">{} topic{}{}</p></a>'.format(
                n, m, n, m, m, title, len(topics), "" if len(topics) == 1 else "s",
                " &middot; " + gate if gate else ""))
    body = """<main>
<section class="wrap hero">
  <span class="kicker">Sessions</span>
  <h1>Every session, in order</h1>
  <p class="lead">Each session page carries what you need for that class: the topics, the labs you will run,
  the evidence you will read and the task that follows. Sessions build on each other — nothing is taught
  twice, and nothing appears before what it depends on.</p>
</section>
<section class="wrap section-sm">
  <div class="sess-grid">
{}
  </div>
</section>
<section class="wrap section-sm">
  <div class="box box-note"><div class="box-title">Note</div>
  A session page is published once its material is built and reviewed. Files, datasets and captures are
  published with a SHA-256 hash so you can verify what you downloaded.</div>
</section>
</main>""".format("\n".join(cards))
    write("sessions.html", layout("Sessions — DGS Cyber Security Diploma",
        "All sessions of the DGS Academy Cyber Security Diploma, in teaching order.",
        "sessions", "", body))

def build_session_pages():
    labs = _labs_by_session()
    for idx, (n, m, title, topics, gate) in enumerate(SESSIONS):
        mod_name = [x[1] for x in MODULES if x[0] == m][0]
        blocks = []
        for i, (tm, ti) in enumerate(topics, 1):
            t_title, t_desc = TOPICS[tm][ti - 1]
            blocks.append("""    <div class="topic-block">
      <span class="t-no">Topic {}</span>
      <h3>{}</h3>
      <p>{}</p>
    </div>""".format(i, t_title, t_desc))
        rows = "\n".join(
            '      <tr><td>{}</td><td>{}</td><td><span class="pill {}">{}</span></td><td>{}</td><td>{}</td></tr>'
            .format(letter, lt, cls, label, _cell(tool),
                    _cell(att) if att.strip() == "—" else '<span class="att">' + att + '</span>')
            for letter, lt, (label, cls), tool, att in labs.get(n, []))
        labs_tbl = """  <div class="table-wrap"><table>
    <thead><tr><th>Lab</th><th>What you do</th><th>Format</th><th>Tool</th><th>ATT&amp;CK</th></tr></thead>
    <tbody>
{}
    </tbody></table></div>""".format(rows) if rows else ""
        prev_a = ('    <a class="prev" href="../session-{:02d}/index.html"><span>Previous</span>'
                  'Session {:02d}</a>'.format(SESSIONS[idx-1][0], SESSIONS[idx-1][0])) if idx > 0 else \
                 '    <a class="prev" href="../sessions.html"><span>Back to</span>All sessions</a>'
        next_a = ('    <a class="next" href="../session-{:02d}/index.html"><span>Next</span>'
                  'Session {:02d}</a>'.format(SESSIONS[idx+1][0], SESSIONS[idx+1][0])) if idx < len(SESSIONS)-1 else \
                 '    <a class="next" href="../projects/index.html"><span>Finish with</span>The final project</a>'
        gate_box = ('  <div class="box box-take"><div class="box-title">Project gate</div>{}</div>\n'
                    .format(gate)) if gate else ""
        body = """<main>
<section class="wrap hero">
  <div class="sess-hero">
    <span class="sess-no">{n:02d}</span>
    <div>
      <span class="kicker">Session {n:02d}</span>
      <h1>{title}</h1>
      <div class="sess-meta"><span class="tag m{m}">Module {m} &middot; {mod}</span>
        <span class="badge">{nt} topic{s}</span><span class="badge">{nl} labs</span></div>
    </div>
  </div>
</section>

<section class="wrap section-sm">
  <div class="sec-head sh-m{m}"><h2>What this session covers</h2></div>
{blocks}
</section>

<section class="wrap section-sm">
  <div class="sec-head sh-m{m}"><h2>Labs in this session</h2>
    <span class="note">Guided in class, then yours to finish</span></div>
{labs}
</section>

<section class="wrap section-sm">
{gate}  <div class="box box-lab"><div class="box-title">Session pack</div>
  The slides, lab guide, datasets and the practical task for this session are published here once the
  material is reviewed.</div>
  <div class="prevnext">
{prev}
{next}
  </div>
</section>
</main>""".format(n=n, title=title, m=m, mod=mod_name, nt=len(topics),
                  s="" if len(topics) == 1 else "s", nl=len(labs.get(n, [])),
                  blocks="\n".join(blocks), labs=labs_tbl, gate=gate_box,
                  prev=prev_a, next=next_a)
        write("session-{:02d}/index.html".format(n),
              layout("Session {:02d} — {} — DGS Cyber Security Diploma".format(n, re.sub("&[a-z]+;", "&", title)),
                     "Session {:02d} of the DGS Academy Cyber Security Diploma.".format(n),
                     "sessions", "../", body))

# ------------------------------------------------------------------ 404
def build_404():
    body = """<main>
<section class="wrap hero">
  <span class="kicker">404</span>
  <h1>That page is not here</h1>
  <p class="lead">The link is wrong, or the page has moved. Everything on the site is reachable from the
  curriculum.</p>
  <div class="cta-row"><a class="btn btn-primary" href="/dgs-cybersec-diploma/roadmap.html">Go to the curriculum</a>
    <a class="btn" href="/dgs-cybersec-diploma/index.html">Back to the home page</a></div>
</section>
</main>"""
    write("404.html", layout("Page not found — DGS Cyber Security Diploma",
        "That page does not exist on the DGS Academy Cyber Security Diploma site.", "", "/dgs-cybersec-diploma/", body))


if __name__ == "__main__":
    print("building docs/ ...")
    build_home(); build_roadmap(); build_labs(); build_projects(); build_tools(); build_practice()
    build_sessions_index(); build_session_pages(); build_404()
    print("done.")
