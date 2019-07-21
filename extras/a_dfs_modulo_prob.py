mod=1000000007
class Graph():
    def __init__(self, nodes,graph=None):
        self.vertices= int(nodes)
        self.graph= [[int(0) for i in range(nodes)] for k in range(nodes)]
        if not graph is None:
            for i in range(nodes):
                for j in range(nodes):
                    self.graph[i][j]=graph[i][j]
class node():
    def __init__(self,name,steps):
        self.name=name
        self.steps=steps

t=int(input())
while(t):
    stack=list()
    [n,m,x]=[ int(y) for y in input().split()]
    
    #output list
    out=[0]*(n+1)
    #print("Out:",out,sep=" ")


    g=Graph(n+1)
    for i in range(m):
        [a,b]=[ int(y) for y in input().split()]
        g.graph[a][b]=1    
    #print(g.graph)
    src=node(x,1)
    stack.append(src)

    while(stack):
        y=stack.pop()
        for i in range(1,n+1):
            if(g.graph[y.name][i]==1):
                k=((y.steps%mod)+1)%mod
                if(k%2==0):
                    out[i]+=1
                stack.append(node(i,k))

    #print
    for i in range(1,len(out)):
        print(out[i],end=" ")            
    print()
    t=t-1