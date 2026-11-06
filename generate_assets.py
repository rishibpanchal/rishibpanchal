"""Builds the animated profile README assets. Edit CONFIG, run `python generate_assets.py`."""
import os, base64, textwrap
from xml.sax.saxutils import escape as e

# Palette pulled from the character art: Night Fury black, eye green, leather, ember red
P = dict(bg="#07090a", line="#9fc356", green="#a9d05a", leather="#d39a52",
         ember="#e4572e", text="#f1f3e8", muted="#98a48c", chip="#dfe8c8")
FONT = "Manrope, 'Segoe UI', Helvetica, Arial, sans-serif"
W = 860
PROFILE = "https://github.com/rishibpanchal"

CONFIG = {
    "name": "Rishi Panchal",
    "tagline": "Systems, Concurrency, and State",
    "intro": "Concurrent, auditable, verifiable backend and AI systems.",
    "character": "src/character.png",
    "projects": [
        dict(name="WealthOps", sub="AI-Powered Wealth Management Operations Platform",
             url="https://github.com/rishibpanchal/WealthOps",
             desc="Turns plain-language requests into auditable workflows: a LangGraph planner, policy RAG, deterministic guardrails and a human approval queue.",
             stat="100% unauthorized-action blocking across 50 test scenarios",
             tags=["FastAPI", "LangGraph", "React", "TypeScript"]),
        dict(name="TransactX", sub="Enterprise Banking Core and ATM Simulator",
             url="https://github.com/rishibpanchal/TransactX",
             desc="ACID transfers, ordered-lock deadlock prevention, an immutable double-entry ledger, and a sandbox comparing optimistic and pessimistic locking.",
             stat="Pessimistic locks: 100% success vs ~15-25% optimistic at 50 concurrent transfers",
             tags=["Spring Boot", "JWT", "PostgreSQL", "Redis", "React"]),
        dict(name="QuantScope", sub="Quantitative Trading and Analytics Platform",
             url="https://github.com/rishibpanchal/QuantScope",
             desc="Market analytics, signal discovery, VaR and efficient-frontier portfolio tools, strategy backtesting, news sentiment and an AI copilot.",
             stat="Falls back to synthetic price data when the market feed is down",
             tags=["React", "TypeScript", "FastAPI", "Pandas", "TradingView Charts"]),
        dict(name="RecycleIT", sub="Circular Supply-Chain and Traceability Platform",
             url="https://github.com/rishibpanchal/RecycleIT",
             desc="AI proposes, deterministic code validates: mass-balance checks, a KùzuDB traceability graph, anomaly detection, LCA metrics and a SHA-256 audit ledger.",
             stat="KùzuDB runs deep impact traversals 9.6x faster than SQLite",
             tags=["Next.js", "FastAPI", "KùzuDB", "NetworkX"]),
    ],
    "principles": [
        ("AI proposes, code decides", "Models plan and explain. Guardrails and calculators do the arithmetic."),
        ("Ordered locks", "Accounts lock in a fixed order, so concurrent transfers cannot deadlock."),
        ("Verifiable history", "SHA-256 hash chains make any edit to the ledger detectable."),
        ("Measured, not claimed", "Benchmarks and evaluation suites back every performance claim."),
    ],
    "stack": [
        ("Languages & Runtimes", [
            ("Java 21", "java"),
            ("Python", "python"),
            ("TypeScript", "typescript"),
            ("C / C++", "cpp"),
            ("SQL", "sql"),
        ]),
        ("Backend & Frameworks", [
            ("Spring Boot", "spring"),
            ("FastAPI", "fastapi"),
            ("React", "react"),
            ("Next.js", "nextjs"),
            ("Node.js", "nodejs"),
        ]),
        ("Storage & State", [
            ("PostgreSQL", "postgres"),
            ("Redis", "redis"),
            ("KùzuDB Graph", "kuzudb"),
            ("SQLite", "sqlite"),
        ]),
        ("AI & Systems Engineering", [
            ("LangGraph", "langgraph"),
            ("Project Loom", "loom"),
            ("NumPy / Pandas", "pandas"),
            ("Docker", "docker"),
            ("Git", "git"),
        ]),
    ],
    "links": [("GitHub", PROFILE), ("LinkedIn", "https://linkedin.com/in/rishii-panchal"),
              ("Email", "mailto:rishibpanchal006@gmail.com")],
}

