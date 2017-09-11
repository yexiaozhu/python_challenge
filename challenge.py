#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

start_url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html"

import urllib, bz2

f = urllib.urlopen(start_url)
s = [chr(len(i)-1) for i in f.readlines()[12::]]
text = ''.join(s)
print bz2.decompress(text)