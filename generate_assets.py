"""Generates the animated SVG assets for the profile README.
Edit CONFIG, run `python generate_assets.py`, commit the assets/ folder."""
import os, base64
from xml.sax.saxutils import escape as e

CONFIG = {
    "name": "Rishi Panchal",
    "tagline": "Systems, Concurrency, and State",
    # (title, subtitle, repo url, optional one-line description)
    "projects": [
        ("ApexLedger", "Financial Concurrency Engine", "https://github.com/rishibpanchal/ApexLedger", ""),
        ("WealthOps", "Governed AI Operations Platform", "https://github.com/rishibpanchal/WealthOps", ""),
        ("TransactX", "Transaction Isolation Sandbox", "https://github.com/rishibpanchal/TransactX", ""),
        ("QuantScope", "Quantitative Risk Terminal", "https://github.com/rishibpanchal/QuantScope", ""),
        ("RecycleIT", "Provenance Graph Engine", "https://github.com/rishibpanchal/RecycleIT", ""),
    ],
    "principles": ["Concurrency", "Isolation", "Provenance", "Governance", "Risk"],
    "character": "src/character.png",  # transparent PNG shown in the hero; set to None to remove
    "base_url": "https://raw.githubusercontent.com/rishibpanchal/rishibpanchal/main/assets",
    "links": [
        ("GitHub", "https://github.com/rishibpanchal"),
        ("LinkedIn", "https://linkedin.com/in/rishi-panchal"),
        ("Email", "mailto:rishibpanchal006@gmail.com"),
    ],
}

FONT = "Manrope, 'Segoe UI', Helvetica, Arial, sans-serif"
W = 860

DEFS = """
<defs>
  <radialGradient id="v" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#6e14d2" stop-opacity=".72"/><stop offset=".4" stop-color="#5a0fb4" stop-opacity=".35"/><stop offset=".7" stop-color="#5a0fb4" stop-opacity="0"/></radialGradient>
  <radialGradient id="b" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#283cff" stop-opacity=".6"/><stop offset=".45" stop-color="#1e32c8" stop-opacity=".25"/><stop offset=".7" stop-color="#1e32c8" stop-opacity="0"/></radialGradient>
  <radialGradient id="c" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#00bee6" stop-opacity=".34"/><stop offset=".7" stop-color="#00bee6" stop-opacity="0"/></radialGradient>
  <radialGradient id="f1" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#ff6400" stop-opacity=".6"/><stop offset=".4" stop-color="#ff3200" stop-opacity=".2"/><stop offset=".7" stop-color="#ff0000" stop-opacity="0"/></radialGradient>
  <radialGradient id="f2" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#ffb400" stop-opacity=".5"/><stop offset=".4" stop-color="#ff5000" stop-opacity=".15"/><stop offset=".7" stop-color="#ff0000" stop-opacity="0"/></radialGradient>
  <linearGradient id="bar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a3cff"/><stop offset="1" stop-color="#2a8cff"/></linearGradient>
</defs>"""

STYLE = """
<style>
.t{font-family:%s}
@keyframes a{0%%,100%%{transform:translateX(0);opacity:.8}50%%{transform:translateX(320px);opacity:1}}
@keyframes b{0%%,100%%{transform:translateX(0);opacity:.7}50%%{transform:translateX(-240px);opacity:1}}
@keyframes p{0%%,100%%{transform:scale(1);opacity:.75}50%%{transform:scale(1.15);opacity:1}}
@keyframes up{0%%{transform:translate(0,0) scale(1);opacity:0}20%%{opacity:1}80%%{opacity:1}100%%{transform:translate(-20px,-70px) scale(.4);opacity:0}}
@keyframes blink{0%%,100%%{opacity:1}50%%{opacity:.25}}
.g1{animation:a 9s ease-in-out infinite}.g2{animation:b 12s ease-in-out infinite}
.g3{animation:a 14s ease-in-out infinite reverse}.fire{transform-origin:740px 100px;animation:p 4s ease-in-out infinite}
.e1{animation:up 3s ease-in infinite}.e2{animation:up 4s ease-in 1s infinite}.e3{animation:up 2.6s ease-in 2s infinite}
.char{animation:fl 6s ease-in-out infinite}
@keyframes fl{0%%,100%%{transform:translateY(0)}50%%{transform:translateY(-8px)}}
.dot{animation:blink 1.8s ease-in-out infinite}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>""" % FONT


def svg(h, body, glow=True, fire=False):
    g = ""
    if glow:
        g += '<ellipse class="g1" cx="160" cy="%d" rx="260" ry="190" fill="url(#v)"/>' % (h + 30)
        g += '<ellipse class="g2" cx="400" cy="%d" rx="220" ry="150" fill="url(#b)"/>' % (h + 30)
        g += '<ellipse class="g3" cx="560" cy="%d" rx="170" ry="120" fill="url(#c)"/>' % (h + 40)
    if fire:
        g += '<ellipse class="fire" cx="740" cy="100" rx="220" ry="200" fill="url(#f1)"/>'
        g += '<ellipse class="fire" cx="690" cy="140" rx="170" ry="150" fill="url(#f2)"/>'
        for i, (x, y, r) in enumerate([(630, 175, 6), (700, 190, 8), (760, 170, 7), (660, 200, 6), (820, 180, 7)]):
            g += '<circle class="e%d" cx="%d" cy="%d" r="%d" fill="url(#f%d)"/>' % (i % 3 + 1, x, y, r, i % 2 + 1)
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">%s%s'
            '<clipPath id="cp"><rect width="%d" height="%d" rx="16"/></clipPath>'
            '<rect width="%d" height="%d" rx="16" fill="#08080c"/><g clip-path="url(#cp)">%s</g>'
            '<rect x=".5" y=".5" width="%d" height="%d" rx="16" fill="none" stroke="#6e50dc" stroke-opacity=".28"/>'
            '%s</svg>') % (W, h, W, h, STYLE, DEFS, W, h, W, h, g, W - 1, h - 1, body)


