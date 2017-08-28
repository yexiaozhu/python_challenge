#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

import zlib
import binascii
import bz2
from zlib import decompress
from bz2 import BZ2Decompressor

zh = 'x\x9c'
bh = 'BZ'

result = []

f = open('package.pack', 'rb')
s = f.read()

while True:
        h = s[:2]
        if h == zh:
                s = decompress(s)
                result.append(' ')
        elif h == bh:
                s = BZ2Decompressor().decompress(s)
                result.append('#')
        elif s[-1:-3:-1] in [zh, bh]:
                s = s[::-1]
                result.append('\n')
        else:
                break
print ''.join(result)