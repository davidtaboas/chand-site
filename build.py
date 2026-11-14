#!/usr/bin/env python3
"""Genera las páginas del sitio (inglés en la raíz, español en es/) a partir de los textos de
content.py. Solo biblioteca estándar: `python3 build.py`."""
import math
import pathlib

from content import LANGS, PAGES

ROOT = pathlib.Path(__file__).parent
BASE = "https://davidtaboas.github.io/chand-site/"
ISSUES = "https://github.com/davidtaboas/chand-site/issues"
CSP = ("default-src 'none'; img-src 'self'; style-src 'self'; font-src 'self'; script-src 'self'; "
       "base-uri 'none'; form-action 'none'")


def num(value, lang, digits=1):
    text = f"{value:.{digits}f}"
    return text.replace(".", ",") if lang == "es" else text


def pct(value, lang):
    return f"{value} %" if lang == "es" else f"{value}%"


def path(points, close_to=None):
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in points)
    if close_to is not None:
        d += f" L{points[-1][0]:.1f} {close_to} L{points[0][0]:.1f} {close_to} Z"
    return d


def pull(t, peak=1.0, rise=0.22, end=2.5):
    """Forma de un tirón: arranque rápido, meseta que cede un poco y suelta."""
    up = 1 - math.exp(-((t / rise) ** 1.7)) if t > 0 else 0
    down = 1 / (1 + math.exp((t - end) / 0.05))
    return peak * up * (1 - 0.035 * t) * down


# --- Visualizaciones -------------------------------------------------------------------------

def viz_hero():
    """Tres tirones que van perdiendo fuerza, de fondo en la portada."""
    pts = []
    for i in range(0, 1201, 4):
        t = i / 1200 * 12
        f = sum(pull(t - start, peak, end=2.4) for start, peak in ((0.8, 1.0), (4.6, 0.9), (8.4, 0.8)))
        pts.append((i, 360 - f * 320))
    return (f'<svg class="trace px s4" viewBox="0 0 1200 380" preserveAspectRatio="none" aria-hidden="true">'
            f'<path d="{path(pts)}" fill="none" stroke="currentColor" stroke-width="2" vector-effect="non-scaling-stroke"/>'
            f'<line x1="0" x2="1200" y1="40" y2="40" stroke="currentColor" stroke-width="2" stroke-dasharray="0.1 9" '
            f'stroke-linecap="round" vector-effect="non-scaling-stroke"/></svg>')


def viz_fatigue(t, lang):
    """Tirones de control frente a la referencia; el umbral se mueve con el control."""
    base, top, scale = 250, 30, 2.2  # 100 % = 220 px
    out = [f'<svg class="viz" id="fatigue-viz" viewBox="0 0 560 290" role="img" aria-labelledby="fatigue-desc">',
           f'<desc id="fatigue-desc">{t["fatigue_viz_desc"]}</desc>',
           f'<line class="axis" x1="0" x2="560" y1="{base}" y2="{base}"/>',
           f'<line class="dots" x1="0" x2="560" y1="{top}" y2="{top}"/>',
           f'<text x="0" y="{top - 10}">{t["reference"]} · 42{"," if lang == "es" else "."}4 kg</text>']
    threshold = 10
    y_th = base - (100 - threshold) * scale
    out.append(f'<line class="dots stop" id="fatigue-line" x1="0" x2="560" y1="{y_th:.1f}" y2="{y_th:.1f}"/>')
    out.append(f'<text class="t-stop" id="fatigue-label" x="560" y="{y_th + 16:.1f}" text-anchor="end">'
               f'{t["threshold"]} −{pct(threshold, lang)}</text>')
    value = 100.0
    for i in range(8):
        value *= 0.97
        loss = round(100 - value, 1)
        x = 14 + i * 68
        h = value * scale
        over = " over" if loss >= threshold else ""
        out.append(f'<rect class="bar grow d{min(i + 1, 6)}{over}" data-loss="{loss}" x="{x}" y="{base - h:.1f}" '
                   f'width="46" height="{h:.1f}" rx="5"/>')
        out.append(f'<text x="{x + 23}" y="{base + 20}" text-anchor="middle">{i + 1}</text>')
        out.append(f'<text class="t-on" x="{x + 23}" y="{base - h + 20:.1f}" text-anchor="middle">'
                   f'−{num(loss, lang)}</text>')
    out.append("</svg>")
    return "".join(out)


