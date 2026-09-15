import sys
from PIL import Image

for file in ["cassiopea.jpg", "geminis.jpg", "orion.jpg", "osamayor.jpg", "escorpio.jpg"]:
    try:
        img = Image.open(f"assets/constellations/{file}")
        w, h = img.size
        
        # sample a 10px border around the image to find the maximum background luminance
        max_lum = 0
        for x in range(w):
            for y in range(h):
                if x < 10 or x > w - 10 or y < 10 or y > h - 10:
                    r,g,b = img.getpixel((x, y))
                    lum = max(r,g,b)
                    if lum > max_lum:
                        max_lum = lum
        print(f"{file} max border luminance: {max_lum}")
    except Exception as e:
        pass