def rg(i, c, a):
    return ('<radialGradient id="%s" cx="50%%" cy="50%%" r="50%%"><stop offset="0" stop-color="%s" stop-opacity="%s"/>'
            '<stop offset=".45" stop-color="%s" stop-opacity="%s"/><stop offset=".72" stop-color="%s" stop-opacity="0"/></radialGradient>'
            % (i, c, a, c, float(a) * .4, c))

DEFS = ("<defs>" + rg("gf", "#1f8a5a", ".55") + rg("go", "#7da82f", ".34") + rg("ga", "#d39a52", ".30")
        + rg("f1", "#e4572e", ".6") + rg("f2", "#ffb04a", ".5")
        + '<linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a9d05a"/><stop offset="1" stop-color="#d39a52"/></linearGradient></defs>')

STYLE = """<style>
.t{font-family:%s}
@keyframes a{0%%,100%%{transform:translateX(0);opacity:.8}50%%{transform:translateX(300px);opacity:1}}
@keyframes b{0%%,100%%{transform:translateX(0);opacity:.7}50%%{transform:translateX(-230px);opacity:1}}
@keyframes p{0%%,100%%{transform:scale(1);opacity:.75}50%%{transform:scale(1.14);opacity:1}}
@keyframes up{0%%{transform:translate(0,0) scale(1);opacity:0}20%%{opacity:1}80%%{opacity:1}100%%{transform:translate(-16px,-80px) scale(.4);opacity:0}}
@keyframes fl{0%%,100%%{transform:translateY(0)}50%%{transform:translateY(-7px)}}
.g1{animation:a 10s ease-in-out infinite}.g2{animation:b 13s ease-in-out infinite}.g3{animation:a 15s ease-in-out infinite reverse}
.fire{transform-origin:700px 150px;animation:p 4s ease-in-out infinite}
.e1{animation:up 3s ease-in infinite}.e2{animation:up 4s ease-in 1s infinite}.e3{animation:up 2.6s ease-in 2s infinite}
.char{animation:fl 6s ease-in-out infinite}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>""" % FONT

def svg(h, body, fire=False, shift=0):
    g = ('<ellipse class="g1" cx="150" cy="%d" rx="270" ry="170" fill="url(#gf)"/>'
         '<ellipse class="g2" cx="420" cy="%d" rx="230" ry="140" fill="url(#go)"/>'
         '<ellipse class="g3" cx="600" cy="%d" rx="170" ry="110" fill="url(#ga)"/>') % (h + 30, h + 30, h + 40)
    if fire:
        g += ('<ellipse class="fire" cx="700" cy="150" rx="270" ry="220" fill="url(#f1)"/>'
              '<ellipse class="fire" cx="670" cy="190" rx="200" ry="160" fill="url(#f2)"/>')
        for i, (x, y, r) in enumerate([(560, 235, 6), (610, 245, 8), (700, 250, 7), (540, 215, 6), (790, 245, 7)]):
            g += '<circle class="e%d" cx="%d" cy="%d" r="%d" fill="url(#f%d)"/>' % (i % 3 + 1, x, y, r, i % 2 + 1)
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">%s%s'
            '<clipPath id="cp"><rect width="%d" height="%d" rx="16"/></clipPath>'
            '<rect width="%d" height="%d" rx="16" fill="%s"/><g clip-path="url(#cp)"><g transform="translate(%d,0)">%s</g></g>'
            '<rect x=".5" y=".5" width="%d" height="%d" rx="16" fill="none" stroke="%s" stroke-opacity=".25"/>%s</svg>'
            % (W, h, W, h, STYLE, DEFS, W, h, W, h, P["bg"], shift, g, W - 1, h - 1, P["line"], body))

def text(x, y, s, size, fill=None, weight=700, anchor="start", extra=""):
    return '<text class="t" x="%s" y="%s" font-size="%s" font-weight="%s" fill="%s" text-anchor="%s" %s>%s</text>' % (
        x, y, size, weight, fill or P["text"], anchor, extra, e(s))

