# -*- coding: utf-8 -*-
"""Generate illustrated SVG scenes for RhinoFence — dusk landscapes with each
fence type drawn in silhouette. Pure-SVG so pages stay fast and self-hosted."""
import os, math, random

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
os.makedirs(OUT, exist_ok=True)

W, H = 800, 500          # card scenes
GROUND = 440             # ground line y

SKIES = {
    "gold":   ["#141a26", "#4a2c1e", "#c96a2a", "#ffb066"],
    "amber":  ["#1a1626", "#5b2b23", "#d97c33", "#ffc07a"],
    "teal":   ["#0e1b24", "#1c3f4c", "#3d7d8e", "#a9d3dd"],
    "mauve":  ["#171426", "#45223c", "#984465", "#ff9a76"],
    "ember":  ["#120f1a", "#3d1f26", "#8a3b2e", "#ff8a4d"],
    "dawn":   ["#101c2e", "#2c4a63", "#7793ab", "#f2c9a0"],
}

SIL = "#101318"          # silhouette colour
SIL2 = "#171b22"         # nearer silhouette
RIM = "#ffd45e"          # rim-light (brand gold)


def sky(scheme, w=W, h=H):
    c = SKIES[scheme]
    return f'''<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{c[0]}"/><stop offset=".45" stop-color="{c[1]}"/>
      <stop offset=".78" stop-color="{c[2]}"/><stop offset="1" stop-color="{c[3]}"/>
    </linearGradient>
    <radialGradient id="sunglow" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="{SKIES[scheme][3]}" stop-opacity=".9"/>
      <stop offset="1" stop-color="{SKIES[scheme][3]}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="vig" cx=".5" cy=".42" r=".75">
      <stop offset=".55" stop-color="#000" stop-opacity="0"/>
      <stop offset="1" stop-color="#000" stop-opacity=".38"/>
    </radialGradient>
    <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>
      <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.05 0"/></filter>'''


def sun(x, y, r=44):
    return (f'<circle cx="{x}" cy="{y}" r="{r*3.2:.0f}" fill="url(#sunglow)"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffd9a0"/>')


