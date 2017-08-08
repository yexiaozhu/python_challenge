#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu
import re

start_url = "http://www.pythonchallenge.com/pc/def/oxygen.html"

from PIL import Image
img = Image.open('oxygen.png')
# data = [img.getpixel((i, 43)) for i in range(0, 609)]
data = [chr(img.getpixel((i, 50))[0]) for i in range(0, 609, 7)]
# print data
# print ''.join(data)
result = ''.join(data)
print result
print type(result)
data = re.findall(r'\d+', result)
print data
# print type(data)
list = []
for i in data:
    # print int(i)
    list.append(int(i))
print list
passcodes = ''.join([chr(j) for j in list])
end_url =  start_url.replace('oxygen', passcodes)
print end_url