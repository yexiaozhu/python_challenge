#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

# second youngest
# 1**6.1.27. it might be a birthday, beacuse we should buy flower for that day.
from calendar import isleap
from datetime import date
TUESDAY = 1
for year in range(1006, 2000, 10):
    t = date(year, 1, 27)
    if isleap(year) and t.weekday() == TUESDAY:
        print t.isoformat()

start_url = 'http://www.pythonchallenge.com/pc/return/cat.html'
# end_url = start_url.replace('bull', passcodes)
# print end_url
