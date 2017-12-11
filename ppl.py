import networkx as nx

G = nx.Graph()

def gencoord(self, thelist):
		


G.add_edge('a' , 'b')
G.add_edge('a' , 'c')
G.add_edge('a' , 'd')
G.add_edge('a' , 'e')

G.add_edge('b' , 'c')
G.add_edge('b' , 'd')
G.add_edge('b' , 'e')

G.add_edge('c' , 'd')
G.add_edge('c', 'e')

G.add_edge('d' , 'e')

an = G.neighbors('a')
bn = G.neighbors('b')
cn = G.neighbors('c')
dn = G.neighbors('d')
en = G.neighbors('e')

#print "connected to a: " , an
#print "connected to b: " ,bn
for x in an:
	print x
#print cn
#print dn
#print en