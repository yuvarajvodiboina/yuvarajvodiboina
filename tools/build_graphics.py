"""Builds every profile README graphic as an animated SVG set in Google Sans.

GitHub cannot load web fonts in a README, so every label is converted to
vector outlines. The palette is CodeHorizon's: warm paper and sun orange,
light in both GitHub themes on purpose.

Needs: pip install fonttools uharfbuzz, and Google Sans in ~/Library/Fonts.

    python tools/build_graphics.py <screenshots dir> <contributions.json>

The screenshots dir holds shopgrade/keeptake/securevault/tubefocus .webp
(from yuvarajvodiboina.in/assets/screens/). The JSON is the output of:
    gh api graphql -f query='{user(login:"yuvarajvodiboina"){contributionsCollection{
      contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}'
"""
import base64
import datetime as dt
import json
import math
import os
import sys

import uharfbuzz as hb
from fontTools.pens.basePen import BasePen
from fontTools.ttLib import TTFont

FONT_DIR = os.path.expanduser("~/Library/Fonts")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "profile")
SHOTS = sys.argv[1] if len(sys.argv) > 1 else "."
CAL = sys.argv[2] if len(sys.argv) > 2 else "cal.json"

PAPER, TOP, INK, MUTED, LINE, SIDE = "#f2efe9", "#fbfaf7", "#1c1a17", "#5c5148", "#ddd5c8", "#cfc8ba"
SUN, SUN_TEXT, SUN_SOFT, PEACH = "#f4500f", "#c23c06", "#ffbf9e", "#ffe1cf"
MINT, LILAC, BUTTER = "#d9f0d9", "#e9e2fb", "#fbeec2"

BASE_CSS = """
@keyframes rise { from { opacity:0; transform:translateY(36px) } to { opacity:1; transform:none } }
@keyframes fade { from { opacity:0 } to { opacity:1 } }
.rise { animation: rise 1s cubic-bezier(.2,.7,.2,1) both }
.fade { animation: fade 1.2s ease both }
@media (prefers-reduced-motion: reduce) { * { animation: none !important } }
"""

# ------------------------------------------------------------------ type
_fonts = {}


def font(weight):
    if weight not in _fonts:
        path = os.path.join(FONT_DIR, f"GoogleSans-{weight}.ttf")
        tt = TTFont(path)
        with open(path, "rb") as fh:
            hbf = hb.Font(hb.Face(fh.read()))
        _fonts[weight] = (tt.getGlyphSet(), tt.getGlyphOrder(), hbf)
    return _fonts[weight]


class _Pen(BasePen):
    def __init__(self, gs, dx, sc):
        super().__init__(gs)
        self.o, self.dx, self.sc = [], dx, sc

    def _p(self, pt):
        return f"{(pt[0] + self.dx) * self.sc:.1f} {pt[1] * self.sc:.1f}"

    def _moveTo(self, pt):
        self.o.append("M" + self._p(pt))

    def _lineTo(self, pt):
        self.o.append("L" + self._p(pt))

    def _qCurveToOne(self, a, b):
        self.o.append("Q" + self._p(a) + " " + self._p(b))

    def _curveToOne(self, a, b, c):
        self.o.append("C" + self._p(a) + " " + self._p(b) + " " + self._p(c))

    def _closePath(self):
        self.o.append("Z")


def _shape(s, weight):
    gs, order, hbf = font(weight)
    buf = hb.Buffer()
    buf.add_str(s)
    buf.guess_segment_properties()
    hb.shape(hbf, buf, {"kern": True, "liga": False})
    for info in buf.glyph_infos:
        if info.codepoint == 0:
            raise ValueError(f"Google Sans {weight} has no glyph in {s!r}")
    return gs, order, buf


def width(s, size, weight="Regular", track=0):
    _, _, buf = _shape(s, weight)
    return (sum(p.x_advance for p in buf.glyph_positions) + track * len(s)) * size / 1000


