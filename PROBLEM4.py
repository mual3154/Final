#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 15:29:04 2017

@author: rhoenigman
"""
from collections import defaultdict
import networkx as nx
#create a directed graph
G = nx.DiGraph()

def bfs(self, current, dest, pathamount, path): #create the recursive function breadthfirstsearch
	total = 0 #the total routes that reach Fly
	edges = [ ] #edges are the other nodes pointed to by the current node
	edges = self.successors(current) #retrieves a list of edges connected from networkx
	que = [ ] #develop list of edges
	for x in edges: #for loop to move all the edges from edges to que for a better data structure
		que.append(x) #adds the items into the list
	q = 0 # starts from the start of the que
	path.append(current) #adds the current path to the list recording the current path
	for q in range(len(que)): #traverses the que list
		if que[q] == dest: #checks if the current node is 'Fly'
			total = total + 1 # adds 1 to the total paths
			path.append('Fly') # appends fly at the end because the code never visits Fly
			print path #and therefore never adds it to the list
			path.pop()	# I then have to pop it out of the list
		else :
			total = total + bfs(self, que[q], dest, total, path) #recursively call my code
	path.pop() #pops the last member of the path as it leaves its recursive call
	return total #returns amount of paths
	

#adding an edge also adds the node
G.add_edge('Spider', 'A', weight=1.0)
G.add_edge('Spider', 'H', weight=1.0)
G.add_edge('Spider', 'J', weight=1.0)

G.add_edge('H', 'G', weight=1.0)
G.add_edge('H', 'K', weight=1.0)

G.add_edge('G', 'L', weight=1.0)
G.add_edge('G', 'F', weight=1.0)

G.add_edge('F', 'E', weight=1.0)

G.add_edge('E', 'Fly', weight=1.0)

G.add_edge('J', 'S', weight=1.0)
G.add_edge('J', 'K', weight=1.0)

G.add_edge('K', 'L', weight=1.0)
G.add_edge('L', 'M', weight=1.0)
G.add_edge('M', 'N', weight=1.0)
G.add_edge('M', 'F', weight=1.0)

G.add_edge('N', 'O', weight=1.0)
G.add_edge('N', 'E', weight=1.0)

G.add_edge('O', 'Fly', weight=1.0)

G.add_edge('A', 'S', weight=1.0)
G.add_edge('A', 'B', weight=1.0)

G.add_edge('B', 'R', weight=1.0)
G.add_edge('B', 'C', weight=1.0)

G.add_edge('S', 'R', weight=1.0)
G.add_edge('R', 'Q', weight=1.0)

G.add_edge('Q', 'C', weight=1.0)
G.add_edge('Q', 'P', weight=1.0)

G.add_edge('C', 'D', weight=1.0)
G.add_edge('D', 'Fly', weight=1.0)
G.add_edge('P', 'D', weight=1.0)
G.add_edge('P', 'O', weight=1.0)
G.add_edge('O', 'Fly', weight=1.0)

G.add_edge('T', 'Q', weight=1.0)
G.add_edge('T', 'P', weight=1.0)
G.add_edge('T', 'O', weight=1.0)
G.add_edge('T', 'N', weight=1.0)
G.add_edge('T', 'M', weight=1.0)

G.add_edge('R', 'T', weight=1.0)
G.add_edge('S', 'T', weight=1.0)
G.add_edge('J', 'T', weight=1.0)
G.add_edge('K', 'T', weight=1.0)
G.add_edge('L', 'T', weight=1.0)

#each edge has a weight of 1. The shortest path is the fewest edges.
#Use this to verify that your graph built correctly.
print("!!!!!INITIAL TEST FOR THE GRAPH!!!!!")
t = nx.shortest_path(G, 'Spider', 'Fly', weight='weight')
print t

print " "
print " "
print "The following is a list of all the possible paths between the fly and the spider: "
totalpaths = 0
path = [ ]
m = bfs(G, 'Spider', 'Fly', totalpaths, path)
print " "
print"The total amount of paths are: ", m 