def chips(x, y, items, maxx, size=12.5):
    out, cx, cy = "", x, y
    for s in items:
        w = round(22 + size * 0.6 * len(s))
        if cx + w > maxx:
            cx, cy = x, cy + 34
        out += ('<rect x="%d" y="%d" width="%d" height="26" rx="13" fill="%s" fill-opacity=".1" stroke="%s" stroke-opacity=".4"/>'
                % (cx, cy, w, P["green"], P["green"]) + text(cx + w / 2, cy + 17.5, s, size, P["chip"], 600, "middle"))
        cx += w + 8
    return out, cy + 26

def write(name, content):
    os.makedirs("assets", exist_ok=True)
    open("assets/" + name, "w", encoding="utf-8").write(content)

def hero():
    c = CONFIG
    body = (text(48, 120, c["name"], 58, extra='letter-spacing="-1"')
            + text(50, 160, c["tagline"], 22, P["green"], 600)
            + text(50, 192, c["intro"], 14.5, P["muted"], 500))
    img = c["character"]
    if img and os.path.exists(img):
        import struct
        with open(img, "rb") as f:
            png_bytes = f.read(24)
        w, h = struct.unpack(">II", png_bytes[16:24])
        ch = 270; cw = round(ch * w / h)
        b64 = base64.b64encode(open(img, "rb").read()).decode()
        body += '<image class="char" x="%d" y="6" width="%d" height="%d" href="data:image/png;base64,%s"/>' % (W - cw - 24, cw, ch, b64)
    write("hero.svg", svg(260, body, fire=True))

def cards():
    for i, p in enumerate(CONFIG["projects"]):
        lines = textwrap.wrap(p["desc"], 88)
        body = ('<rect x="30" y="30" width="4" height="150" rx="2" fill="url(#bar)"/>'
                + text(56, 56, p["name"], 25, extra='letter-spacing="-.3"')
                + text(W - 40, 54, "View repository", 13.5, P["green"], 600, "end")
                + text(56, 80, p["sub"], 14.5, P["leather"], 600))
        y = 110
        for ln in lines:
            body += text(56, y, ln, 13.5, "#c9d2bd", 500); y += 21
        body += ('<circle cx="60" cy="%d" r="3.5" fill="%s"/>' % (y + 6, P["ember"]) + text(72, y + 10, p["stat"], 13, "#f0b987", 600))
        cb, bottom = chips(56, y + 28, p["tags"], W - 40)
        write("card_%s.svg" % p["name"].lower(), svg(bottom + 26, body + cb, shift=(i * 190) % 560 - 200))

def principles():
    body, x = text(48, 54, "Working principles", 22), 36
    for t, d in CONFIG["principles"]:
        body += '<rect x="%d" y="80" width="188" height="124" rx="12" fill="%s" fill-opacity=".07" stroke="%s" stroke-opacity=".3"/>' % (x, P["green"], P["green"])
        body += '<rect x="%d" y="96" width="3" height="18" rx="1.5" fill="%s"/>' % (x + 14, P["leather"])
        for j, ln in enumerate(textwrap.wrap(t, 20)):
            body += text(x + 24, 110 + j * 18, ln, 14.5)
        n = len(textwrap.wrap(t, 20))
        for j, ln in enumerate(textwrap.wrap(d, 26)):
            body += text(x + 14, 112 + n * 18 + 10 + j * 16, ln, 12, P["muted"], 500)
        x += 200
    write("principles.svg", svg(232, body))

