import networkx as nx
import matplotlib.pyplot as plt
import sys
from time import clock, sleep, time

class Graph:
	def __init__(self,vertices):
		self.start = time()
		self.V= vertices #No. of vertices
		self.graph = nx.Graph()
		# self.graph = [] # default dictionary

	# function to add an edge to graph
	def addEdge(self,u,v,w):
		self.graph.add_edge(int(u), int(v), length= float(w))

	#draws the graph and displays the weights on the edges
	def drawGraph(self):
		pos = nx.spring_layout(self.graph)
		nx.draw(self.graph, pos, with_labels = True)  #with_labels=true is to show the node number in the output graph
		edge_labels = nx.get_edge_attributes(self.graph,'length')
		nx.draw_networkx_edge_labels(self.graph, pos, edge_labels = edge_labels, font_size = 5) #prints weight on all the edges
		return pos

	
	def minDistance(self, dist, mstSet):
		min = sys.maxsize
		for v in range(self.V):
			if dist[v] < min and mstSet[v] == False:
				min = dist[v]
				min_index = v
		return min_index


	#function that performs prims algorithm on the graph G
	def PrimMST(self):
		pos = self.drawGraph()
		dist = [] # dist[i] will hold the minimum weight edge value of node i to be included in MST
		parent = [None]* self.V # parent[i] will hold the vertex connected to i, in the MST edge
		mstSet = [] # mstSet[i] will hold true if vertex i is included in the MST
		#initially, for every node, dist[] is set to maximum value and mstSet[] is set to False
		for i in range(self.V):
			dist.append(sys.maxsize)
			mstSet.append(False)
		dist[0] = 0
		parent[0]= -1 #starting vertex is itself the root, and hence has no parent
		for count in range(self.V):
			u = self.minDistance(dist, mstSet) #pick the minimum distance vertex from the set of vertices
			mstSet[u] = True
			#update the vertices adjacent to the picked vertex
			for v in range(self.V):
				if (u, v) in self.graph.edges():
					# if mstSet[v] == False and self.graph[u][v]['length'] < dist[v]:
					if self.graph[u][v]['length'] > 0 and mstSet[v] == False and dist[v] > self.graph[u][v]['length']:
						dist[v] = self.graph[u][v]['length']
						parent[v] = u
		#  edge_labels = nx.get_edge_attributes(self.graph, 'length')
		#  print(edge_labels)
		total_sum = 0
		for X in range(self.V):
			if parent[X] != -1: #ignore the parent of the starting node
				if (parent[X], X) in self.graph.edges():
					# print(parent[X], X, self.graph[parent[X]][X]['length'])
					total_sum += self.graph[parent[X]][X]['length']
					nx.draw_networkx_edges(self.graph, pos, edgelist = [(parent[X], X)], width = 2.5, alpha = 0.6, edge_color = 'r')
		
		self.end = time()
		print(self.end - self.start)
		print("Total Cost ", total_sum)
		plt.show()


if __name__ == "__main__":
    fo = open("dataset 81.txt", 'r')

    file = fo.read().splitlines()

    fo.close()

    no = int(file[0])
    g = Graph(no)

    for x in file[1:]:
        new = x.split()
        #g.addEdge(int(new[1]), int(new[2]), round(float(new[3]), 3))
        g.addEdge(int(new[0]), int(new[1]), round(float(new[2]), 3))

    g.PrimMST()