def text(x, y, s, size, weight="Regular", fill=INK, anchor="start", track=0, cls="", style=""):
    gs, order, buf = _shape(s, weight)
    sc = size / 1000
    cx, out = 0, []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        pen = _Pen(gs, cx + pos.x_offset, sc)
        gs[order[info.codepoint]].draw(pen)
        out += pen.o
        cx += pos.x_advance + track
    w = (cx - track) * sc
    if anchor == "middle":
        x -= w / 2
    elif anchor == "end":
        x -= w
    label = s.replace("&", "&amp;").replace('"', "&quot;")
    g = (f'<g transform="translate({x:.1f} {y:.1f}) scale(1 -1)" fill="{fill}" aria-label="{label}">'
         f'<path d="{"".join(out)}"/></g>')
    if cls or style:
        g = f'<g class="{cls}" style="{style}">{g}</g>'
    return g


def rich(x, y, parts, size, anchor="start", cls="", style=""):
    """parts: [(string, weight, fill)] set on one baseline."""
    total = sum(width(s, size, w) for s, w, _ in parts)
    if anchor == "middle":
        x -= total / 2
    elif anchor == "end":
        x -= total
    out = []
    for s, w, f in parts:
        out.append(text(x, y, s, size, w, f))
        x += width(s, size, w)
    g = "".join(out)
    return f'<g class="{cls}" style="{style}">{g}</g>' if (cls or style) else g


def wrap(s, size, weight, max_w):
    lines, cur = [], ""
    for word in s.split():
        trial = (cur + " " + word).strip()
        if width(trial, size, weight) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    return lines + [cur]


def arrow(x, y, s, color, stroke=3.2):
    """A north-east arrow icon, s px square, top-left at x, y."""
    return (f'<path d="M{x + s * .2:.1f} {y + s * .8:.1f}L{x + s * .8:.1f} {y + s * .2:.1f}'
            f'M{x + s * .32:.1f} {y + s * .2:.1f}H{x + s * .8:.1f}V{y + s * .68:.1f}" fill="none" '
            f'stroke="{color}" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round"/>')


def eyebrow(x, y, num, label, right=None, W=1600, color=MUTED, numcolor=SUN_TEXT):
    out = [text(x, y, num, 24, "Medium", numcolor, track=40),
           text(x + width(num, 24, "Medium", 40) + 18, y, label, 24, "Medium", color, track=110)]
    if right:
        out.append(text(W - x, y, right, 24, "Medium", color, "end", track=110))
    return "".join(out)


def svg(name, w, h, title, desc, body, css="", bg=PAPER, radius=28):
    doc = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
           f'role="img" aria-labelledby="title desc">\n<title id="title">{title}</title>\n'
           f'<desc id="desc">{desc}</desc>\n<style>{BASE_CSS}{css}</style>\n'
           f'<clipPath id="frame"><rect width="{w}" height="{h}" rx="{radius}"/></clipPath>\n'
           f'<g clip-path="url(#frame)"><rect width="{w}" height="{h}" fill="{bg}"/>\n{body}\n</g>\n</svg>\n')
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w") as fh:
        fh.write(doc)
    print(f"{name:28} {len(doc) / 1024:6.0f} KB")


def shot(slug):
    with open(os.path.join(SHOTS, slug + ".webp"), "rb") as fh:
        return "data:image/webp;base64," + base64.b64encode(fh.read()).decode()


def striped_sun(cx, cy, r, color, gap_color, bands=6):
    """A sun cut by horizontal bands that thicken towards the horizon."""
    out = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}"/>']
    y = cy - 6
    for k in range(bands):
        hgt = 9 - k * 1.3
        out.append(f'<rect x="{cx - r - 2}" y="{y - hgt:.1f}" width="{2 * r + 4}" height="{hgt:.1f}" fill="{gap_color}"/>')
        y -= hgt + 13 + k * 4
    return "".join(out)



