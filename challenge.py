#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

import Image
from cStringIO import StringIO

s= open("evil2.gfx", "rb").read()
for i in range(5):
    piece = s[i::5]
    im = Image.open(StringIO(piece))
    f = open("%d.%s" %(i, im.format.lower()), "wb")
    f.write(piece)
    f.close()

start_url = 'http://www.pythonchallenge.com/pc/return/evil.html'
# end_url = start_url.replace('bull', passcodes)
# print end_url
