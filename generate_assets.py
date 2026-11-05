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
        dict(name="ApexLedger", sub="Asynchronous Trade Settlement and Financial Engine",
             url="https://github.com/rishibpanchal/ApexLedger",
             desc="Double-entry settlement on Java virtual threads, with pessimistic locking, ordered-lock deadlock prevention and a SHA-256 tamper-evident ledger.",
             stat="Account balances audit to exactly $20,000,000 under live load",
             tags=["Java 21", "Spring Boot 3", "PostgreSQL", "Docker"]),
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
    "stack": ["Java", "Spring Boot", "Python", "FastAPI", "TypeScript", "React", "Next.js", "PostgreSQL",
              "Redis", "KùzuDB", "LangGraph", "Docker"],
    "links": [("GitHub", PROFILE), ("LinkedIn", "https://linkedin.com/in/rishi-panchal"),
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

def stack():
    cb, bottom = chips(48, 78, CONFIG["stack"], W - 48, 13.5)
    write("stack.svg", svg(bottom + 30, text(48, 52, "Stack", 22) + cb))

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
