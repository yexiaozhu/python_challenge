#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

# <!--
# TODO: do you owe someone an apology? now it is a good time to
# tell him that you are sorry. Please show good manners although
# it has nothing to do with this level.
# -->
# <!-- 	it can't find it. this is an undocumented module. -->
# <!--
# 'va gur snpr bs jung?'
# -->

import string
dd = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    print i,string.translate("va gur snpr bs jung",string.maketrans(dd,dd[i::]+dd[0:i:]))