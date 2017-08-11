#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

import Image

im = Image.open("mozart.gif")
for y in range(im.size[1]):
    #获得像素点
    line=[im.getpixel((x, y)) for x in range(im.size[0])]
    idx=line.index(195)
    line=line[idx:]+line[:idx]
    #重新排列像素点
    [im.putpixel((x, y),line[x]) for x in range(len(line))]

im.show()

start_url = 'http://www.pythonchallenge.com/pc/return/mozart.html'
# end_url = start_url.replace('bull', passcodes)
# print end_url
