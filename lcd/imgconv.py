#!/usr/bin/env python
import Image
im = Image.open('face.png')
ic = im.getdata()
b = []
for row in range(0, 64, 8):
    for col in range(0, 102):
        b.append(sum([0 if ic.getpixel((col, row + p)) else 1 << p for p in range(0, 8)]))
print ', '.join([hex(c) for c in b])
