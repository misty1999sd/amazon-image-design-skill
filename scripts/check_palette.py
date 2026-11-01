"""Numeric acceptance probe for reference-locked product rebuilds.

Prints one JSON line per image with the checks used by
references/product-fidelity-banana-workflow.md. Read-only: it never writes,
resamples or modifies the image.

Usage:
    python check_palette.py IMAGE [IMAGE ...]
    python check_palette.py --scan 3400,3700,3950 IMAGE      # dark run widths per row
"""

import argparse
import json
import sys

import numpy as np
from PIL import Image


def neutral_mask(rgb):
    mx = rgb.max(2)
    mn = rgb.min(2)
    sat = (mx - mn) / np.maximum(mx, 1.0)
    return (sat < 0.06) & (mx < 235) & (mx > 25)


def measure(path):
    im = Image.open(path)
    size = im.size
    rgb = np.asarray(im.convert("RGB")).astype(np.float32)
    lum = rgb.mean(2)

    m = neutral_mask(rgb)
    if m.sum() > 1000:
        r = rgb[..., 0][m].mean()
        g = rgb[..., 1][m].mean()
        b = rgb[..., 2][m].mean()
        green_deficit = g - (r + b) / 2.0
        rb = r - b
    else:
        r = g = b = green_deficit = rb = float("nan")

    band = max(8, int(round(min(size) * 0.01)))
    edges = np.concatenate(
        [
            rgb[:band].reshape(-1, 3),
            rgb[-band:].reshape(-1, 3),
            rgb[:, :band].reshape(-1, 3),
            rgb[:, -band:].reshape(-1, 3),
        ]
    )
    edge_pure = float((edges > 250).all(1).mean())

    ys, xs = np.nonzero(lum < 245)
    if ys.size:
        top, bottom = int(ys.min()), int(size[1] - 1 - ys.max())
        left, right = int(xs.min()), int(size[0] - 1 - xs.max())
    else:
        top = bottom = left = right = -1

    w, h = size
    return {
        "path": path,
        "size": f"{w}x{h}",
        "neutral_px": int(m.sum()),
        "mean_rgb": [round(float(r), 1), round(float(g), 1), round(float(b), 1)],
        "green_deficit": round(float(green_deficit), 2),
        "r_minus_b": round(float(rb), 2),
        "edge_pure": round(edge_pure, 3),
        "margins_pct": {
            "top": round(100.0 * top / h, 2) if top >= 0 else -1,
            "bottom": round(100.0 * bottom / h, 2) if bottom >= 0 else -1,
            "left": round(100.0 * left / w, 2) if left >= 0 else -1,
            "right": round(100.0 * right / w, 2) if right >= 0 else -1,
        },
        "true_black": round(float((lum < 30).mean()), 4),
        "mid_grey": round(float(((lum >= 120) & (lum < 180)).mean()), 4),
    }


def scan(path, rows):
    im = Image.open(path).convert("L")
    lum = np.asarray(im).astype(np.float32)
    h, w = lum.shape
    out = {"path": path, "size": f"{w}x{h}", "rows": {}}
    for y in rows:
        if not 0 <= y < h:
            continue
        row = lum[y]
        mask = row < 150
        runs = []
        start = None
        for x, v in enumerate(mask):
            if v and start is None:
                start = x
            elif not v and start is not None:
                runs.append([start, x - 1, x - start])
                start = None
        if start is not None:
            runs.append([start, w - 1, w - start])
        out["rows"][y] = [r for r in runs if r[2] >= 4][:14]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("images", nargs="+")
    ap.add_argument("--scan", default="", help="comma separated rows for dark-run widths")
    args = ap.parse_args()

    rows = [int(v) for v in args.scan.split(",") if v.strip()] if args.scan else []
    rc = 0
    for path in args.images:
        try:
            if rows:
                print(json.dumps(scan(path, rows), ensure_ascii=False))
            else:
                print(json.dumps(measure(path), ensure_ascii=False))
        except Exception as exc:
            print(json.dumps({"path": path, "error": f"{type(exc).__name__}: {exc}"}))
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
