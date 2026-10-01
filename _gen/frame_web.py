#!/usr/bin/env python3
"""Frame the raw simulator captures in _gen/raw/ in an iPhone shell and export WebP to
assets/guides/. Shell geometry copied from AlarmPlanner's website/_gen/frame_web.py (the
version whose side buttons don't clip). Raw captures: iPhone 17 sim, 1206x2622, light mode,
status bar overridden to 9:41. Run: python3 _gen/frame_web.py"""
import os
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "..", "assets", "guides")
FINAL = (640, 1384)          # keeps the 1206x2622 capture's aspect inside the shell
SCREEN_R_RATIO, BEZEL_RATIO, RIM_RATIO = 0.145, 0.030, 0.011
RIM_COLOR = (0x2C, 0x2C, 0x2D, 255)

def shell_with_buttons(img):
    img = img.convert("RGBA")
    sw, height = img.size
    scr_r = int(sw * SCREEN_R_RATIO); bez = max(6, int(sw * BEZEL_RATIO))
    rimw = max(2, int(sw * RIM_RATIO)); bwid = max(3, rimw * 2)
    fw, fh = sw + (bez + rimw) * 2, height + (bez + rimw) * 2
    W, H = fw + bwid * 2, fh
    ox = bwid
    out = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(out)
    unit = fh / 100
    for y0, y1 in [(20, 26), (30, 40), (42, 52)]:
        d.rounded_rectangle([2, int(unit * y0), ox + 2, int(unit * y1)], radius=bwid // 2, fill=RIM_COLOR)
    d.rounded_rectangle([ox + fw - 2, int(unit * 33), W - 2, int(unit * 50)], radius=bwid // 2, fill=RIM_COLOR)
    d.rounded_rectangle([(ox, 0), (ox + fw - 1, fh - 1)], radius=scr_r + bez + rimw, fill=RIM_COLOR)
    d.rounded_rectangle([(ox + rimw, rimw), (ox + fw - rimw - 1, fh - rimw - 1)], radius=scr_r + bez, fill=(8, 8, 10, 255))
    m = Image.new("L", img.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([(0, 0), img.size], radius=scr_r, fill=255)
    img.putalpha(m)
    out.paste(img, (ox + bez + rimw, bez + rimw), img)
    return out

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for f in sorted(os.listdir(RAW)):
        if not f.endswith(".png"): continue
        framed = shell_with_buttons(Image.open(os.path.join(RAW, f)))
        w = FINAL[0]; h = round(framed.size[1] * w / framed.size[0])
        framed = framed.resize((w, h), Image.LANCZOS)
        path = os.path.join(OUT, f.replace(".png", ".webp"))
        framed.save(path, "WEBP", quality=82, method=6)
        print(f"{os.path.basename(path)}  {w}x{h}  {os.path.getsize(path)//1024}KB")
