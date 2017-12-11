from collections import defaultdict

class Graph:
	def __init__(self,graph):
		self.graph = graph;
		self.row = len(graph)

	def BFS(self, s, t, parent):
		visited = [False]*(self.row)
		que= []
		que.append(s)
		visited[s] = True

		while que:
			u = que.pop(0)
			for ind, val in enumerate(self.graph[u]):
				if(visited[ind] == False and val>0):
					que.append(ind)
					visited[ind]= True
					parent[ind] = u
		return True if visited[t] else False
	

	def FordFulk(self, source, sink):
		parent = [-1]*(self.row)
		max_flow = 0

		while(self.BFS(source,sink,parent)):
			path_flow = float("Inf")
			s = sink
			while(s != source):
				if(path_flow > self.graph[parent[s][s]]):
					path_flow = self.graph[parent[s][s]]
				#path_flow = min(path_flow, self.graph[parent[s][s]])
				s = parent[s]

			max_flow += path_flow

			v = sink

			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]

		return max_flow




graph = [[0, 16, 13, 0, 0, 0],
		[0, 0, 10, 12, 0, 0],
		[0, 4, 0, 0, 14, 0],
		[0, 0, 9, 0, 0, 20],
		[0, 0, 0, 7, 0, 4],
		[0, 0, 0, 0, 0, 0]]
g = Graph(graph)
source = 0; sink = 5

print("The maximum possible flow is {0}".format(g.FordFulk(source,sink)))
