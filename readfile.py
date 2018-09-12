# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 16:27:14 2018
@author: chenyy
"""
import math
import Linkage
from scipy import spatial
import re
import networkx as nx
G = nx.Graph()

"""c_num = input("input a  number:")"""
uw = open("Date.txt", "r")
"""def make_graph():
    with open ('Link.txt', 'r') as f:
        for line in f:
            
            G.add_node(H)
            s.append(line.strip())"""
            
            
#network building
file=open("Link.txt","r")
data=file.read()
for s in data.split("),"):
    G.add_nodes_from(re.findall(r'(\d+)',s))
    if re.findall(r'\d+',s)[0] != re.findall(r'\d+',s)[1]:
        G.add_edge(re.findall(r'\d+',s)[0],re.findall(r'\d+',s)[1])
    else:
        pass
    
file.close()

#caculate simularity 
def sim_b(n1, n2):
     simb = 1-spatial.distance.cosine(d[n1], d[n2])
     return simb

def sim_a(n1, n2):
    adj_n1 = list(G.adj[n1])
    adj_n2 = list(G.adj[n2])
    
    ins_num = len(list(set(adj_n1) & set(adj_n2)))
    
    sima = (ins_num/math.sqrt(len(adj_n1) * len(adj_n2)))
    
    return sima

def edge_weight(G, a):
    for e in G.edges:
        e_weight = ((1-a)*sim_b(e[0], e[1]) + (a*sim_a(e[0], e[1])))
        G.add_edge(e[0], e[1], weight =e_weight)

edge_weight(G,0.5)

print("nodes:%d  ,   edges:%d "%(G.number_of_nodes(),G.number_of_edges()))
print(1-spatial.distance.cosine(d['3025887'], d['3025887']))
M = 1-spatial.distance.cosine(d['3025887'], d['3025887'])
print(len(G.adj['51764'].keys()))
