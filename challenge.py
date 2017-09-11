#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu
import Image
import re
import urllib

start_url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.html"

# <font color="gold">
# 	<br>The picture is only meant to help you relax
# 	     <!-- while you look at the csv file -->
# </font>
url = 'http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.csv'
data = re.findall(r"[\d.]+", urllib.urlopen(url).read())
print len(data)
new = Image.new('F',(53,139))
new.putdata(map(float,data))
new = new.transpose(Image.ROTATE_90)
new = new.transpose(Image.FLIP_TOP_BOTTOM)
new.save(r'out30.tiff')

s = [chr(int(data[i][5]+data[i+1][5]+data[i+2][6])) for i in range(0,len(data)-2,3)]
print ''.join(s)