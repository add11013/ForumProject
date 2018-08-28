import re
import numpy as np

file=open("Link.txt","r")
data=file.read()
for s in data.split("),"):
    print(re.findall(r'\d+',s))
file.close()