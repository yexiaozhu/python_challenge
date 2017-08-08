#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

start_url = "http://www.pythonchallenge.com/pc/def/channel.html"

import zipfile as zf
zfp = zf.ZipFile('channel.zip')
nothing = '90052'
li = []
while True:
    try:
        fp = zfp.open(nothing+'.txt', 'r')
        text = fp.read().decode()
        nothing = text.split()[-1]
        li.append(zfp.getinfo(nothing+'.txt').comment.decode())
        fp.close()
    except KeyError:
        print 'It"s time to check manually'
        break
print ''.join(li)