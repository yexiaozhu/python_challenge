#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu
import re

start_url = "http://www.pythonchallenge.com/pc/def/integrity.html"

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
import bz2
print 'username:', bz2.decompress(un)
print 'password:', bz2.decompress(pw)