ICONS = {
    "java": '<path d="M2.5 5.5h8a2.5 2.5 0 0 1-2.5 5H5a2.5 2.5 0 0 1-2.5-5z" fill="none" stroke="#a9d05a" stroke-width="1.3"/><path d="M10.5 6.5h1.5a1.2 1.2 0 0 1 0 2.4h-1.5" fill="none" stroke="#a9d05a" stroke-width="1.2"/><path d="M5 1.5c-.4.8.2 1.3-.2 2.2 M8 1.5c-.4.8.2 1.3-.2 2.2" fill="none" stroke="#d39a52" stroke-width="1.2" stroke-linecap="round"/>',
    "python": '<path d="M7.8 1H4.2A2.2 2.2 0 0 0 2 3.2V5h4v1H1.5A1.5 1.5 0 0 0 0 7.5v2A2.2 2.2 0 0 0 2.2 11.7H3.5V10a1.5 1.5 0 0 1 1.5-1.5h3A1.5 1.5 0 0 0 9.5 7V3.5A2.5 2.5 0 0 0 7.8 1z" fill="#a9d05a"/><circle cx="3.8" cy="2.5" r=".7" fill="#07090a"/><path d="M8.2 15h3.6a2.2 2.2 0 0 0 2.2-2.2V11h-4v-1h4.5A1.5 1.5 0 0 0 16 8.5v-2a2.2 2.2 0 0 0-2.2-2.2H12.5V6a1.5 1.5 0 0 1-1.5 1.5h-3A1.5 1.5 0 0 0 6.5 9v3.5a2.5 2.5 0 0 0 1.7 2.5z" fill="#d39a52"/><circle cx="12.2" cy="13.5" r=".7" fill="#07090a"/>',
    "typescript": '<rect x="1" y="1" width="14" height="14" rx="3" fill="#a9d05a" fill-opacity=".15" stroke="#a9d05a" stroke-width="1.1"/><path d="M3 5.5h4.5 M5.25 5.5v6" stroke="#a9d05a" stroke-width="1.3" stroke-linecap="round"/><path d="M9 11.5c.5.3 1.2.4 1.8.4 1.2 0 1.7-.5 1.7-1.1 0-1.4-3.3-.8-3.3-2.7 0-1 .9-1.6 2.1-1.6.6 0 1.2.1 1.6.3 M9.5 9.5c.3.2.7.3 1.1.3" fill="none" stroke="#d39a52" stroke-width="1.2" stroke-linecap="round"/>',
    "cpp": '<polygon points="8,1 15,5 15,11 8,15 1,11 1,5" fill="none" stroke="#a9d05a" stroke-width="1.2"/><path d="M6.5 6.5a2 2 0 1 0 0 3" fill="none" stroke="#d39a52" stroke-width="1.2" stroke-linecap="round"/><path d="M10 8h2.5 M11.25 6.75v2.5 M13.5 8h2 M14.5 7v2" stroke="#a9d05a" stroke-width="1" stroke-linecap="round"/>',
    "sql": '<ellipse cx="8" cy="4" rx="5.5" ry="2" fill="none" stroke="#a9d05a" stroke-width="1.2"/><path d="M2.5 4v3.5c0 1.1 2.5 2 5.5 2s5.5-.9 5.5-2V4" fill="none" stroke="#d39a52" stroke-width="1.2"/><path d="M2.5 7.5v3.5c0 1.1 2.5 2 5.5 2s5.5-.9 5.5-2V7.5" fill="none" stroke="#a9d05a" stroke-width="1.2"/>',
    "spring": '<path d="M14 2c-6.5 0-11.5 4.5-11.5 11 6.5 0 11.5-4.5 11.5-11z" fill="none" stroke="#a9d05a" stroke-width="1.3"/><path d="M2.5 13c3-3 6.5-5 11.5-11" fill="none" stroke="#d39a52" stroke-width="1.2"/><circle cx="9" cy="6.5" r="1.2" fill="#a9d05a"/>',
    "fastapi": '<circle cx="8" cy="8" r="6.8" fill="none" stroke="#a9d05a" stroke-width="1.2"/><path d="M8.5 2.5L5 8.5h3.2L7.5 13.5 12 7.5H8.8z" fill="#d39a52"/>',
    "react": '<circle cx="8" cy="8" r="1.5" fill="#a9d05a"/><ellipse cx="8" cy="8" rx="6.5" ry="2.4" fill="none" stroke="#a9d05a" stroke-width="1"/><ellipse cx="8" cy="8" rx="6.5" ry="2.4" transform="rotate(60 8 8)" fill="none" stroke="#d39a52" stroke-width="1"/><ellipse cx="8" cy="8" rx="6.5" ry="2.4" transform="rotate(120 8 8)" fill="none" stroke="#a9d05a" stroke-width="1"/>',
    "nextjs": '<circle cx="8" cy="8" r="6.8" fill="none" stroke="#a9d05a" stroke-width="1.2"/><path d="M5.5 11.5V4.5l5.5 7 M10.5 4.5v3.5" fill="none" stroke="#d39a52" stroke-width="1.2" stroke-linecap="round"/>',
    "nodejs": '<polygon points="8,1.5 14,5 14,11 8,14.5 2,11 2,5" fill="none" stroke="#a9d05a" stroke-width="1.2"/><path d="M5.5 11V5l5 6V5" fill="none" stroke="#d39a52" stroke-width="1.2" stroke-linecap="round"/>',
    "postgres": '<path d="M12.5 4.5a3.5 3.5 0 0 0-6 1.8c-1.2 0-2.5 1-2.5 2.7 0 1.5.8 2.5 2 2.8L5.5 14h1.8l-.3-2.2c.4 0 .7-.1 1.2-.4V14h1.8v-3c1-.5 1.8-1.5 1.8-2.8V4.5z" fill="none" stroke="#a9d05a" stroke-width="1.2"/><circle cx="9" cy="6" r=".8" fill="#d39a52"/>',
    "redis": '<path d="M8 1.5l5.5 3v6.5L8 14 2.5 11V4.5z" fill="none" stroke="#a9d05a" stroke-width="1.2"/><path d="M8 1.5v12.5 M2.5 4.5L8 7.5l5.5-3" fill="none" stroke="#d39a52" stroke-width="1.1"/>',
    "kuzudb": '<line x1="4" y1="12" x2="8" y2="4" stroke="#d39a52" stroke-width="1.2"/><line x1="8" y1="4" x2="12.5" y2="10" stroke="#d39a52" stroke-width="1.2"/><line x1="4" y1="12" x2="12.5" y2="10" stroke="#d39a52" stroke-width="1.2"/><circle cx="8" cy="4" r="2.2" fill="#a9d05a"/><circle cx="4" cy="12" r="2.2" fill="#a9d05a"/><circle cx="12.5" cy="10" r="2.2" fill="#e4572e"/>',
    "sqlite": '<path d="M3 13C3 7 7 3 13 3c0 6-4 10-10 10z" fill="none" stroke="#a9d05a" stroke-width="1.2"/><line x1="3" y1="13" x2="9" y2="7" stroke="#d39a52" stroke-width="1.2"/><path d="M6 7l2 2 M8 5l2 2" stroke="#a9d05a" stroke-width="1"/>',
    "langgraph": '<rect x="1" y="6" width="3.8" height="3.8" rx="1" fill="#a9d05a"/><rect x="11" y="2" width="3.8" height="3.8" rx="1" fill="#d39a52"/><rect x="11" y="10" width="3.8" height="3.8" rx="1" fill="#e4572e"/><path d="M4.8 8h2c1 0 1.8-.8 1.8-1.8V4h2.4 M6.8 8c0 1 .8 1.8 1.8 1.8v2.2h2.4" fill="none" stroke="#dfe8c8" stroke-width="1.1"/>',
    "loom": '<path d="M1 4c3.5 0 4.5 4 7 4s3.5-4 7-4" fill="none" stroke="#a9d05a" stroke-width="1.3" stroke-linecap="round"/><path d="M1 8c3.5 0 4.5 4 7 4s3.5-4 7-4" fill="none" stroke="#d39a52" stroke-width="1.3" stroke-linecap="round"/><path d="M1 12c3.5 0 4.5 4 7 4s3.5-4 7-4" fill="none" stroke="#e4572e" stroke-width="1.3" stroke-linecap="round"/>',
    "pandas": '<rect x="2" y="2" width="12" height="12" rx="2" fill="none" stroke="#a9d05a" stroke-width="1.2"/><line x1="6" y1="2" x2="6" y2="14" stroke="#d39a52" stroke-width="1"/><line x1="10" y1="2" x2="10" y2="14" stroke="#d39a52" stroke-width="1"/><line x1="2" y1="6" x2="14" y2="6" stroke="#d39a52" stroke-width="1"/><line x1="2" y1="10" x2="14" y2="10" stroke="#d39a52" stroke-width="1"/>',
    "docker": '<path d="M1 9.5c.5-1 2-1 3-1h8c2 0 3.5 1 3.5 2.5 0 2-2 3.5-5 3.5H4C2 14.5 1 12.5 1 9.5z" fill="none" stroke="#a9d05a" stroke-width="1.2"/><rect x="4" y="6" width="2" height="2" fill="#d39a52"/><rect x="6.5" y="6" width="2" height="2" fill="#d39a52"/><rect x="9" y="6" width="2" height="2" fill="#d39a52"/><rect x="6.5" y="3.5" width="2" height="2" fill="#d39a52"/>',
    "git": '<circle cx="4" cy="4" r="1.8" fill="#a9d05a"/><circle cx="4" cy="12" r="1.8" fill="#a9d05a"/><circle cx="12" cy="7" r="1.8" fill="#e4572e"/><line x1="4" y1="4" x2="4" y2="12" stroke="#a9d05a" stroke-width="1.2"/><path d="M4 10c2.5 0 4.5-1.5 6-2.5l2-.5" fill="none" stroke="#d39a52" stroke-width="1.2"/>',
}

