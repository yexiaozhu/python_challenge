#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

# <!-- you've got his e-mail -->
# import md5
#
# f = open('mybroken.zip', 'rb').read()
# for i in range(len(f)):
#     for j in range(256):
#         newtext = f[:i]+chr(j)+f[i+1:]
#         if md5.md5(newtext).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
#             open('mybroken_new.zip', 'wb').write(newtext)

import md5, array

def sub(data, good_md5):
    allchars = map(chr, range(256))
    for i, oldch in enumerate(data):
        for newch in allchars:
            data[i] = newch
            if md5.new(data).hexdigest() == good_md5:
                return True
        data[i] = oldch
    return False

data = array.array("c", open("mybroken.zip", "rb").read())
sub(data, "bbb8b499a0eef99b52c7f13f4e78c24b")
f = open("repaired.zip", "wb")
f.write(data)
f.close()