"""Make the card-reel backgrounds and mask used by build_card_reel.py.

work/card_bg_cream.png  1080x1920 cream (238,221,199) with a white 10 px frame around the card and a soft shadow
work/card_bg_black.png  1080x1920 black with a faint 108 px grid, same white frame and shadow
work/card_mask.png      936x1248 greyscale mask with rounded corners (r=36) for the footage
Card position: 936x1248 at (72, 592); the white frame spans (62, 582)-(1018, 1850).
The halo is a close, not pixel-exact, recreation of the reference ad's backgrounds.
Usage (inside the ad folder): python make_card_assets.py   (render_card_reel.sh runs it if work/card_mask.png is missing)
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).parent
W, H = 1080, 1920
CARD = (72, 592, 936, 1248)
FRAME_PAD, RADIUS = 10, 36


def frame_layer(bg, glow):
    """White frame around the card with a soft halo: a dark shadow on cream, a warm orange glow on black."""
    x, y, w, h = CARD
    box = (x - FRAME_PAD, y - FRAME_PAD, x + w + FRAME_PAD, y + h + FRAME_PAD)
    halo = Image.new("L", (W, H), 0)
    ImageDraw.Draw(halo).rounded_rectangle((box[0] - 4, box[1] - 2, box[2] + 4, box[3] + 8), RADIUS + 8, fill=110)
    halo = halo.filter(ImageFilter.GaussianBlur(16))
    bg.paste(glow, (0, 0), halo)
    ImageDraw.Draw(bg).rounded_rectangle(box, RADIUS + FRAME_PAD, fill=(255, 255, 255))
    return bg


def main():
    out = HERE / "work"
    out.mkdir(exist_ok=True)
    cream = Image.new("RGB", (W, H), (238, 221, 199))
    frame_layer(cream, (150, 120, 95)).save(out / "card_bg_cream.png")

    black = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(black)
    for v in range(0, W, 108):
        d.rectangle((v, 0, v + 1, H), fill=(22, 22, 22))
    for v in range(0, H, 108):
        d.rectangle((0, v, W, v + 1), fill=(22, 22, 22))
    frame_layer(black, (120, 40, 12)).save(out / "card_bg_black.png")

    mask = Image.new("L", (CARD[2], CARD[3]), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, CARD[2] - 1, CARD[3] - 1), RADIUS, fill=255)
    mask.save(out / "card_mask.png")
    print("wrote", ", ".join(p.name for p in sorted(out.glob("card_*.png"))))


if __name__ == "__main__":
    main()