# ------------------------------------------------------------------ hero
def hero(total):
    W, H, HZ = 1600, 600, 400
    css = """
@keyframes sunrise { from { transform:translateY(150px) } to { transform:none } }
.sun { animation: sunrise 2.6s cubic-bezier(.16,.8,.2,1) .2s both }
"""
    waves = []
    for i in range(8):
        L = 240 + i * 50
        y0 = HZ + 6 + i * 6 + i * i * 0.6
        amp = 1.5 + i * 1.0
        pts, x = [], -L
        while x <= W + L:
            pts.append(f"{x:.0f} {y0 + amp * math.sin(2 * math.pi * x / L):.1f}")
            x += 12
        css += f"@keyframes w{i} {{ to {{ transform:translateX(-{L}px) }} }}\n"
        waves.append(f'<path d="M{"L".join(pts)}" fill="none" stroke="{SUN if i % 2 == 0 else "#ff7a45"}" '
                     f'stroke-opacity="{0.35 + 0.08 * i:.2f}" stroke-width="{1.4 + i * 0.45:.1f}" '
                     f'style="animation:w{i} {9 + i * 2.2:.1f}s linear infinite"/>')
    body = [
        text(64, 84, "SOFTWARE ENGINEER", 24, "Medium", MUTED, track=120, cls="fade"),
        text(64 + width("SOFTWARE ENGINEER", 24, "Medium", 120) + 34, 84, "HYDERABAD, INDIA", 24, "Medium",
             SUN_TEXT, track=120, cls="fade"),
    ]
    pill = "OPEN TO ROLES"
    pw = width(pill, 24, "Medium", 110) + 56
    body.append(f'<g class="fade"><rect x="{W - 64 - pw:.1f}" y="48" width="{pw:.1f}" height="52" rx="26" fill="{INK}"/>'
                + text(W - 64 - pw / 2, 83, pill, 24, "Medium", TOP, "middle", track=110) + "</g>")
    body.append(f'<clipPath id="sky"><rect width="{W}" height="{HZ}"/></clipPath>'
                f'<g clip-path="url(#sky)"><g class="sun">{striped_sun(1380, HZ, 120, SUN, PAPER, 5)}</g></g>')
    body.append(f'<line x1="0" y1="{HZ}" x2="{W}" y2="{HZ}" stroke="{SUN}" stroke-width="2"/>')
    body += waves
    body.append(text(54, 232, "Yuvaraj Vodiboina", 128, "Bold", INK, track=-16, cls="rise", style="animation-delay:.1s"))
    body.append(rich(64, 316, [("I build for the ", "Regular", MUTED), ("browser", "MediumItalic", SUN_TEXT),
                               (" and the ", "Regular", MUTED), ("pocket.", "MediumItalic", SUN_TEXT)], 44,
                     cls="rise", style="animation-delay:.3s"))
    stats = [("11", "products shipped"), ("8", "live on Chrome and Play"),
             ("9", "merged open-source PRs"), (f"{total:,}", "contributions this year")]
    py, ph = 460, 116
    body.append(f'<rect x="32" y="{py}" width="{W - 64}" height="{ph}" rx="22" fill="{TOP}" stroke="{LINE}" stroke-width="1.5"/>')
    cw = (W - 64) / 4
    for i, (n, lab) in enumerate(stats):
        x = 32 + i * cw + 36
        if i:
            body.append(f'<line x1="{32 + i * cw:.0f}" y1="{py + 24}" x2="{32 + i * cw:.0f}" y2="{py + ph - 24}" stroke="{LINE}" stroke-width="1.5"/>')
        body.append(f'<g class="rise" style="animation-delay:{.5 + i * .1:.2f}s">'
                    + text(x, py + 60, n, 54, "Bold", SUN if i == 2 else INK, track=-10)
                    + text(x, py + 94, lab, 24, "Regular", MUTED) + "</g>")
    svg("hero.svg", W, H, "Yuvaraj Vodiboina, software engineer",
        f"Yuvaraj Vodiboina, software engineer in Hyderabad, India, open to roles. I build for the browser and the "
        f"pocket. 11 products shipped, 8 live on Chrome and Google Play, 9 merged open-source pull requests, "
        f"{total:,} GitHub contributions this year.", "\n".join(body), css)


