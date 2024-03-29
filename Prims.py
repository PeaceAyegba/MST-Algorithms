# A Python program for Prim's Minimum Spanning Tree (MST) algorithm.
# The program is for adjacency matrix representation of the graph

import sys # Library for INT_MAX

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]

    # A utility function to print the constructed MST stored in parent[]
    def printMST(self, parent):
        print ("Edge \tWeight")
        for i in range(1,self.V):
            print (parent[i],"-",i,"\t",self.graph[i][ parent[i] ] )

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initilaize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # Function to construct and print MST for a graph
    # represented using adjacency matrix representation
    def primMST(self):

        #Key values used to pick minimum weight edge in cut
        key = [sys.maxsize] * self.V
        parent = [None] * self.V # Array to store constructed MST
        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1 # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                        key[v] = self.graph[u][v]
                        parent[v] = u

        self.printMST(parent)

g = Graph(37)
g.graph = [ [0,  81.5865,    0,     0,   0, 0, 0,  0,   0, 252.6349,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  338.7641],
          [81.5865, 0  ,82.5435,0, 0,0,89.886,73.8749, 0, 0,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
          [0, 82.5435, 0,67.9046, 0, 0, 0,  0,   0, 0,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 67.9046, 0,64.1961, 0, 0,  0,   0, 0,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 64.1961, 0,253.6179, 0,  0,   0,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
          [0, 0, 0, 0, 253.6179, 0,113.4832,  0,208.4023,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0,123.7738, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 89.886, 0, 0, 0,113.4832, 0,  0,   0, 0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
          [0,73.8749, 0, 0, 0, 0, 0,  0,169.7241,0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0],
          [0, 0, 0, 0, 0, 208.4023, 0,169.7241,   0, 0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0,196.889, 0, 0,173.2129, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 160.5986, 0],
          [252.6349, 0, 0, 0, 0, 0, 0,  0,   0, 0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 118.3903, 349.2051],
          [0, 0, 0, 0, 0, 0, 0,  0, 0, 0 ,0,261.9837, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,185.8489, 0, 0, 219.6409],
          [0, 0, 0, 0, 0, 0, 0,  0, 0, 0 ,261.9837, 0,0, 209.3103, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  91.1888, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,   0, 0 ,0, 0, 0, 95.6952, 0, 0, 0, 232.2036 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 202.7576, 0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,   0, 0 ,0, 209.3103, 95.6952, 0,285.0276, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,   0, 0 ,0, 0, 0,285.0276, 0, 129.7066,187.3142,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,   0, 0 ,0, 0, 0,0 ,  129.7066,0,0,0 ,0, 0, 0,298.9509, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,   0, 0 ,0, 0, 0,0 , 187.3142,0,0,130.5206,0, 0, 0,0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,   0, 0 ,0, 0,232.2036,0 , 0,0,130.5206,0 , 137.4058, 0, 0,0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,   0, 0 ,0, 0,0 ,0 , 0,0,0,137.4058,0, 165.1677, 0,0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 171.3123 , 0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,   0, 0 ,0, 0,0 ,0 , 0,0,0,0,165.1677, 0,84.6042,0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  130.2419, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,196.889, 0 ,0, 0,0 ,0 , 0,0,0,0,0 ,84.6042,0,0 ,  337.2769, 181.5531, 0, 0, 0, 0, 0,332.0392, 0, 0, 0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,0, 0 ,0, 0,0 ,0 , 0, 298.9509,0,0,0 ,0,0,0 ,125.4547, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,0, 0 ,0, 0,0 ,0 , 0,0,0,0,0 ,0,337.2769,125.4547 ,0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,173.2129, 0 ,0, 0,0 ,0 , 0, 0,0,0,0 ,181.5531,0,0 ,0, 165.3347, 0, 66.4409, 0, 0, 0,0, 0, 0, 0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0, 0, 0,  0,0 , 0 ,0, 0,0 ,0 , 0, 0,0,0,0 ,0,0,0 ,0, 165.3347, 0, 180.6815, 0, 0, 0,0, 0, 0, 0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0,123.7738, 0,  0,0 , 0 ,0, 0,0 ,0 , 0, 0,0,0,0 ,0,0,0 ,0, 0, 180.6815, 0, 0, 0, 0,0, 0, 0, 166.7202, 0, 0,  0, 0],
          [0, 0, 0, 0, 0,0, 0,  0,0 , 0 ,0, 0,0 ,0 , 0, 0,0,0,0 ,0,0,0 ,0, 66.4409, 0, 0, 0, 0, 0,0,  112.0243, 0, 0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0,0, 0,  0,0 , 0 ,0, 0,0 ,0 , 0, 0,0,0,0 ,0,0,0 ,0, 0, 0, 0, 0, 0, 0,54.7012, 73.2377, 174.6213, 0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0,0, 0,  0,0 , 0 ,0, 0,0 ,0 , 0, 0,0,0,0 ,0,0,0 ,0, 0, 0, 154.9616, 0, 0, 0,0, 0, 92.6074, 0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0,0, 0,  0,0 , 0 ,0, 0,0 ,0 , 0, 0,0,0,0 ,0, 332.0392,0 ,0, 0, 0, 0, 0, 54.7012, 0,0, 177.6956, 0, 0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0,0, 0,  0,0 , 0 ,0, 0,0 ,0 , 0, 0,0,0,0 ,0, 0,0 ,0, 0, 0, 0, 112.0243, 73.2377, 0,177.6956, 0, 0, 0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0,0, 0,  0,0 , 0 ,0, 0,0 ,0 , 0, 0,0,0,0 ,0, 0,0 ,0, 0, 0, 0, 0, 174.6213,92.6074,0, 0, 0,189.1641, 0, 0,  0, 0],
          [0, 0, 0, 0, 0,0, 0,  0,0 , 0 ,0, 0,0 ,0 , 0, 0,0,0,0 ,0, 0,0 ,0, 0, 0,166.7202, 0, 0,0,0, 0, 189.1641,0, 0, 0,  0, 0],
          [0, 0, 0, 0, 0,0, 0,  0,0 , 0 ,185.8489,91.1888,0 ,0 , 0, 0,0,0,0 ,0, 0,0 ,0, 0, 0,0, 0, 0,0,0, 0, 0,0, 0,199.7968,  0, 0],
          [0, 0, 0, 0, 0,0, 0,  0,0 , 138.7795,0,0,202.7576 ,0 , 0, 0,0,0,171.3123 ,0, 0,0 ,0, 0, 0,0, 0, 0,0,0, 0, 0,0,199.7968 ,0, 161.2244, 0],
          [0, 0, 0, 0, 0,0, 0,  0,160.5986 , 118.3903,0,0,0 ,0 , 0, 0,0,0,0,130.2419, 0,0 ,0, 0, 0,0, 0, 0,0,0, 0, 0,0,0 ,161.2244, 0, 0],
          [338.7641, 0, 0, 0, 0,0, 0,  0,0, 349.2051,219.6409,0,0 ,0 , 0, 0,0,0,0,0, 0,0 ,0, 0, 0,0, 0, 0,0,0, 0, 0,0,0 ,0, 0, 0]]

g.primMST()

