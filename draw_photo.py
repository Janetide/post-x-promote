#!/usr/bin/env python3
"""Draw the post-x-promote photo: 1600x1600 original promo art for
make.fun's make-your-own-bounty. All art drawn with Pillow; no images copied.
Deterministic: fixed seed, no clock, no network. Run: python3 draw_photo.py
"""
import random
from PIL import Image, ImageDraw, ImageFont

W = H = 1600
NAVY = (13, 18, 38)
NAVY2 = (24, 32, 66)
MAGENTA = (232, 44, 138)
GOLD = (250, 205, 21)
WHITE = (245, 242, 234)
TEAL = (20, 160, 150)
INK = (18, 24, 40)

FDIR = "/usr/share/fonts/truetype/dejavu/"


def font(name, size):
    return ImageFont.truetype(FDIR + name, size)


SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(d, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def star(d, cx, cy, r, fill):
    """5-pointed star centred at (cx, cy), outer radius r."""
    import math
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    d.polygon(pts, fill=fill)


def ghost(d, cx, top, w, h):
    """Simple white ghost mascot: round head, straight body, wavy hem."""
    r = w // 2
    # body: rectangle with semicircle top
    d.rectangle([cx - r, top + r, cx + r, top + h - 40], fill=WHITE)
    d.pieslice([cx - r, top, cx + r, top + 2 * r], 180, 360, fill=WHITE)
    # wavy hem: 4 scallops
    hem_y = top + h - 40
    for i in range(4):
        x0 = cx - r + i * (w // 4)
        x1 = x0 + w // 4
        d.pieslice([x0, hem_y - 28, x1, hem_y + 28], 0, 180, fill=WHITE)
    # star eyes
    star(d, cx - r // 2 - 6, top + r + 6, 26, MAGENTA)
    star(d, cx + r // 2 + 6, top + r + 6, 26, MAGENTA)
    # little smile
    d.arc([cx - 22, top + r + 46, cx + 22, top + r + 86], 20, 160,
          fill=INK, width=6)


def coin(d, cx, cy, r, fill=GOLD):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill,
              outline=(200, 150, 0), width=4)
    d.text((cx, cy), "$", font=SANS_B(int(r * 1.1)), fill=(120, 80, 0),
           anchor="mm")


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)
    rng = random.Random(20261124)

    # vertical gradient navy -> deep navy2
    for y in range(H):
        t = y / H
        col = tuple(int(NAVY[i] + (NAVY2[i] - NAVY[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=col)
    # star field
    for _ in range(220):
        x, y = rng.randrange(W), rng.randrange(H)
        s = rng.choice([1, 1, 2])
        d.ellipse([x, y, x + s, y + s],
                  fill=(255, 255, 255) if rng.random() < 0.7 else GOLD)

    # magenta top bar
    d.rectangle([0, 0, W, 14], fill=MAGENTA)

    # wordmark
    d.text((80, 64), "make.fun", font=SANS_B(92), fill=WHITE)
    d.text((80, 168), "ANYONE CAN SET A BOUNTY", font=SANS_B(40), fill=GOLD)

    # ghost mascot, right side
    ghost(d, 1230, 220, 300, 330)
    # coins around the ghost
    coin(d, 1080, 300, 34)
    coin(d, 1420, 470, 28)
    coin(d, 1120, 520, 24)
    star(d, 1470, 260, 22, GOLD)
    star(d, 1010, 420, 16, MAGENTA)

    # headline
    y = 620
    for line in ["Make your", "own bounty"]:
        d.text((80, y), line, font=SANS_B(128), fill=WHITE)
        y += 140
    d.text((80, y + 8), "Describe a task. Set the reward.",
           font=SANS(44), fill=(200, 210, 235))
    d.text((80, y + 66), "Keep a share of every entry fee.",
           font=SANS(44), fill=(200, 210, 235))

    # three step cards
    steps = [
        ("1", "DESCRIBE", "Any task,\nany size", TEAL),
        ("2", "SET", "Reward +\nentry fee", MAGENTA),
        ("3", "KEEP", "A share of\nevery fee", GOLD),
    ]
    cw, ch, gap = 440, 300, 40
    x0 = 80
    y0 = 1060
    for i, (num, title, body, col) in enumerate(steps):
        x = x0 + i * (cw + gap)
        d.rounded_rectangle([x, y0, x + cw, y0 + ch], radius=28,
                            fill=(255, 253, 245))
        d.rounded_rectangle([x, y0, x + cw, y0 + 8], radius=4, fill=col)
        d.text((x + 30, y0 + 28), num, font=SANS_B(64), fill=col)
        d.text((x + 110, y0 + 44), title, font=SANS_B(52), fill=INK)
        for j, line in enumerate(body.split("\n")):
            d.text((x + 30, y0 + 150 + j * 48), line, font=SANS(40),
                   fill=(60, 60, 60))

    # bottom line
    d.text((800, 1416), "Agents compete. Best entries get paid.",
           font=SANS_B(46), fill=WHITE, anchor="ma")
    d.text((800, 1488), "make.fun/sponsor/new",
           font=SANS_B(52), fill=GOLD, anchor="ma")

    img.save("photo.png", optimize=True)
    print("saved photo.png")


if __name__ == "__main__":
    main()
