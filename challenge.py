#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

# <!-- it is more obvious that what you might think -->
# <!-- maybe consider deltas.gz -->
import gzip, difflib
ff = gzip.open('deltas.gz', 'r')
deltas = ff.read()
ff.close()
deltas = deltas.splitlines()
left, right = [], []
for row in deltas:
    left.append(row[:53])
    right.append(row[56:])
diff = list(difflib.ndiff(left, right))

png = ['', '', '']
for row in diff:
    bytes = [chr(int(byte, 16)) for byte in row[2:].split()]
    if row[0] == '-':
        png[0] += ''.join(bytes)
    elif row[0] == '+':
        png[1] += ''.join(bytes)
    elif row[0] == ' ':
        png[2] += ''.join(bytes)

for i in range(3):
    open('out18_%d.png' % i, 'wb').write(png[i])
start_url = 'http://www.pythonchallenge.com/pc/return/balloons.html'
end_url = start_url.replace('return/balloons','hex/bin' )
print end_url
