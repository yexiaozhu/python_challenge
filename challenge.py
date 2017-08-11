#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

import xmlrpclib
server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print server.phone('Bert')

start_url = 'http://www.pythonchallenge.com/pc/return/disproportional.html'
# end_url = start_url.replace('bull', passcodes)
# print end_url
