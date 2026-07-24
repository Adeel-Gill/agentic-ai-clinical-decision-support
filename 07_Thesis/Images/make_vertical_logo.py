#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Regenerate the vertical (stacked) Superior University logo used on the thesis
title page, derived from the official horizontal asset (superior_logo.png).

Output: superior_logo_vertical.png
  - network icon on top
  - single-line "SUPERIOR UNIVERSITY" wordmark below (logo purple, Times New Roman)
  - transparent canvas padded to a 5:7.43 (width:height) aspect ratio so the
    title page can place it at exactly 5 cm x 7.43 cm with NO distortion.

Run:  python make_vertical_logo.py
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "superior_logo.png")
OUT = os.path.join(HERE, "superior_logo_vertical.png")

PURPLE = (112, 26, 115)          # sampled from the official mark
TARGET_ICON_W = 560              # px; ~285 dpi when printed at 5 cm wide
ASPECT_W, ASPECT_H = 5.0, 7.43   # title-page box (cm) -> canvas aspect ratio
FONT_PATH = r"C:\Windows\Fonts\times.ttf"


def main():
    im = Image.open(SRC).convert("RGBA")
    a = np.array(im)
    rgb = a[:, :, :3].astype(int)
    alpha = a[:, :, 3]
    ink = (rgb.sum(axis=2) < 720) & (alpha > 10)

    # --- crop the circular icon (left square region of the horizontal logo) ---
    region = ink[:, 0:200]
    ys = np.where(region.any(axis=1))[0]
    xs = np.where(region.any(axis=0))[0]
    icon = im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    scale = TARGET_ICON_W / icon.width
    icon = icon.resize((TARGET_ICON_W, round(icon.height * scale)), Image.LANCZOS)

    # --- render the wordmark as a single crisp line sized to the icon width ---
    text = "SUPERIOR UNIVERSITY"
    size = 10
    while True:
        f = ImageFont.truetype(FONT_PATH, size)
        w = f.getbbox(text)[2] - f.getbbox(text)[0]
        if w >= TARGET_ICON_W or size > 800:
            break
        size += 2
    f = ImageFont.truetype(FONT_PATH, size)
    bb = f.getbbox(text)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    word = Image.new("RGBA", (tw + 6, th + 6), (255, 255, 255, 0))
    ImageDraw.Draw(word).text((-bb[0] + 3, -bb[1] + 3), text, font=f, fill=PURPLE + (255,))

    # --- stack icon + wordmark ---
    pad = round(TARGET_ICON_W * 0.05)
    gap = round(TARGET_ICON_W * 0.11)
    content_w = max(icon.width, word.width) + 2 * pad
    content_h = pad + icon.height + gap + word.height + pad

    # --- pad to the 5:7.43 target aspect so Word never stretches the artwork ---
    target_aspect = ASPECT_W / ASPECT_H
    canvas_w = content_w
    canvas_h = round(canvas_w / target_aspect)
    if canvas_h < content_h:                       # content taller than box -> widen
        canvas_h = content_h
        canvas_w = round(canvas_h * target_aspect)

    canvas = Image.new("RGBA", (canvas_w, canvas_h), (255, 255, 255, 0))
    top = (canvas_h - content_h) // 2 + pad
    canvas.paste(icon, ((canvas_w - icon.width) // 2, top), icon)
    canvas.paste(word, ((canvas_w - word.width) // 2, top + icon.height + gap), word)

    canvas.save(OUT)
    print("saved", OUT, canvas.size, "aspect=%.4f" % (canvas_w / canvas_h))


if __name__ == "__main__":
    main()
