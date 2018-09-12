import re
import networkx as nx
G = nx.Graph()

file=open("Link.txt","r")
data=file.read()
for s in data.split("),"):
    G.add_nodes_from(re.findall(r'\d+',s))
    G.add_edge(re.findall(r'\d+',s)[0],re.findall(r'\d+',s)[1])
    
file.close()
print(len(G.adj['51764'].keys()))
print("nodes:%d  ,   edges:%d "%(G.number_of_nodes(),G.number_of_edges()))