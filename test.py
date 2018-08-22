
import re


s="('1509182', '1175625'),"
p = re.compile(r'\d+')

print(p.findall(s))