def viz_pull(t, lang):
    """Curva de un tirón con el pico y la pendiente 20–80 % (RFD)."""
    W, base, top = 560, 250, 50
    xs = lambda s: 30 + s / 3.2 * (W - 40)
    samples = [(i / 200 * 3.2 - 0.25, 0) for i in range(201)]
    samples = [(s, pull(s)) for s, _ in samples]
    peak_t, peak = max(samples, key=lambda p: p[1])
    ys = lambda f: base - f / peak * (base - top)
    pts = [(xs(s + 0.25), ys(f)) for s, f in samples]
    rising = [p for p in samples if p[0] <= peak_t]
    t20 = next(p for p in rising if p[1] >= 0.2 * peak)
    t80 = next(p for p in rising if p[1] >= 0.8 * peak)
    x20, y20, x80, y80 = xs(t20[0] + 0.25), ys(t20[1]), xs(t80[0] + 0.25), ys(t80[1])
    px, py = xs(peak_t + 0.25), ys(peak)
    kg = f'42{"," if lang == "es" else "."}4 kg'
    return "".join([
        f'<svg class="viz" viewBox="0 0 {W} 290" role="img" aria-labelledby="pull-desc">',
        f'<desc id="pull-desc">{t["pull_viz_desc"]}</desc>',
        f'<line class="axis" x1="30" x2="{W}" y1="{base}" y2="{base}"/>',
        f'<line class="dots" x1="30" x2="{W}" y1="{top}" y2="{top}"/>',
        f'<path class="fill-soft late" d="{path(pts, base)}"/>',
        f'<path class="curve draw" pathLength="1" d="{path(pts)}"/>',
        f'<line class="dots accent" x1="30" x2="{x20 + 60:.1f}" y1="{y20:.1f}" y2="{y20:.1f}"/>',
        f'<line class="dots accent" x1="30" x2="{x80 + 60:.1f}" y1="{y80:.1f}" y2="{y80:.1f}"/>',
        f'<text class="t-accent" x="{x20 + 68:.1f}" y="{y20 + 4:.1f}">{pct(20, lang)}</text>',
        f'<text class="t-accent" x="{x80 + 68:.1f}" y="{y80 + 4:.1f}">{pct(80, lang)}</text>',
        f'<line class="slope late" x1="{x20:.1f}" y1="{y20:.1f}" x2="{x80:.1f}" y2="{y80:.1f}"/>',
        f'<circle class="dot" cx="{x20:.1f}" cy="{y20:.1f}" r="5"/><circle class="dot" cx="{x80:.1f}" cy="{y80:.1f}" r="5"/>',
        f'<text class="t-accent" x="{x80 + 68:.1f}" y="{(y20 + y80) / 2 + 4:.1f}">RFD · 196 kg/s</text>',
        f'<circle cx="{px:.1f}" cy="{py:.1f}" r="6" fill="var(--text)"/>',
        f'<text class="t-strong" x="{px + 14:.1f}" y="{py - 14:.1f}" font-size="17">{t["peak"]} · {kg}</text>',
        f'<text x="30" y="{base + 22}">0 s</text><text x="{xs(1.25):.1f}" y="{base + 22}" text-anchor="middle">1 s</text>',
        f'<text x="{xs(2.25):.1f}" y="{base + 22}" text-anchor="middle">2 s</text>',
        f'<text x="{xs(3.2):.1f}" y="{base + 22}" text-anchor="end">3 s</text>',
        "</svg>"])


