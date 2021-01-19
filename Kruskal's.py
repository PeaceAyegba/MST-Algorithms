# Python program for Kruskal's algorithm to find
# Minimum Spanning Tree of a given connected,
# undirected and weighted graph

from collections import defaultdict

#Class to represent a graph
class Graph:

    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = [] # default dictionary
                                # to store graph


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

        result =[] #This will store the resultant MST

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
            u,v,w =  self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent ,v)

            # If including this edge does't cause cycle,
                        # include it in result and increment the index
                        # of result for next edge
            if x != y:
                e = e + 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)
            # Else discard the edge

        # print the contents of result[] to display the built MST
        print ("Following are the edges in the constructed MST")
        for u,v,weight  in result:
            #print str(u) + " -- " + str(v) + " == " + str(weight)
            print ("%d -- %d == %f" % (u,v,weight))

# Driver code
g = Graph(37)
g.addEdge(0, 1, 81.5865)
g.addEdge(0, 9, 252.6349)
g.addEdge(0, 36, 338.7641)
g.addEdge(1, 2, 82.5435)
g.addEdge(1, 6, 89.886)
g.addEdge(1, 7, 73.8749)
g.addEdge(2, 3, 67.9046)
g.addEdge(3, 4, 64.1961)
g.addEdge(4, 5, 253.6179)
g.addEdge(5, 6, 113.4832)
g.addEdge(5, 8, 208.4023)
g.addEdge(5, 25, 123.7738)
g.addEdge(7, 8, 169.7241)
g.addEdge(8, 20, 196.889)
g.addEdge(8, 23, 173.2129)
g.addEdge(8, 35, 160.5986)
g.addEdge(9, 35, 118.3903)
g.addEdge(10, 11, 261.9837)
g.addEdge(10,33 ,185.8489 )
g.addEdge(10, 36, 219.6409)
g.addEdge(36, 9, 349.2051)
g.addEdge(11, 13, 209.3103)
g.addEdge(12, 13, 95.6952)
g.addEdge(12, 17, 232.2036)
g.addEdge(13, 14, 285.0276)
g.addEdge(14, 15, 129.7066)
g.addEdge(14, 16, 187.3142)
g.addEdge(15, 21, 298.9509)
g.addEdge(16, 17, 130.5206)
g.addEdge(17, 18, 137.4058)
g.addEdge(18, 19, 165.1677)
g.addEdge(19, 35, 130.2419)
g.addEdge(20, 19, 84.6042)
g.addEdge(20, 23, 181.5531)
g.addEdge(20, 29, 332.0392)
g.addEdge(21, 22, 125.4547)
g.addEdge(22, 20, 337.2769)
g.addEdge(23, 24, 165.3347)
g.addEdge(24, 25, 180.6815)
g.addEdge(26, 23, 66.4409)
g.addEdge(26, 30, 112.0243)
g.addEdge(27, 29, 54.7012)
g.addEdge(27, 31, 174.6213)
g.addEdge(28, 31, 92.6074)
g.addEdge(28, 25, 154.9616)
g.addEdge(29, 30, 177.6956)
g.addEdge(30, 27, 73.2377)
g.addEdge(31, 32, 189.1641)
g.addEdge(32, 25, 166.7202)
g.addEdge(33, 11, 91.1888)
g.addEdge(33, 34,199.7968 )
g.addEdge(34, 12, 202.7576)
g.addEdge(34, 18, 171.3123)
g.addEdge(34, 35, 161.2244)
g.addEdge(34, 9, 138.7795)
g.KruskalMST()

#This code is contributed by Neelam Yadav
