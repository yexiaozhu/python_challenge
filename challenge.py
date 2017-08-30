#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

import Image, ImageDraw, ImageSequence
img = Image.open('white.gif')
new = Image.new('RGB', (200, 200), 'black')
newimg = ImageDraw.Draw(new)
x = 0
y = 0
for s in ImageSequence.Iterator(img):
    l,u,r,d = img.getbbox()
    dx = (l - 100)
    dy = (u - 100)
    x += dx
    y += dy
    if dx == dy == 0:
        x += 30
        y += 30
    newimg.point((x, y))
new.save('out22.png')