def viz_train(t, lang):
    """Seis repeticiones de 7 s con 3 s de descanso y la zona objetivo."""
    W, base, top = 560, 200, 30
    sx = (W) / 60
    ys = lambda f: base - f * (base - top)
    out = [f'<svg class="viz" viewBox="0 0 {W} 250" role="img" aria-labelledby="train-desc">',
           f'<desc id="train-desc">{t["train_viz_desc"]}</desc>',
           f'<rect class="fill-accent" x="0" y="{ys(0.75):.1f}" width="{W}" height="{ys(0.65) - ys(0.75):.1f}" rx="4"/>',
           f'<text class="t-accent" x="{W}" y="{ys(0.75) - 8:.1f}" text-anchor="end">{t["target_zone"]} · 65–{pct(75, lang)}</text>']
    pts = []
    for rep in range(6):
        x0 = rep * 10 * sx
        out.append(f'<rect class="work" x="{x0:.1f}" y="{top}" width="{7 * sx:.1f}" height="{base - top}" rx="6"/>')
        out.append(f'<text x="{x0 + 3.5 * sx:.1f}" y="{base + 22}" text-anchor="middle">7 s</text>')
        if rep < 5:
            out.append(f'<text x="{x0 + 8.5 * sx:.1f}" y="{base + 22}" text-anchor="middle" fill-opacity="0.6">3</text>')
        level = 0.705 - 0.012 * rep
        for i in range(0, 101):
            s = i / 100 * 10
            if s < 7:
                wobble = 0.018 * math.sin(s * 4.1 + rep) + 0.01 * math.sin(s * 9.7 + rep * 2)
                f = (level + wobble) * (1 - math.exp(-((s / 0.35) ** 1.6)))
            else:
                f = level * math.exp(-(s - 7) / 0.12)
            pts.append((x0 + s * sx, ys(f)))
    out.append(f'<line class="axis" x1="0" x2="{W}" y1="{base}" y2="{base}"/>')
    out.append(f'<path class="curve draw" pathLength="1" d="{path(pts)}"/>')
    out.append("</svg>")
    return "".join(out)


def mini(inner, desc):
    return f'<svg class="viz" viewBox="0 0 240 110" role="img" aria-label="{desc}">{inner}</svg>'


def mini_curve():
    pts, top = [], None
    for i in range(121):
        s = i / 120 * 3.1 - 0.2
        f = pull(s)
        p = (10 + i / 120 * 220, 96 - f * 84)
        pts.append(p)
        if top is None or p[1] < top[1]:
            top = p
    return pts, top


def viz_peak(t, lang):
    pts, top = mini_curve()
    return mini(f'<line class="axis" x1="10" x2="230" y1="96" y2="96"/><path class="curve" d="{path(pts)}"/>'
                f'<line class="dots accent" x1="10" x2="230" y1="{top[1]:.1f}" y2="{top[1]:.1f}"/>'
                f'<circle class="dot" cx="{top[0]:.1f}" cy="{top[1]:.1f}" r="6"/>', t["g_peak"])


def viz_rfd(t, lang):
    pts, top = mini_curve()
    rising = [p for p in pts if p[0] <= top[0]]
    a = next(p for p in rising if 96 - p[1] >= 0.2 * (96 - top[1]))
    b = next(p for p in rising if 96 - p[1] >= 0.8 * (96 - top[1]))
    k = (b[1] - a[1]) / (b[0] - a[0])
    x1, x2 = a[0] - 10, b[0] + 12
    return mini(f'<line class="axis" x1="10" x2="230" y1="96" y2="96"/><path class="curve" stroke-opacity="0.45" d="{path(pts)}"/>'
                f'<line class="slope" x1="{x1:.1f}" y1="{a[1] + k * (x1 - a[0]):.1f}" x2="{x2:.1f}" y2="{a[1] + k * (x2 - a[0]):.1f}"/>'
                f'<circle class="dot" cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="4.5"/><circle class="dot" cx="{b[0]:.1f}" cy="{b[1]:.1f}" r="4.5"/>',
                t["g_rfd"])


def viz_loss(t, lang):
    return mini(f'<line class="dots" x1="10" x2="230" y1="40" y2="40"/>'
                f'<text x="10" y="26">{t["reference"]}</text>'
                f'<rect class="bar" x="10" y="54" width="193.6" height="26" rx="6"/>'
                f'<rect class="fill-soft" x="205.6" y="54" width="24.4" height="26" rx="6"/>'
                f'<text class="t-stop" x="230" y="100" text-anchor="end" font-size="14">−{pct(12, lang)}</text>', t["g_loss"])


def viz_asym(t, lang):
    left, right = 41.2, 42.7
    w = lambda v: v / right * 150
    return mini(f'<text class="t-left" x="10" y="38">{t["left"]}</text><rect class="bar left" x="80" y="24" width="{w(left):.1f}" height="20" rx="5"/>'
                f'<text class="t-right" x="10" y="78">{t["right"]}</text><rect class="bar right" x="80" y="64" width="{w(right):.1f}" height="20" rx="5"/>'
                f'<line class="dots" x1="{80 + w(left):.1f}" x2="{80 + w(left):.1f}" y1="14" y2="96"/>'
                f'<line class="dots" x1="230" x2="230" y1="14" y2="96"/>'
                f'<text class="t-strong" x="{80 + (w(left) + 150) / 2:.1f}" y="106" text-anchor="middle" font-size="12">{pct(num(3.5, lang), lang)}</text>',
                t["g_asym"])


