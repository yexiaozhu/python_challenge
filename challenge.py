#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu
import email
import re
import urllib
import wave
import StringIO
import os
import ossaudiodev

url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html'
src = urllib.urlopen(url).read()
c = re.compile("<!--\n(.*)\n-->", re.DOTALL)
data = c.findall(src)[0]
message = email.message_from_string(data)
audio = message.get_payload(0).get_payload(decode=True)
wav = wave.open(StringIO.StringIO(audio))
print wav
print wav.getsampwidth() # 2 bytes, 16bits
format = ossaudiodev.AFMT_S16_BE # Big Endian
channels = 2
dsp = ossaudiodev.open('w')
dsp.setparameters(format, channels, wav.getframerate())
dsp.write(audio)
