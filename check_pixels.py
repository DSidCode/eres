import sys
from PIL import Image

for file in ["cassiopea.jpg", "geminis.jpg", "orion.jpg", "osamayor.jpg", "escorpio.jpg"]:
    try:
        img = Image.open(f"assets/constellations/{file}")
        w, h = img.size
        pixels = [
            img.getpixel((0, 0)),
            img.getpixel((w-1, 0)),
            img.getpixel((0, h-1)),
            img.getpixel((w-1, h-1)),
            img.getpixel((w//2, 10)),
            img.getpixel((10, h//2))
        ]
        print(f"{file} edge pixels: {pixels}")
    except Exception as e:
        print(f"Error reading {file}: {e}")
