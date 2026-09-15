import sys
from PIL import Image

file = "geminis.jpg"
img = Image.open(f"assets/constellations/{file}")
pixels = list(img.getdata())
max_lum = max(max(r,g,b) for r,g,b in pixels)
print(f"{file} max luminance: {max_lum}")

count_above_60 = sum(1 for r,g,b in pixels if max(r,g,b) > 60)
print(f"Pixels above 60 lum: {count_above_60} / {len(pixels)}")
