#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw " \
      "fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. " \
      "lmu ynnjw ml rfc spj."

def str_2(s):
    ans = ''
    for c in s:
        if c.isalpha():
            tmp = ord(c) + 2
            if tmp > ord('z'):
                tmp -= 26
            ans += chr(tmp)
        else:
            ans += c
    return ans
print str_2(str)
print str_2('map')
start_url = 'http://www.pythonchallenge.com/pc/def/map.html'
end_url = start_url.replace('map', str_2('map'))
print end_url