def text(x, y, s, size, fill="#f2f0ff", weight=700, anchor="start", extra=""):
    return '<text class="t" x="%s" y="%s" font-size="%s" font-weight="%s" fill="%s" text-anchor="%s" %s>%s</text>' % (
        x, y, size, weight, fill, anchor, extra, e(s))


def write(name, content):
    os.makedirs("assets", exist_ok=True)
    with open("assets/" + name, "w", encoding="utf-8") as f:
        f.write(content)


def hero():
    c = CONFIG
    body = (text(48, 100, c["name"], 52, weight=800, extra='letter-spacing="-1"')
            + text(50, 140, c["tagline"], 20, fill="#b9aef0", weight=500))
    img = CONFIG.get("character")
    if img and os.path.exists(img):
        import struct
        with open(img, "rb") as f:
            png_bytes = f.read(24)
        w, h = struct.unpack(">II", png_bytes[16:24])
        ch = 186; cw = round(ch * w / h)
        b64 = base64.b64encode(open(img, "rb").read()).decode()
        body += '<image class="char" x="%d" y="10" width="%d" height="%d" href="data:image/png;base64,%s"/>' % (W - cw - 40, cw, ch, b64)
    write("hero.svg", svg(200, body, fire=True))


def cards():
    for i, (title, sub, _url, desc) in enumerate(CONFIG["projects"]):
        h = 120 if not desc else 140
        body = ('<rect x="28" y="26" width="4" height="%d" rx="2" fill="url(#bar)"/>' % (h - 52)
                + text(52, 58, title, 26, weight=800)
                + text(52, 88, sub, 15, fill="#b9aef0", weight=500)
                + (text(52, 114, desc, 13, fill="#8f89b3", weight=500) if desc else "")
                + text(W - 40, 58, "View repository", 14, fill="#8a9bff", weight=600, anchor="end"))
        write("card_%s.svg" % title.lower(), svg(h, body))


def principles():
    chips, x = "", 48
    for p in CONFIG["principles"]:
        w = 28 + 10 * len(p)
        chips += ('<rect x="%d" y="78" width="%d" height="36" rx="18" fill="#6e50dc" fill-opacity=".14" '
                  'stroke="#8a6cff" stroke-opacity=".45"/>' % (x, w)
                  + text(x + w / 2, 101, p, 15, fill="#e4defc", weight=600, anchor="middle"))
        x += w + 12
    write("principles.svg", svg(140, text(48, 52, "Working principles", 22, weight=800) + chips))


def status():
    body = ('<circle class="dot" cx="58" cy="62" r="6" fill="#3ddc84"/>'
            + text(76, 68, "Online", 20, weight=800)
            + text(48, 104, "%d featured projects" % len(CONFIG["projects"]), 15, fill="#b9aef0", weight=500))
    write("status.svg", svg(130, body))


def footer():
    write("footer.svg", svg(110, text(48, 66, "Get in touch", 24, weight=800)
                            + text(48, 92, "Open a repository, or send a message.", 14, fill="#b9aef0", weight=500)))
    for label, _ in CONFIG["links"]:
        w = 40 + 11 * len(label)
        body = ('<rect x="1" y="1" width="%d" height="40" rx="20" fill="#6e50dc" fill-opacity=".16" '
                'stroke="#8a6cff" stroke-opacity=".5"/>' % (w - 2) + text(w / 2, 26, label, 14, fill="#efeaff", weight=700, anchor="middle"))
        write("btn_%s.svg" % label.lower(),
              '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="42" viewBox="0 0 %d 42">%s%s</svg>' % (w, w, STYLE, body))


def readme():
    base = CONFIG.get("base_url", "assets").rstrip("/")
    L = ['<div align="center">', '', '![%s](%s/hero.svg)' % (CONFIG["name"], base), '']
    for title, sub, url, _ in CONFIG["projects"]:
        L += ['<a href="%s"><img src="%s/card_%s.svg" alt="%s - %s" width="100%%"/></a>' % (url, base, title.lower(), title, sub), '']
    L += ['![Working principles](%s/principles.svg)' % base, '', '![Status](%s/status.svg)' % base, '',
          '![Get in touch](%s/footer.svg)' % base, '']
    L += ['  '.join('<a href="%s"><img src="%s/btn_%s.svg" alt="%s"/></a>' % (u, base, l.lower(), l) for l, u in CONFIG["links"]), '',
          '</div>', '']
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    hero(); cards(); principles(); status(); footer(); readme()
    print("done")