def stack():
    body = (text(48, 50, "Technical Stack", 22, weight=800)
            + text(48, 74, "Categorized engineering toolchain and runtime ecosystems", 13.5, P["muted"], 500)
            + '<line x1="48" y1="92" x2="812" y2="92" stroke="%s" stroke-opacity=".18" stroke-dasharray="4 4"/>' % P["line"])
    y = 116
    for cat_title, items in CONFIG["stack"]:
        body += ('<rect x="48" y="%d" width="3" height="13" rx="1.5" fill="%s"/>' % (y, P["leather"])
                 + text(58, y + 11, cat_title.upper(), 11, P["leather"], weight=700, extra='letter-spacing="1.2"'))
        cy = y + 20
        cx, maxx, row_h = 48, W - 48, 30
        for name, icon_key in items:
            text_w = round(len(name) * 7.8)
            w = 32 + text_w + 12
            if cx + w > maxx:
                cx = 48
                cy += row_h + 8
            body += ('<rect x="%d" y="%d" width="%d" height="%d" rx="15" fill="%s" fill-opacity=".09" stroke="%s" stroke-opacity=".38"/>'
                     % (cx, cy, w, row_h, P["green"], P["green"]))
            if icon_key in ICONS:
                body += '<g transform="translate(%d,%d)">%s</g>' % (cx + 9, cy + 7, ICONS[icon_key])
            body += text(cx + 30, cy + 19.5, name, 12.5, P["chip"], weight=600, anchor="start")
            cx += w + 8
        y = cy + row_h + 20
    write("stack.svg", svg(y + 8, body))

