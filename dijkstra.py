#Each graph object has
#   -vertices
#   -graph

import sys

class Graph():
    def __init__(self, nodes,graph=None):
        self.vertices= int(nodes)
        self.graph= [[int(0) for i in range(nodes)] for k in range(nodes)]
        if not graph is None:
            for i in range(nodes):
                for j in range(nodes):
                    self.graph[i][j]=graph[i][j]

    def minDis(self,dist,lookup):
        min_value=sys.maxsize
        min_index=-1
        for i in range(self.vertices):
            if dist[i]<min_value and lookup[i]==False:
                min_value=dist[i]
                min_index=i
        return min_index                        

    def dijkstra(self,source):

        #initializing distance list
        dist=[sys.maxsize]*self.vertices
        dist[source]=0

        #Status of all nodes considered
        lookup=[False]*self.vertices
        
        for i in range(self.vertices):
            u=self.minDis(dist,lookup)
            lookup[u]=True
            for v in range(self.vertices):
                if self.graph[u][v]>0 and lookup[v]==False:
                     dist[v]=min(dist[v],dist[u]+self.graph[u][v])

        return dist        

a  = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]; 
g  = Graph(9,a)
print(g.dijkstra(0))

