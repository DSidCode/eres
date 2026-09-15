import sys
from PIL import Image

file = "geminis.jpg"
img = Image.open(f"assets/constellations/{file}")
w, h = img.size
pixels = [
    img.getpixel((w//4, h//4)),
    img.getpixel((w//4, 3*h//4)),
    img.getpixel((3*w//4, h//4)),
    img.getpixel((3*w//4, 3*h//4))
]
print(f"{file} mid-background pixels: {pixels}")
