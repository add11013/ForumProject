import re
import numpy as np

file=open("Link.txt","r")
data=file.read()
b = np.array([[], []])
list1=[]
for s in data.split("),"):
    
    p = re.compile(r'\d+')
    b=p.findall(s) 
file.close()

