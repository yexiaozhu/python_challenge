#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

start_url = "http://www.pythonchallenge.com/pc/def/peak.html"

import pickle

with open('banner.p', 'rb') as fp:
    t = pickle.load(fp)
    for item in t:
        print(''.join([x[0] * x[1] for x in item]))