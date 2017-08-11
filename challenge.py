#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

# import re, bz2, urllib2, urllib, cookielib
#
# info = []
# cookies = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
# urllib2.install_opener(opener)
#
# nothing = str(12345)
# for i in range(400):
#     path = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
#     text = urllib.urlopen(path + nothing).read()
#     r = urllib2.Request(path + nothing)
#     yy = str(urllib2.urlopen(r).info())
#     info.append((re.findall('info=(.{0,4});', yy)))
#     a = re.findall(r'(\d+)', text)
#     print i, text ,info
#     if a == []:
#         break
#     nothing = str(a[len(a) - 1])
#
# s = ''.join([k for i in info for k in i])
# print s
# print bz2.decompress(urllib.unquote_plus(s))
from urllib2 import Request, urlopen
from urllib import quote_plus

info = 'the flowers are on their way'
url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
req = Request(url, headers={'Cookie': 'info=' + quote_plus(info)})
print urlopen(req).read()
start_url = 'http://www.pythonchallenge.com/pc/return/romance.html'
# end_url = start_url.replace('bull', passcodes)
# print end_url
