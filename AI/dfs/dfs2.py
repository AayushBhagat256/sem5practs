from collections import defaultdict

def addEdge(graph,u,v):
    graph[u].append(v)
    
    
graph = defaultdict(list)
addEdge(graph, 'a', 'b')
addEdge(graph, 'a', 'c')
addEdge(graph, 'b', 'd')
addEdge(graph, 'b', 'e')
addEdge(graph, 'c', 'f')
addEdge(graph, 'd', 'g')
addEdge(graph, 'f', 'h')

print(graph)

# declaring arrays 
visited = []
closeList = []

def dfsUtil(visited,closeList,graph,curNode,goal):
    visited.append(curNode)
    print(f'open list = {visited}\nclose list = {closeList}')
    curNode = visited.pop()
    closeList.append(curNode)
    
    if curNode == goal:
        return
    
    for neighbour in graph[curNode]:
        if neighbour not in visited:
            dfsUtil(visited,closeList,graph,neighbour,goal)

print("Algorithm for DFS is:") 
dfsUtil(visited,closeList,graph,'a','h')  