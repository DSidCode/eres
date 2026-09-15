import sys
from PIL import Image

img = Image.open('/tmp/butterfly_test.png')
pixels = list(img.getdata())
count = sum(1 for p in pixels if p[0] > 200 and p[1] > 200 and p[2] < 150)
print(f"Yellow pixels count: {count}")