def viz_cf(t, lang):
    cf, inner, bars = 0.5, [], []
    for i in range(24):
        f = cf + 0.5 * math.exp(-i / 5.5) + 0.012 * math.sin(i * 2.3)
        bars.append(f)
    cf = sum(bars[-6:]) / 6
    y = lambda f: 96 - f * 84
    for i, f in enumerate(bars):
        x = 10 + i * 9.2
        inner.append(f'<rect class="work" x="{x:.1f}" y="{y(min(f, cf)):.1f}" width="6.4" height="{min(f, cf) * 84:.1f}" rx="1.5"/>')
        if f > cf:
            inner.append(f'<rect class="bar" x="{x:.1f}" y="{y(f):.1f}" width="6.4" height="{(f - cf) * 84:.1f}" rx="1.5"/>')
    inner.append(f'<line class="dots accent" x1="10" x2="230" y1="{y(cf):.1f}" y2="{y(cf):.1f}"/>')
    inner.append(f'<text class="t-accent" x="230" y="{y(cf) - 8:.1f}" text-anchor="end">CF</text>')
    inner.append(f'<text class="t-accent" x="62" y="{y(0.86):.1f}">W′</text>')
    inner.append('<line class="axis" x1="10" x2="230" y1="96" y2="96"/>')
    return mini("".join(inner), t["g_cf"])


# --- Piezas de página ------------------------------------------------------------------------

def shot(name, lang, alt, cls="", eager=False, small=False):
    w, h = (480, 1043) if small else (720, 1564)
    src = f"assets/img/{lang}/{name}"
    load = ('fetchpriority="high"' if "p-main" in cls else 'decoding="async"') if eager else 'loading="lazy" decoding="async"'
    return (f'<figure class="phone {cls}"><picture><source type="image/avif" srcset="{{rel}}{src}.avif">'
            f'<img src="{{rel}}{src}.webp" alt="{alt}" width="{w}" height="{h}" {load}></picture></figure>')


def layout(page, lang, t, title, description, body, current=None):
    rel = "" if lang == "en" else "../"
    here = "" if lang == "en" else "es/"
    other = "es" if lang == "en" else "en"
    other_href = (f"es/{page}" if lang == "en" else f"../{page}").replace("index.html", "") or "./"
    canonical = BASE + here + page.replace("index.html", "")
    alt = {"en": BASE + page.replace("index.html", ""), "es": BASE + "es/" + page.replace("index.html", "")}
    home = f"{rel}{here}" or "./"
    nav = "".join(
        f'<a class="{cls}" href="{href}"{" aria-current=page" if key == current else ""}>{label}</a>'
        for key, cls, href, label in [
            ("fatigue", "only-wide", f"{home}#fatigue", t["nav_fatigue"]),
            ("measure", "only-wide", f"{home}#measure", t["nav_measure"]),
            ("train", "only-wide", f"{home}#train", t["nav_train"]),
            ("privacy", "", f"{rel}{here}privacy.html", t["nav_privacy"]),
            ("support", "", f"{rel}{here}support.html", t["nav_support"]),
        ])
    alt_attr = f' data-es="{other_href}"' if lang == "en" else ""
    html = f"""<!doctype html>
<html lang="{lang}" class="no-js"{alt_attr}>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta http-equiv="Content-Security-Policy" content="{CSP}">
<meta name="referrer" content="same-origin">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{alt['en']}">
<link rel="alternate" hreflang="es" href="{alt['es']}">
<link rel="alternate" hreflang="x-default" href="{alt['en']}">
<meta name="color-scheme" content="dark light">
<meta name="theme-color" content="#0d1117" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#fafbfc" media="(prefers-color-scheme: light)">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}assets/img/og.png">
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'es_ES'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{rel}assets/img/icon-64.png" type="image/png">
<link rel="apple-touch-icon" href="{rel}assets/img/icon-180.png">
<link rel="preload" href="{rel}assets/fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{rel}assets/site.css">
<script src="{rel}assets/site.js"></script>
</head>
<body>
<a class="skip" href="#main">{t['skip']}</a>
<header class="top"><div class="wrap">
<a class="brand" href="{home}"><img src="{rel}assets/img/icon-64.png" alt="" width="64" height="64">Chand</a>
<nav aria-label="{t['nav_label']}">{nav}<a class="lang" href="{other_href}" hreflang="{other}" lang="{other}" aria-label="{t['lang_label']}">{other.upper()}</a></nav>
</div></header>
<main id="main">
{body}
</main>
<footer><div class="wrap">
<span>© 2026 David Táboas</span>
<nav aria-label="{t['footer_label']}"><a href="{rel}{here}privacy.html">{t['nav_privacy']}</a><a href="{rel}{here}support.html">{t['nav_support']}</a><a href="{ISSUES}" rel="noopener">{t['contact']}</a></nav>
<p>{t['health']}</p>
<p>{t['site_note']}</p>
</div></footer>
</body>
</html>
"""
    return html.replace("{rel}", rel)


