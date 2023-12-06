from collections import defaultdict

def addEdge(graph,u,v):
    graph[u].append(v)
    
graph = defaultdict(list)
addEdge(graph,0,1)
addEdge(graph,0,2)
addEdge(graph,1,3)
addEdge(graph,1,4)
addEdge(graph,2,5)
addEdge(graph,2,6)

print(graph)

target = 6
maxdepth = 3
src = 0

# 2 functions DLS to search the graph+depths and DDFS to find the target

def dls(target,src,graph,maxdepth):
    if src == target:
        return True
    
    if maxdepth<=0:
        return False
    
    for i in graph[src]:
        if dls(target,i,graph,maxdepth-1):
            return True
    return False

def iddfs(target,src,graph,maxdepth):
    for i in range(maxdepth):
        if dls(target,src,graph,i):
            return True
    return False

if iddfs(target,src,graph,maxdepth):
    print("We can reach to it in max depth")
else:
    print("Nahi hoga ye")