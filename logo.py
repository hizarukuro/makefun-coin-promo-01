#!/usr/bin/env python3
"""Draw the BountyBot logo: one bold robot head on a plain field.

Why it looks the way it does: the judge sees this image fitted inside
512 px a side and pump.fun traders see it as a small thumbnail, so the
rules are one subject, a thick dark outline, high contrast, a plain
background, and nothing that only reads at full size. BountyBot is a
bounty-hunting robot — signal-yellow head, cyan visor with two eyes,
and an antenna topped with the gold coin it is hunting.

Output: logo.png, a 1024x1024 PNG (pump.fun allows up to 5 MiB and
16 megapixels). Drawn entirely with PIL shapes; no external assets.
The drawing calls below are the launch session's own rendering of the
design in COIN.md, and their output is byte-for-byte the image the coin
was launched with.
"""

import math

from PIL import Image, ImageDraw

SIZE = 1024

# The palette: a deep-navy field so the yellow head carries the contrast.
FIELD = (13, 20, 43)
HEAD_YELLOW = (255, 196, 0)
INK = (16, 18, 24)          # outlines, visor, features
EYE_CYAN = (64, 224, 255)
COIN_GOLD = (255, 170, 0)
COIN_SHADE = (184, 116, 0)
EYE_GLINT = (245, 247, 250)


def star_points(cx, cy, r):
    """A ten-point star outline (five outer tips, five inner) at (cx, cy)."""
    pts = []
    for i in range(10):
        ang = -math.pi / 2 + i * math.pi / 5
        rad = r if i % 2 == 0 else r * 0.45
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    return pts


def draw_bountybot(d):
    # Antenna: a stalk topped by the gold coin BountyBot hunts. The coin
    # carries a star — a "$" built from strokes turns to mush at thumbnail
    # size, while a star still reads as "prize".
    d.rectangle([492, 96, 532, 240], fill=INK)
    d.ellipse([412, 16, 612, 216], fill=COIN_GOLD, outline=INK, width=14)
    d.ellipse([444, 48, 580, 184], outline=COIN_SHADE, width=10)
    d.polygon(star_points(512, 116, 44), fill=INK)

    # Side bolts / ears.
    d.rounded_rectangle([96, 430, 196, 640], radius=36, fill=INK)
    d.rounded_rectangle([828, 430, 928, 640], radius=36, fill=INK)

    # The head: one big rounded square with a thick dark outline.
    d.rounded_rectangle([156, 220, 868, 884], radius=120,
                        fill=HEAD_YELLOW, outline=INK, width=22)

    # Visor: a single dark band holding two glowing eyes with glints.
    d.rounded_rectangle([248, 400, 776, 590], radius=90, fill=INK)
    d.ellipse([330, 452, 442, 564], fill=EYE_CYAN)
    d.ellipse([582, 452, 694, 564], fill=EYE_CYAN)
    d.ellipse([362, 476, 410, 524], fill=EYE_GLINT)
    d.ellipse([614, 476, 662, 524], fill=EYE_GLINT)

    # Mouth: a determined flat line, notched twice.
    d.rounded_rectangle([402, 692, 622, 724], radius=16, fill=INK)
    d.rectangle([452, 724, 470, 748], fill=INK)
    d.rectangle([554, 724, 572, 748], fill=INK)

    # Chin badge: a small coin dot echoing the antenna's prize.
    d.ellipse([472, 780, 552, 860], fill=COIN_GOLD, outline=INK, width=10)


def main():
    img = Image.new("RGB", (SIZE, SIZE), FIELD)
    draw_bountybot(ImageDraw.Draw(img))
    img.save("logo.png", optimize=True)
    print("logo.png written")


if __name__ == "__main__":
    main()