def home(lang, t):
    themes = "".join(
        f'<figure class="px s{1 + i % 2}">{shot("theme-" + key, lang, t["theme_alt"].format(name), small=True)}'
        f'<figcaption><b>{name}</b>{detail}</figcaption></figure>'
        for i, (key, name, detail) in enumerate(t["themes"]))
    zeros = "".join(f'<div class="card reveal"><b class="num">0</b><span>{a}</span><p>{b}</p></div>' for a, b in t["zeros"])
    steps = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in t["fatigue_steps"])
    train_steps = "".join(f"<li><b>{a}</b><span>{b}</span></li>" for a, b in t["train_steps"])
    glossary = [("", "g_peak_t", viz_peak, "g_peak"), ("", "g_rfd_t", viz_rfd, "g_rfd"), ("", "g_loss_t", viz_loss, "g_loss"),
                ("wide", "g_asym_t", viz_asym, "g_asym"), ("wide", "g_cf_t", viz_cf, "g_cf")]
    bento = "".join(f'<article class="card {cls} reveal"><h3>{t[title]}</h3>{fn(t, lang)}<p>{t[text]}</p></article>'
                    for cls, title, fn, text in glossary)
    req = "".join(f'<div class="card reveal"><h3>{a}</h3><p>{b}</p></div>' for a, b in t["req"])
    rel_here = "" if lang == "en" else ""
    return f"""<section class="hero">
<div class="wrap">
<h1>{t['hero_h1']}</h1>
<p class="lead">{t['hero_lead']}</p>
<div class="cta"><span class="pill"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.05 12.54c-.03-2.6 2.13-3.86 2.23-3.92-1.21-1.78-3.1-2.02-3.78-2.05-1.6-.16-3.14.95-3.95.95-.82 0-2.08-.93-3.42-.9-1.76.03-3.38 1.02-4.29 2.6-1.83 3.17-.47 7.87 1.31 10.45.87 1.26 1.91 2.68 3.27 2.63 1.31-.05 1.81-.85 3.39-.85 1.58 0 2.03.85 3.42.82 1.41-.02 2.31-1.29 3.17-2.56 1-1.46 1.41-2.88 1.44-2.95-.03-.01-2.76-1.06-2.79-4.22ZM14.44 4.9c.72-.88 1.21-2.09 1.08-3.3-1.04.04-2.3.69-3.05 1.57-.67.77-1.26 2.01-1.1 3.2 1.16.09 2.35-.59 3.07-1.47Z"/></svg>{t['soon']}</span>
<a class="pill ghost" href="#fatigue">{t['how']}</a></div>
<ul class="facts">{"".join(f"<li>{x}</li>" for x in t['facts'])}</ul>
</div>
<div class="stage">
<div class="glow"></div>
{viz_hero()}
{shot("fatigue", lang, t['alt_fatigue'], "p-left px s2", eager=True)}
{shot("workout", lang, t['alt_workout'], "p-right px s2", eager=True)}
{shot("capture", lang, t['alt_capture'], "p-main px s1", eager=True)}
<div class="chip chip-a px s3"><small>{t['chip_max']}</small><b class="num">{num(42.4, lang)} kg</b></div>
<div class="chip chip-b px s3"><small>{t['chip_loss']}</small><b class="num">−{pct(12, lang)}</b></div>
</div>
</section>

<section class="section" id="fatigue">
<div class="wrap">
<p class="label">{t['nav_fatigue']}</p>
<h2>{t['fatigue_h2']}</h2>
<p class="lead">{t['fatigue_lead']}</p>
<div class="split">
<div>
<div class="card reveal" id="fatigue-card" data-stop="{t['verdict_stop']}" data-threshold="{t['threshold']}" data-lang="{lang}">
<div class="fatigue-head">
<p class="verdict">{t['verdict_label']}<b class="num is-stop" id="fatigue-verdict" aria-live="polite">{t['verdict_stop'].format(4)}</b></p>
<label class="range">{t['threshold_label']} <output id="fatigue-out" for="fatigue-range">{pct(10, lang)}</output>
<input id="fatigue-range" type="range" min="5" max="20" step="1" value="10"></label>
</div>
{viz_fatigue(t, lang)}
<p class="cap">{t['fatigue_cap']}</p>
</div>
<ol class="steps">{steps}</ol>
</div>
<div class="duo">{shot("fatigue", lang, t['alt_fatigue'], "px s1")}{shot("fatigue-chart", lang, t['alt_fatigue_chart'], "px s2")}</div>
</div>
</div>
</section>

<section class="section alt" id="measure">
<div class="wrap">
<p class="label">{t['nav_measure']}</p>
<h2>{t['measure_h2']}</h2>
<p class="lead">{t['measure_lead']}</p>
<div class="split flip">
<div class="card reveal">{viz_pull(t, lang)}<p class="cap">{t['pull_cap']}</p></div>
<div class="duo">{shot("plan", lang, t['alt_plan'], "px s1")}{shot("summary", lang, t['alt_summary'], "px s2")}</div>
</div>
<div class="bento">{bento}</div>
</div>
</section>

<section class="section" id="train">
<div class="wrap">
<p class="label">{t['nav_train']}</p>
<h2>{t['train_h2']}</h2>
<p class="lead">{t['train_lead']}</p>
<div class="split">
<div>
<div class="card reveal">{viz_train(t, lang)}<p class="cap">{t['train_cap']}</p></div>
<ol class="steps">{train_steps}</ol>
</div>
<div class="duo">{shot("workout", lang, t['alt_workout'], "px s1")}{shot("live", lang, t['alt_live'], "px s2")}</div>
</div>
</div>
</section>

<section class="section alt" id="themes">
<div class="wrap">
<p class="label">{t['themes_label']}</p>
<h2>{t['themes_h2']}</h2>
<p class="lead">{t['themes_lead']}</p>
</div>
<div class="themes" tabindex="0" role="group" aria-label="{t['themes_label']}">{themes}</div>
</section>

<section class="section" id="privacy">
<div class="wrap">
<p class="label">{t['nav_privacy']}</p>
<h2>{t['privacy_h2']}</h2>
<p class="lead">{t['privacy_lead']}</p>
<div class="zeros">{zeros}</div>
<div class="note"><a class="pill ghost" href="privacy.html">{t['privacy_link']}</a><a class="pill ghost" href="support.html">{t['support_link']}</a></div>
</div>
</section>

<section class="section alt" id="requirements">
<div class="wrap">
<p class="label">{t['req_label']}</p>
<h2>{t['req_h2']}</h2>
<div class="req">{req}</div>
</div>
</section>"""


def doc(lang, t, key):
    return f'<article class="doc"><div class="wrap">{PAGES[key][lang].replace("{issues}", ISSUES)}</div></article>'


def main():
    for lang, t in LANGS.items():
        out = ROOT if lang == "en" else ROOT / "es"
        out.mkdir(exist_ok=True)
        (out / "index.html").write_text(
            layout("index.html", lang, t, t["title"], t["description"], home(lang, t)), encoding="utf-8")
        for key in ("privacy", "support"):
            (out / f"{key}.html").write_text(
                layout(f"{key}.html", lang, t, t[f"{key}_title"], t[f"{key}_description"], doc(lang, t, key), current=key),
                encoding="utf-8")
    pages = ["", "privacy.html", "support.html"]
    urls = "".join(
        f"<url><loc>{BASE}{prefix}{p}</loc>"
        f'<xhtml:link rel="alternate" hreflang="en" href="{BASE}{p}"/>'
        f'<xhtml:link rel="alternate" hreflang="es" href="{BASE}es/{p}"/></url>\n'
        for p in pages for prefix in ("", "es/"))
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        f'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n{urls}</urlset>\n', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")


if __name__ == "__main__":
    main()
