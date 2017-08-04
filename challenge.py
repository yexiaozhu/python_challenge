#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu
import urllib
from urllib import *
import re
import os


def read(nothing):
    try:
        head = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
        s = urllib.urlopen(head + nothing).read()
        print s
        # 使用正则表达式匹配抓取到的页面中的最后一个数字
        pat = re.compile('([0-9]+)')
        nothing = re.findall(pat, s)[-1]
        # 返回函数本身 使函数一直执行下去
        return read(nothing)
    except:
        if 'Divide' in s:
            return read(str(int(nothing) / 2))
        else:
            pass


if __name__ == '__main__':
    read('12345')
    # start_url = 'http://www.pythonchallenge.com/pc/def/'
    # end_url = start_url + str(s)
    # print end_url
    raw_input('<PRESS ENTER>')

# end_url = start_url.replace('ocr', passcodes)
# print end_url