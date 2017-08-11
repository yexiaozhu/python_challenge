#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

import Image

im = Image.open('wire.png')
new = Image.new('RGB', (100, 100), 'black')

count = 0
flag = 0
max = 99
line = 1
x = 0
y = 0
for i in range(10000):
    new.putpixel((x, y), im.getpixel((count, 0)))
    if (flag == 0):
        x += 1
    elif flag == 1:
        y += 1
    elif flag == 2:
        x -= 1
    else:
        y -= 1

    if (line == max):
        flag += 1
        line = 1
        if flag == 4:
            flag = 0
            max -= 2
            y += 1
            x += 1
    else:
        line += 1

    count += 1

new.save('out14.png')

start_url = 'http://www.pythonchallenge.com/pc/return/italy.html'
# end_url = start_url.replace('bull', passcodes)
# print end_url
