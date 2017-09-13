#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu
import Image

import cStringIO
import urllib

start_url = "http://repeat:switch@www.pythonchallenge.com/pc/ring/grandpa.html"

# <!-- short break, this ***REALLY*** has nothing to do with Python -->

url = 'http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/mandelbrot.gif'
ufos = Image.open(cStringIO.StringIO(urllib.urlopen(url).read()))
def mandelbrot(left=0.34, bottom=0.57, width=0.036, height=0.027, max=128, size=(640, 480)):
     xstep = width / size[0]
     ystep = height / size[1]
     for y in xrange(size[1] - 1, -1, -1):
         for x in xrange(size[0]):
             c = complex(left + x * xstep, bottom + y * ystep)
             z = 0+0j
             for i in xrange(max):
                 z = z * z + c
                 if abs(z) > 2:
                     break
             yield i
mandel = ufos.copy() # We can reuse the type, size and palette
mandel.putdata(list(mandelbrot()))
mandel.show()

differences = [(a - b) for a, b in zip(ufos.getdata(), mandel.getdata()) if a != b]
print len(differences)
print set(differences)
factor = lambda n: filter(lambda f: not n%f, xrange(1,n+1))
print factor(len(differences))
plot = Image.new('L', (23, 73))
plot.putdata([(i < 16) and 255 or 0 for i in differences])
# plot.resize((230, 730)).show()
plot.save('out31.png')