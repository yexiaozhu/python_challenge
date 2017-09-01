#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

# <!-- did you say gif? -->
# <!-- oh, and this is NOT a repeat of 14 -->
import Image, string, bz2, keyword
f = Image.open('zigzag.gif')
fd = f.tobytes()
fp = f.palette.getdata()[1][::3]
trans = string.maketrans(''.join([chr(i) for i in range(256)]), fp)
ftran = fd.translate(trans)
diff = ['', '']
img = Image.new('1', f.size, 0)
for i in range(1, len(fd)):
    if fd[i] != ftran[i-1]:
        diff[0] += fd[i]
        diff[1] += ftran[i-1]
        img.putpixel(((i-1)%f.size[0], (i-1)/f.size[0]), 1)
img.save('out27.png')
text = bz2.decompress(diff[0])
for i in text.split():
    if not keyword.iskeyword(i):
        print i