# ------------------------------------------------------------------ links
LINKS = [("portfolio", "Portfolio", True), ("resume", "Résumé", False),
         ("linkedin", "LinkedIn", False), ("email", "Email", False)]


def link_pill(slug, label, primary):
    W, H = 380, 104
    fg, bg = (TOP, INK) if primary else (INK, TOP)
    body = [f'<rect x="1.5" y="1.5" width="{W - 3}" height="{H - 3}" rx="{(H - 3) / 2}" fill="{bg}" '
            f'stroke="{INK if primary else LINE}" stroke-width="3"/>']
    tw = width(label, 36, "Medium") + 20 + 30
    x = (W - tw) / 2
    body.append(text(x, 64, label, 36, "Medium", fg))
    body.append(arrow(x + tw - 30, 37, 30, SUN if primary else SUN_TEXT))
    svg(f"link-{slug}.svg", W, H, label, f"Open {label}", "".join(body), bg="none", radius=52)


# ------------------------------------------------------------------ work
WORK = [
    ("shopgrade", "ShopGrade", PEACH, "542", "tests", "Shopify audits"),
    ("securevault", "SecureVault", MINT, "AES-256", "encryption", "Android vault"),
    ("keeptake", "Keeptake", LILAC, "207", "E2E checks", "Screen recorder"),
    ("tubefocus", "TubeFocus", BUTTER, "63", "checks", "YouTube focus"),
]


def work():
    W, H = 1600, 550
    GAP, X0 = 22, 32
    tw = (W - 2 * X0 - 3 * GAP) / 4
    ty, th, ih = 124, 404, 214
    css = """
@keyframes float { 0%,100% { transform:translateY(0) } 50% { transform:translateY(-7px) } }
.float { animation: float 6s ease-in-out infinite }
"""
    body = [eyebrow(64, 84, "(01)", "SELECTED WORK", "11 PRODUCTS, 8 LIVE"),
            '<filter id="sh" x="-10%" y="-10%" width="120%" height="140%">'
            '<feDropShadow dx="0" dy="12" stdDeviation="12" flood-color="#2a1510" flood-opacity=".16"/></filter>']
    for i, (slug, name, tint, metric, mlabel, kind) in enumerate(WORK):
        x = X0 + i * (tw + GAP)
        fx, fy, fw = x + 20, ty + 20, tw - 40
        body.append(f'<rect x="{x:.1f}" y="{ty}" width="{tw:.1f}" height="{th}" rx="24" fill="{tint}"/>')
        body.append(f'<clipPath id="s{i}"><rect x="{fx:.1f}" y="{fy}" width="{fw:.1f}" height="{ih}" rx="14"/></clipPath>')
        if slug == "securevault":
            img = (f'<image x="{fx + fw / 2 - 60:.1f}" y="{fy + 10}" width="120" height="{ih - 20}" '
                   f'preserveAspectRatio="xMidYMid meet" href="{shot(slug)}"/>')
        else:
            img = (f'<image x="{fx:.1f}" y="{fy}" width="{fw:.1f}" height="{ih}" '
                   f'preserveAspectRatio="xMidYMin slice" href="{shot(slug)}"/>')
        body.append(f'<g class="float" style="animation-delay:{i * .6:.1f}s">'
                    f'<rect x="{fx:.1f}" y="{fy}" width="{fw:.1f}" height="{ih}" rx="14" fill="{TOP}" filter="url(#sh)"/>'
                    f'<g clip-path="url(#s{i})">{img}</g></g>')
        body.append(text(x + 22, ty + 296, name, 40, "Bold", INK, track=-8))
        body.append(text(x + 24, ty + 334, kind, 24, "Regular", MUTED))
        parts = [(metric, "Bold", SUN_TEXT)] + ([(" " + mlabel, "Medium", SUN_TEXT)] if mlabel else [])
        body.append(rich(x + 24, ty + 378, parts, 28))
    svg("work.svg", W, H, "Selected work",
        "Selected work, 4 of 11 products. " + " ".join(
            f"{n}: {k.lower()}, {m} {l}." .replace("  ", " ") for _, n, _, m, l, k in WORK),
        "\n".join(body), css)


