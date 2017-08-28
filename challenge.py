#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

import requests
import re

url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
start = 30203
end = 2123456788
class page(object):
    def __init__(self):
        self.url = url
        self.start = start
        self.end = end
    def next_page(self):
        for i in range(10):
            print i
            # 添加的头部请求
            content_range = {'Range': 'bytes={0}-{1}'.format(self.start, '')}
            print content_range
            # 登陆信息
            auth = ('butter', 'fly')
            # 发送请求
            req = requests.get(url, auth=auth, headers=content_range)
            head = req.headers
            con_range = head.get('Content-Range')
            if con_range:
                '''  
                打印网站连接状态，Content-Range，文件大小，文件前100个字节内容  
                '''
                print 'Status Code:', req.status_code
                print 'Content-Range:', con_range
                print type(con_range)
                con_range_number = re.findall(".*-(.*)/.*", con_range)
                self.start = int(con_range_number[0])+1
                print 'next_number:', start
                print 'content-size: ', len(req.content)
                print 'content[:100]: ', str(req.content[:100])
            else:
                break
        return self.start

    def next_page2(self):
        for i in range(10):
            print i
            # 添加的头部请求
            content_range = {'Range': 'bytes={0}-{1}'.format(self.end, '')}
            print content_range
            # 登陆信息
            auth = ('butter', 'fly')
            # 发送请求
            req = requests.get(url, auth=auth, headers=content_range)
            head = req.headers
            con_range = head.get('Content-Range')
            if con_range:
                '''  
                打印网站连接状态，Content-Range，文件大小，文件前100个字节内容  
                '''
                print 'Status Code:', req.status_code
                print 'Content-Range:', con_range
                print type(con_range)
                print 'content-size: ', len(req.content)
                print 'content[:100]: ', str(req.content[:100])
                con_range_number = re.findall(".* (.*)-.*", con_range)
                number = re.compile(r'\d+').findall(str(req.content[:100]))
                if number:
                    self.end = int(number[0])
                else:
                    self.end = int(con_range_number[0]) - 1
                if con_range:
                    index = re.search(r'-(\d+)/', con_range).group(1)
                    text = req.content
                    with open('first.txt', 'ab') as f:
                        f.write(con_range.encode('utf-8') + b'\n')
                        f.write(text)
                        f.write(b'************************************* \n')
                print self.end
            else:
                break
        return self.end


if __name__ == '__main__':
    page().next_page()
    page().next_page2()