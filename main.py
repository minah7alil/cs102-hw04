import random
import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

new_img = Image.new("RGB", (width, height), "white")


for i in range(20, width - 20):
    for j in range(20, height - 20):
        R, G, B = img.getpixel((i,j))
        if R > 10:
            R = R + 10
        if G > 10:
            G = G + 180
        if B > 10:
            B = B + 10
        new_img.putpixel((i, j), (R, G, B))
new_img.save(output_path)
exit(print(f"Lets make the world more green"))
