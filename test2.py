import re
import numpy as np
import timeit

file=open("Link.txt","r")
data=file.read()
for s in data.split("),"):
    result=re.findall(r'\d+',s)
file.close()

t0 = timeit.default_timer()
t1 = timeit.default_timer()
print('without compile', t0-t1)

file=open("Link.txt","r")
data=file.read()
for s in data.split("),"):
    p = re.compile(r'\d+')
    result=p.findall(s)
file.close()

t0 = timeit.default_timer()
t1 = timeit.default_timer()
print('with compile', t0-t1)