import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
from time import clock, sleep, time

sns.set()

from collections import defaultdict

#Class to represent a graph
class Graph:

    def __init__(self,vertices):
        self.start = time()
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary


    # function to add an edge to graph
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    # A utility function to find set of an element i
    # (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # If ranks are same, then make one as root
        # and increment its rank by one
        else :
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's
        # algorithm
    def KruskalMST(self):

        self.result =[] #This will store the resultant MST

        i = 0 # An index variable, used for sorted edges
        e = 0 # An index variable, used for result[]

            # Step 1:  Sort all the edges in non-decreasing
                # order of their
                # weight.  If we are not allowed to change the
                # given graph, we can create a copy of graph
        self.graph =  sorted(self.graph,key=lambda item: item[2])

        parent = [] ; rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V -1 :

            # Step 2: Pick the smallest edge and increment
                    # the index for next iteration
            # print(self.graph[i][0], self.graph[i], self.graph[i])
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)

            # If including this edge does't cause cycle,
                        # include it in result and increment the index
                        # of result for next edge
            if x != y:
                e = e + 1
                self.result.append([u,v,w])
                self.union(parent, rank, x, y)
            # Else discard the edge
        G = nx.Graph()
        for u,v,weight  in self.graph:
            G.add_edge(u, v, length= float(weight))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels = True)  # with_labels=true is to show the node number in the output graph
        edge_labels = nx.get_edge_attributes(G, 'length')
        nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 5) #    prints weight on all the edges

        
        # print(edge_labels)
        total_sum = 0
        for X in self.result:
            total_sum += X[2]
            if (X[0], X[1]) in G.edges():
                nx.draw_networkx_edges(G, pos, edgelist = [(X[0], X[1])], width = 2, alpha = 0.6, edge_color = 'r')

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

    g.KruskalMST()