def footer():
    write("footer.svg", svg(110, text(48, 62, "Get in touch", 24) + text(48, 90, "Open a repository, or send a message.", 14, P["muted"], 500)))
    for label, _ in CONFIG["links"]:
        w = 44 + 11 * len(label)
        write("btn_%s.svg" % label.lower(),
              '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="42" viewBox="0 0 %d 42">%s<rect x="1" y="1" width="%d" height="40" rx="20" fill="%s" fill-opacity=".12" stroke="%s" stroke-opacity=".55"/>%s</svg>'
              % (w, w, STYLE, w - 2, P["green"], P["green"], text(w / 2, 26, label, 14, P["text"], 700, "middle")))

RAW_ASSETS = "https://raw.githubusercontent.com/rishibpanchal/rishibpanchal/main/assets"

def readme():
    base = RAW_ASSETS
    img = lambda f, alt, u=PROFILE: '<a href="%s"><img src="%s/%s" alt="%s" width="100%%"/></a>' % (u, base, f, alt)
    L = ['<div align="center">', '', img("hero.svg", CONFIG["name"]), '']
    for p in CONFIG["projects"]:
        L += [img("card_%s.svg" % p["name"].lower(), "%s - %s" % (p["name"], p["sub"]), p["url"]), '']
    L += [img("principles.svg", "Working principles"), '', img("stack.svg", "Stack"), '', img("footer.svg", "Get in touch"), '']
    L += ['  '.join('<a href="%s"><img src="%s/btn_%s.svg" alt="%s"/></a>' % (u, base, l.lower(), l) for l, u in CONFIG["links"]), '', '</div>', '']
    open("README.md", "w", encoding="utf-8").write("\n".join(L))

if __name__ == "__main__":
    hero(); cards(); principles(); stack(); footer(); readme(); print("done")
