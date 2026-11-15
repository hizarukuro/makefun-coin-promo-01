#!/usr/bin/env python3
"""Draw BountyBot's logo: one bold robot head on a plain field.

The judge sees the coin's logo fitted within 512 px a side, and pump.fun
traders see it as a thumbnail, so the design rules are: ONE subject, a thick
dark outline, high contrast, a plain background, nothing that only reads at
full size. BountyBot is a bounty-hunting robot: a signal-yellow head, a cyan
visor with two eyes, and an antenna topped with the gold coin it is hunting.

Output: logo.png, 1024x1024 PNG (well under pump.fun's 5 MiB / 16 MP limits).
Everything is drawn with PIL shapes — no external assets.
"""

from PIL import Image, ImageDraw

S = 1024
NAVY = (13, 20, 43)        # plain deep-navy field
YELLOW = (255, 196, 0)     # signal yellow head
DARK = (16, 18, 24)        # outline / visor
CYAN = (64, 224, 255)      # glowing eyes
GOLD = (255, 170, 0)       # the hunted coin
GOLD_DARK = (184, 116, 0)
WHITE = (245, 247, 250)

img = Image.new("RGB", (S, S), NAVY)
d = ImageDraw.Draw(img)

# --- antenna: stalk + the gold coin BountyBot is hunting ---
d.rectangle([492, 96, 532, 240], fill=DARK)
d.ellipse([412, 16, 612, 216], fill=GOLD, outline=DARK, width=14)
d.ellipse([444, 48, 580, 184], outline=GOLD_DARK, width=10)
# a bold "$" suggested by two strokes is fiddly at thumbnail size; a star
# reads cleaner and still says "prize".
cx, cy, r = 512, 116, 44
pts = []
import math
for i in range(10):
    ang = -math.pi / 2 + i * math.pi / 5
    rad = r if i % 2 == 0 else r * 0.45
    pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
d.polygon(pts, fill=DARK)

# --- ears / side bolts ---
d.rounded_rectangle([96, 430, 196, 640], radius=36, fill=DARK)
d.rounded_rectangle([828, 430, 928, 640], radius=36, fill=DARK)

# --- head: big rounded square, thick dark outline ---
d.rounded_rectangle([156, 220, 868, 884], radius=120, fill=YELLOW, outline=DARK, width=22)

# --- visor: one dark band with two glowing eyes ---
d.rounded_rectangle([248, 400, 776, 590], radius=90, fill=DARK)
d.ellipse([330, 452, 442, 564], fill=CYAN)
d.ellipse([582, 452, 694, 564], fill=CYAN)
d.ellipse([362, 476, 410, 524], fill=WHITE)
d.ellipse([614, 476, 662, 524], fill=WHITE)

# --- mouth: a determined flat line with two notches ---
d.rounded_rectangle([402, 692, 622, 724], radius=16, fill=DARK)
d.rectangle([452, 724, 470, 748], fill=DARK)
d.rectangle([554, 724, 572, 748], fill=DARK)

# --- chin badge: a small coin dot, echoing the antenna ---
d.ellipse([472, 780, 552, 860], fill=GOLD, outline=DARK, width=10)

img.save("logo.png", optimize=True)
print("logo.png written")