# ------------------------------------------------------------------ toolkit keyboard
KEYS = [
    ("LANGUAGES", ["TypeScript", "JavaScript", "Kotlin", "Java", "Python", "SQL"], {0, 2}),
    ("WEB", ["React", "Next.js", "React Native", "Node.js", "Tailwind CSS", "Shopify Liquid"], {0, 1}),
    ("ANDROID", ["Jetpack Compose", "Coroutines", "Hilt", "Room", "WorkManager", "Keystore"], {0}),
    ("PLATFORM", ["Manifest V3", "Appwrite", "Firebase", "Cloudflare", "Docker", "Vercel"], {0}),
    ("QUALITY", ["Playwright", "Jest", "Robolectric", "GitHub Actions", "Figma"], {0}),
]


def toolkit():
    W = 1600
    KH, DEPTH, GAP, ROW = 70, 9, 14, 94
    top = 128
    H = top + ROW * len(KEYS) + 30
    css = """
@keyframes press { 0%,6%,100% { transform:none } 2% { transform:translateY(7px) } }
.key { animation: press 9s ease-in-out infinite }
"""
    body = [eyebrow(64, 84, "(02)", "TOOLKIT", "WHAT I SHIP WITH")]
    kx0, kx1 = 330, W - 64
    n = 0
    for r, (cat, keys, hot) in enumerate(KEYS):
        y = top + r * ROW
        body.append(text(64, y + 45, cat, 22, "Medium", MUTED, track=110))
        size = 27
        widths = [width(k, size, "Medium") + 50 for k in keys]
        assert sum(widths) + GAP * (len(keys) - 1) <= kx1 - kx0, cat
        x = kx0
        for i, (k, w) in enumerate(zip(keys, widths)):
            face, ink, side = (SUN, TOP, "#b83a0a") if i in hot else (TOP, INK, SIDE)
            body.append(f'<rect x="{x:.1f}" y="{y + DEPTH}" width="{w:.1f}" height="{KH}" rx="16" fill="{side}"/>')
            body.append(f'<g class="key" style="animation-delay:{n * .37 % 9:.2f}s">'
                        f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{KH}" rx="16" fill="{face}" '
                        f'stroke="{INK}" stroke-opacity=".12" stroke-width="2"/>'
                        + text(x + w / 2, y + 45, k, size, "Medium", ink, "middle") + "</g>")
            x += w + GAP
            n += 1
    svg("toolkit.svg", W, H, "Toolkit",
        " ".join(f"{c.title()}: {', '.join(k)}." for c, k, _ in KEYS), "\n".join(body), css)


