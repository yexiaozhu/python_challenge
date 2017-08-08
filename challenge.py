#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

import re
def describe(s):
    sets = re.findall("(1+|2+|3+)", s)
    return "".join([str(len(x))+x[0] for x in sets])
s = '1'
for i in range(30):
    s = describe(s)
    print s
    print len(s)
# print s
# print len(s)
passcodes = str(len(s))
start_url = 'http://www.pythonchallenge.com/pc/return/bull.html'
end_url = start_url.replace('bull', passcodes)
print end_url
