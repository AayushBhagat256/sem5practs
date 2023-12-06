# taking the graph input 
graph = {
    'a':['b','c'],
    'b':['d','e'],
    'c':['f'],
    'd':['g'],
    'e':[],
    'f':['h'],
    'g':[],
    'h':[]
}

# desclaring 2 arrays
queue = []
visited = []

closeList = []

def bfs(visited,graph,curNode,goal):
    visited.append(curNode)
    queue.append(curNode)
    print(f'open List = {queue}\nclose list = {closeList}')
    
    while queue:
        m = queue.pop(0)
        closeList.append(m)
        
        if m == goal:
            return
        
        for neighbours in graph[m]:
            if neighbours not in visited:
                #visited and queue mai just append
                visited.append(neighbours)
                queue.append(neighbours)
        print(f'open List = {queue}\nclose list = {closeList}')

print("The BFS algo is : ")
bfs(visited,graph,'a','h')