# ------------------------------------------------------------------ activity
def activity(cal):
    W, H = 1600, 460
    weeks = cal["weeks"]
    days = [d for w in weeks for d in w["contributionDays"]]
    total = cal["totalContributions"]
    best = cur = 0
    for d in days:
        cur = cur + 1 if d["contributionCount"] else 0
        best = max(best, cur)
    sums = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in weeks]
    peak = max(sums)
    css = """
@keyframes grow { from { transform:scaleY(0) } to { transform:none } }
.bar { transform-box:fill-box; transform-origin:50% 100%; animation: grow .9s cubic-bezier(.2,.7,.2,1) both }
"""
    last = dt.date.fromisoformat(days[-1]["date"])
    body = [eyebrow(64, 84, "(03)", "ACTIVITY", f"SNAPSHOT {last.day} {last.strftime('%b').upper()} {last.year}")]
    figures = [(f"{total:,}", "contributions this year", INK), (str(peak), "in the busiest week", SUN),
               (str(best), "day longest streak", INK)]
    x = 64
    for i, (n, lab, col) in enumerate(figures):
        nw = width(n, 64, "Bold", -10)
        body.append(f'<g class="rise" style="animation-delay:{i * .1:.1f}s">'
                    + text(x, 180, n, 64, "Bold", col, track=-10)
                    + text(x + nw + 14, 178, lab, 26, "Regular", MUTED) + "</g>")
        x += nw + 14 + width(lab, 26) + 70
    assert x - 70 < W - 64
    bx0, bx1, base, top = 64, W - 64, H - 66, 222
    slot = (bx1 - bx0) / len(sums)
    for i, s in enumerate(sums):
        bx = bx0 + i * slot + slot * .18
        if not s:
            body.append(f'<rect x="{bx:.1f}" y="{base - 3}" width="{slot * .64:.1f}" height="3" rx="1.5" fill="{LINE}"/>')
            continue
        h = max(6, math.sqrt(s / peak) * (base - top))
        body.append(f'<g class="bar" style="animation-delay:{.2 + i * .018:.3f}s"><rect x="{bx:.1f}" y="{base - h:.1f}" '
                    f'width="{slot * .64:.1f}" height="{h:.1f}" rx="5" fill="{SUN if s == peak else INK}" '
                    f'fill-opacity="{1 if s == peak else .82}"/></g>')
    seen = set()
    for i, w in enumerate(weeks):
        d = dt.date.fromisoformat(w["contributionDays"][0]["date"])
        if d.day <= 7 and (d.year, d.month) not in seen and i < len(weeks) - 2:
            seen.add((d.year, d.month))
            body.append(text(bx0 + i * slot + slot * .18, base + 38, d.strftime("%b"), 21, "Regular", MUTED))
    svg("activity.svg", W, H, f"{total:,} contributions in the last year",
        f"GitHub activity snapshot taken {last.isoformat()}: {total:,} contributions in the last year, {peak} in the "
        f"busiest week, longest streak {best} days. Weekly bar chart, square-root scale.", "\n".join(body), css)
    return total


# ------------------------------------------------------------------ next station
def closing():
    W, H = 1600, 400
    css = """
@keyframes sunrise { from { transform:translateY(220px) } to { transform:none } }
.sun { animation: sunrise 3s cubic-bezier(.16,.8,.2,1) .3s both }
"""
    body = [f'<g class="sun">{striped_sun(1360, H + 30, 250, "#ff7a45", SUN, 7)}</g>',
            eyebrow(64, 84, "(04)", "NEXT STATION", color=PEACH, numcolor=TOP),
            rich(58, 196, [("Open to software ", "Bold", TOP), ("engineering roles.", "BoldItalic", INK)], 76,
                 cls="rise", style="animation-delay:.1s"),
            text(64, 252, "Frontend, Android or full stack, on-site in Hyderabad or remote.", 29, "Regular", PEACH,
                 cls="rise", style="animation-delay:.2s")]
    mail = "yvodiboina@gmail.com"
    mw = width(mail, 32, "Medium") + 64 + 40
    body.append(f'<g class="rise" style="animation-delay:.35s"><rect x="64" y="292" width="{mw:.1f}" height="68" rx="34" fill="{TOP}"/>'
                + text(96, 337, mail, 32, "Medium", INK) + arrow(64 + mw - 66, 308, 36, SUN, 4) + "</g>")
    assert 58 + width("Open to software engineering roles.", 76, "Bold") < W - 40
    svg("closing.svg", W, H, "Open to software engineering roles",
        "Next station: open to frontend, Android or full-stack software engineering roles, on-site in Hyderabad "
        "or remote. Email yvodiboina@gmail.com.", "\n".join(body), css, bg=SUN)


if __name__ == "__main__":
    with open(CAL) as fh:
        cal = json.load(fh)["data"]["user"]["contributionsCollection"]["contributionCalendar"]
    total = activity(cal)
    hero(total)
    for slug, label, primary in LINKS:
        link_pill(slug, label, primary)
    work()
    toolkit()
    closing()