def clouds(seed, w=W):
    rnd = random.Random(seed)
    out = []
    for i in range(3):
        cx, cy = rnd.randint(60, w - 60), rnd.randint(50, 170)
        rx = rnd.randint(60, 130)
        out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{rx//7}" fill="#fff" opacity="0.06"/>')
        out.append(f'<ellipse cx="{cx+rx//3}" cy="{cy+6}" rx="{rx//1.5:.0f}" ry="{rx//9}" fill="#fff" opacity="0.05"/>')
    return "".join(out)


def hills(w=W):
    return (f'<path d="M0 340 Q {w*0.22:.0f} 292 {w*0.45:.0f} 330 T {w} 322 V{GROUND} H0 Z" fill="#0d1016" opacity=".72"/>'
            f'<path d="M0 372 Q {w*0.3:.0f} 336 {w*0.6:.0f} 366 T {w} 356 V{GROUND} H0 Z" fill="#0b0d12" opacity=".92"/>')


def ground(w=W, h=H):
    return f'<rect x="0" y="{GROUND}" width="{w}" height="{h-GROUND}" fill="#090b0f"/>'


def acacia(x, y, s=1.0, flip=False):
    fs = -1 if flip else 1
    return f'''<g transform="translate({x} {y}) scale({fs*s} {s})" fill="{SIL}" stroke="{SIL}">
      <path d="M0 0 C 2 -18 4 -34 10 -46" stroke-width="5" fill="none" stroke-linecap="round"/>
      <path d="M6 -28 C 14 -36 22 -42 34 -47" stroke-width="3.4" fill="none" stroke-linecap="round"/>
      <path d="M8 -34 C 2 -42 -8 -48 -20 -51" stroke-width="3.4" fill="none" stroke-linecap="round"/>
      <path d="M-34 -50 C -20 -62 24 -64 44 -52 C 30 -46 -18 -44 -34 -50 Z"/>
      <path d="M-24 -56 C -12 -64 18 -65 30 -58" opacity=".9"/>
    </g>'''


def birds(x, y, n=3, s=1.0):
    out = []
    for i in range(n):
        bx, by = x + i * 26 * s, y - (i % 2) * 10
        out.append(f'<path d="M{bx} {by} q{5*s} {-7*s} {10*s} 0 q{5*s} {-7*s} {10*s} 0" stroke="{SIL}" stroke-width="{2*s:.1f}" fill="none" stroke-linecap="round"/>')
    return "".join(out)


def frame(scheme, body, w=W, h=H, seed=1):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" preserveAspectRatio="xMidYMid slice">
  <defs>{sky(scheme, w, h)}</defs>
  <rect width="{w}" height="{h}" fill="url(#sky)"/>
  {clouds(seed, w)}
  {body}
  <rect width="{w}" height="{h}" fill="url(#vig)"/>
  <rect width="{w}" height="{h}" filter="url(#grain)" opacity=".8"/>
</svg>'''


# ---------- fence renderers (drawn 0..W, sit on GROUND) ----------

def posts(xs, top, width=7, cap=True, color=SIL2):
    out = []
    for x in xs:
        out.append(f'<rect x="{x-width/2:.1f}" y="{top}" width="{width}" height="{GROUND-top}" fill="{color}"/>')
        if cap:
            out.append(f'<rect x="{x-width/2-1.5:.1f}" y="{top-4}" width="{width+3}" height="5" rx="2" fill="{color}"/>')
        out.append(f'<line x1="{x-width/2:.1f}" y1="{top}" x2="{x-width/2:.1f}" y2="{GROUND}" stroke="{RIM}" stroke-width="1" opacity=".35"/>')
    return "".join(out)


def rim(x1, y1, x2, y2, w=1.6, o=.5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{RIM}" stroke-width="{w}" opacity="{o}"/>'


def clearview():
    top = 318
    mesh = f'''<pattern id="m358" width="9" height="20" patternUnits="userSpaceOnUse">
        <path d="M0 0V20 M0 0H9 M0 10H9" stroke="{SIL2}" stroke-width="1.6" opacity=".95"/></pattern>'''
    body = f'''<defs>{mesh}</defs>
      {hills()}{acacia(120, GROUND, 1.15)}{acacia(690, GROUND, .85, True)}{birds(560, 120)}
      <rect x="0" y="{top}" width="{W}" height="{GROUND-top}" fill="url(#m358)"/>
      <rect x="0" y="{top-6}" width="{W}" height="7" fill="{SIL2}"/>{rim(0, top-6, W, top-6)}
      {posts(range(60, W, 136), top-10)}
      {ground()}'''
    return frame("teal", body, seed=3)


def palisade():
    top = 300
    pales = []
    for x in range(16, W, 20):
        pales.append(f'<path d="M{x-4} {GROUND} V{top+16} L{x} {top} L{x+4} {top+16} V{GROUND} Z" fill="{SIL2}"/>')
        pales.append(f'<path d="M{x-4} {GROUND} V{top+16} L{x} {top}" stroke="{RIM}" stroke-width="1" fill="none" opacity=".3"/>')
    body = f'''{hills()}{acacia(560, GROUND, 1.2)}{birds(150, 130)}
      {"".join(pales)}
      <rect x="0" y="{top+34}" width="{W}" height="9" fill="{SIL}"/>{rim(0, top+34, W, top+34)}
      <rect x="0" y="{GROUND-44}" width="{W}" height="9" fill="{SIL}"/>
      {ground()}'''
    return frame("gold", body, seed=5)


def electric():
    top = 322
    wires, insul = [], []
    for i in range(6):
        y = top + i * 18
        wires.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{SIL2}" stroke-width="2.4"/>')
        wires.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{RIM}" stroke-width=".8" opacity=".4"/>')
    for x in range(80, W, 160):
        for i in range(6):
            insul.append(f'<circle cx="{x}" cy="{top+i*18}" r="4" fill="{SIL}"/>')
    spark_x, spark_y = 520, top + 18
    spark = f'''<g><circle cx="{spark_x}" cy="{spark_y}" r="26" fill="url(#sunglow)" opacity=".9"/>
      <path d="M{spark_x} {spark_y-16} l4 10 10-2 -7 8 7 8 -10-2 -4 10 -4-10 -10 2 7-8 -7-8 10 2 z" fill="#ffe1a6"/></g>'''
    body = f'''{hills()}{acacia(660, GROUND, 1.0, True)}{birds(220, 110)}
      {"".join(wires)}{posts(range(80, W, 160), top-14, 8)}{"".join(insul)}{spark}
      {ground()}'''
    return frame("ember", body, seed=7)


def diamondmesh():
    top = 316
    mesh = f'''<pattern id="dm" width="26" height="26" patternUnits="userSpaceOnUse">
        <path d="M0 13 L13 0 L26 13 L13 26 Z" stroke="{SIL2}" stroke-width="2" fill="none"/></pattern>'''
    body = f'''<defs>{mesh}</defs>
      {hills()}{acacia(140, GROUND, 1.05)}{birds(600, 125)}
      <rect x="0" y="{top}" width="{W}" height="{GROUND-top}" fill="url(#dm)"/>
      <line x1="0" y1="{top}" x2="{W}" y2="{top}" stroke="{SIL2}" stroke-width="3"/>{rim(0, top, W, top)}
      {posts(range(70, W, 150), top-8)}
      {ground()}'''
    return frame("dawn", body, seed=9)


def kudu(x, y, s=1.0):
    """standing antelope silhouette"""
    return f'''<g transform="translate({x} {y}) scale({s})" fill="{SIL}">
      <path d="M0 0 C 6 -16 10 -26 24 -30 C 40 -34 58 -32 66 -26 C 74 -21 76 -12 74 -4
               L70 0 L66 -2 L62 22 L57 22 L54 0 L38 0 L34 22 L29 22 L26 -2
               C 16 -2 6 -2 0 0 Z"/>
      <path d="M64 -26 C 70 -34 74 -40 72 -50 M72 -50 C 76 -44 78 -36 74 -28"
            stroke="{SIL}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
      <path d="M66 -26 L78 -34 L80 -30 L70 -23 Z"/>
    </g>'''


def gamefence():
    top = 330
    wires, drops = [], []
    for i in range(7):
        y = top + i * 16
        wires.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{SIL2}" stroke-width="2"/>')
    for x in range(30, W, 34):
        drops.append(f'<line x1="{x}" y1="{top}" x2="{x}" y2="{GROUND-14}" stroke="{SIL2}" stroke-width="1.4" opacity=".8"/>')
    body = f'''{hills()}{acacia(600, 360, 1.5)}{acacia(90, 372, 1.0, True)}
      {kudu(360, 356, 1.1)}{birds(180, 100, 4)}
      {"".join(wires)}{"".join(drops)}{posts(range(60, W, 170), top-12, 9)}
      {ground()}'''
    return frame("amber", body, seed=11)


def razor():
    wall_top = 342
    coils = []
    for x in range(0, W + 30, 26):
        coils.append(f'<circle cx="{x}" cy="{wall_top-20}" r="19" stroke="{SIL2}" stroke-width="2.6" fill="none"/>')
        coils.append(f'<circle cx="{x}" cy="{wall_top-20}" r="19" stroke="{RIM}" stroke-width=".8" fill="none" opacity=".35"/>')
    blades = []
    rnd = random.Random(4)
    for x in range(0, W + 30, 26):
        a = rnd.uniform(0, math.pi)
        bx, by = x + 19 * math.cos(a), wall_top - 20 + 19 * math.sin(a)
        blades.append(f'<line x1="{bx:.0f}" y1="{by:.0f}" x2="{bx+4:.0f}" y2="{by-4:.0f}" stroke="{SIL2}" stroke-width="2"/>')
    bricks = f'''<pattern id="bw" width="46" height="24" patternUnits="userSpaceOnUse">
        <rect width="46" height="24" fill="{SIL2}"/>
        <path d="M0 12 H46 M23 0 V12 M0 12 M11 12 V24 M34 12 V24" stroke="#0c0f13" stroke-width="2"/></pattern>'''
    body = f'''<defs>{bricks}</defs>
      {hills()}{acacia(680, 350, 1.1, True)}{birds(120, 110)}
      <rect x="0" y="{wall_top}" width="{W}" height="{GROUND-wall_top}" fill="url(#bw)"/>
      {rim(0, wall_top, W, wall_top, 1.6, .45)}
      {"".join(coils)}{"".join(blades)}
      {ground()}'''
    return frame("mauve", body, seed=13)


def gates():
    top, gx = 296, 200
    bars = "".join(f'<line x1="{x}" y1="{top+18}" x2="{x}" y2="{GROUND-16}" stroke="{SIL2}" stroke-width="5"/>' for x in range(gx + 26, gx + 380, 24))
    body = f'''{hills()}{acacia(660, GROUND, 1.1, True)}{birds(560, 115)}
      <rect x="{gx-52}" y="{top-28}" width="44" height="{GROUND-top+28}" fill="{SIL}"/>
      <rect x="{gx-58}" y="{top-40}" width="56" height="14" rx="3" fill="{SIL}"/>{rim(gx-58, top-40, gx-2, top-40)}
      <rect x="{gx}" y="{top}" width="392" height="12" fill="{SIL2}"/>{rim(gx, top, gx+392, top)}
      <rect x="{gx}" y="{GROUND-16}" width="392" height="10" fill="{SIL2}"/>
      <rect x="{gx}" y="{top}" width="10" height="{GROUND-top-6}" fill="{SIL2}"/>
      <rect x="{gx+382}" y="{top}" width="10" height="{GROUND-top-6}" fill="{SIL2}"/>
      {bars}
      <line x1="{gx+6}" y1="{GROUND-20}" x2="{gx+386}" y2="{top+10}" stroke="{SIL2}" stroke-width="4" opacity=".85"/>
      <circle cx="{gx+60}" cy="{GROUND-2}" r="7" fill="{SIL}"/><circle cx="{gx+330}" cy="{GROUND-2}" r="7" fill="{SIL}"/>
      <line x1="{gx-60}" y1="{GROUND+5}" x2="{W}" y2="{GROUND+5}" stroke="{SIL2}" stroke-width="3"/>
      {ground()}'''
    return frame("gold", body, seed=15)


def steel():
    top = 250
    cols = [180, 620]
    web = []
    for i, x in enumerate(range(cols[0], cols[1], 55)):
        y1, y2 = (top + 26, top + 4) if i % 2 == 0 else (top + 4, top + 26)
        web.append(f'<line x1="{x}" y1="{y1}" x2="{x+55}" y2="{y2}" stroke="{SIL2}" stroke-width="4"/>')
    body = f'''{hills()}{acacia(80, GROUND, 1.0)}{birds(600, 105)}
      <rect x="{cols[0]-8}" y="{top-8}" width="{cols[1]-cols[0]+16}" height="12" fill="{SIL2}"/>{rim(cols[0]-8, top-8, cols[1]+8, top-8)}
      <rect x="{cols[0]-8}" y="{top+26}" width="{cols[1]-cols[0]+16}" height="8" fill="{SIL2}"/>
      {"".join(web)}
      <rect x="{cols[0]-8}" y="{top}" width="12" height="{GROUND-top}" fill="{SIL}"/>
      <rect x="{cols[1]-4}" y="{top}" width="12" height="{GROUND-top}" fill="{SIL}"/>
      <rect x="{cols[0]-20}" y="{GROUND-8}" width="36" height="8" fill="{SIL}"/>
      <rect x="{cols[1]-16}" y="{GROUND-8}" width="36" height="8" fill="{SIL}"/>
      {ground()}'''
    return frame("dawn", body, seed=17)


def welding():
    bx, by = 400, 360
    rnd = random.Random(21)
    sparks = []
    for i in range(26):
        a = rnd.uniform(-math.pi, 0.2)
        l = rnd.uniform(14, 66)
        x2, y2 = bx + l * math.cos(a), by + l * math.sin(a)
        sparks.append(f'<line x1="{bx}" y1="{by}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#ffd98f" stroke-width="{rnd.uniform(1,2.4):.1f}" opacity="{rnd.uniform(.4,.95):.2f}" stroke-linecap="round"/>')
    body = f'''{hills()}{acacia(670, GROUND, 1.05, True)}
      <rect x="120" y="{by-4}" width="560" height="10" fill="{SIL2}"/>{rim(120, by-4, 680, by-4, 1.4, .4)}
      <rect x="170" y="{by+6}" width="14" height="{GROUND-by-6}" fill="{SIL}"/>
      <rect x="616" y="{by+6}" width="14" height="{GROUND-by-6}" fill="{SIL}"/>
      <rect x="{bx+30}" y="{by-72}" width="12" height="70" fill="{SIL}" transform="rotate(24 {bx+36} {by-2})"/>
      <circle cx="{bx}" cy="{by}" r="60" fill="url(#sunglow)"/>
      {"".join(sparks)}
      <circle cx="{bx}" cy="{by}" r="9" fill="#fff3d6"/>
      {ground()}'''
    return frame("ember", body, seed=19)


def hero():
    w, h = 1600, 760
    global GROUND
    saved, GROUND = GROUND, 660
    top = 470
    mesh = f'''<pattern id="hm" width="10" height="22" patternUnits="userSpaceOnUse">
        <path d="M0 0V22 M0 0H10 M0 11H10" stroke="{SIL2}" stroke-width="1.5" opacity=".9"/></pattern>'''
    coils = "".join(
        f'<circle cx="{x}" cy="{top-24}" r="22" stroke="{SIL2}" stroke-width="2.6" fill="none"/>'
        f'<circle cx="{x}" cy="{top-24}" r="22" stroke="{RIM}" stroke-width=".8" fill="none" opacity=".3"/>'
        for x in range(0, w + 30, 30))
    hero_hills = (
        f'<path d="M0 520 Q 350 440 700 505 T 1600 488 V660 H0 Z" fill="#0d1016" opacity=".7"/>'
        f'<path d="M0 570 Q 480 505 900 556 T 1600 545 V660 H0 Z" fill="#0b0d12" opacity=".92"/>')
    body = f'''<defs>{mesh}</defs>
      {sun(1180, 430, 70)}{hero_hills}
      {acacia(210, 585, 2.1)}{acacia(1430, 570, 1.5, True)}{acacia(950, 560, 1.0)}
      {birds(660, 180, 5, 1.3)}{birds(1220, 240, 3, 1.0)}
      <rect x="0" y="{top}" width="{w}" height="{660-top}" fill="url(#hm)"/>
      <rect x="0" y="{top-6}" width="{w}" height="7" fill="{SIL2}"/>{rim(0, top-6, w, top-6)}
      {coils}
      {posts(range(80, w, 170), top-10, 8)}
      <rect x="0" y="660" width="{w}" height="{h-660}" fill="#090b0f"/>'''
    out = frame("gold", body, w=w, h=h, seed=2)
    GROUND = saved
    return out


SCENES = {
    "hero.svg": hero,
    "scene-clear-view-fence.svg": clearview,
    "scene-palisade-fence.svg": palisade,
    "scene-electric-fence.svg": electric,
    "scene-diamond-mesh-fence.svg": diamondmesh,
    "scene-game-field-fence.svg": gamefence,
    "scene-razor-wire.svg": razor,
    "scene-gates-fabrication.svg": gates,
    "scene-steel-structures.svg": steel,
    "scene-welding-steel-works.svg": welding,
}

# scenes with sun added where the body doesn't place one
SUNNED = {"scene-palisade-fence.svg": (640, 250, 40), "scene-clear-view-fence.svg": (170, 230, 34),
          "scene-diamond-mesh-fence.svg": (630, 220, 36), "scene-game-field-fence.svg": (140, 240, 46),
          "scene-razor-wire.svg": (560, 230, 38), "scene-gates-fabrication.svg": (100, 220, 40),
          "scene-steel-structures.svg": (700, 200, 36), "scene-electric-fence.svg": (150, 235, 42),
          "scene-welding-steel-works.svg": (90, 215, 30)}

for name, fn in SCENES.items():
    svg = fn()
    if name in SUNNED:
        x, y, r = SUNNED[name]
        svg = svg.replace("<defs>", "", 0)  # no-op keep simple
        # insert sun right after sky rect so silhouettes draw over it
        marker = 'fill="url(#sky)"/>'
        i = svg.index(marker) + len(marker)
        svg = svg[:i] + sun(x, y, r) + svg[i:]
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote", name, f"{len(svg)/1024:.1f} KB")
print("done")
