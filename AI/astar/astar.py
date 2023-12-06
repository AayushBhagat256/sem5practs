# code for A star algorithm
#defining our graph
Graph_nodes = {
    'S':[('A',6),('B',5),('C',10)],
    'A':[('E',6)],
    'B':[('E',6),('D',7)],
    'C':[('D',6)],
    'D':[('F',6)],
    'E':[('F',4)],
    'F':[('G',3)],
}

# print(Graph_nodes['C'])

#define the heuristic function
def heurestic(n):
    h_dist = {
        'S': 17,
        'A': 10,
        'B': 13,
        'C': 4,
        'D': 2,
        'E': 4,
        'F': 1,
        'G': 0
    }
    return h_dist[n]

def getneighbour(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        print('No neighbour found')
        return None
    
def astaralgo(start,goal):
    openset = set(start)
    closeset = set()
    print(f'the open and is {openset}\nclose set is {closeset}')
    g = {} #to track cost
    parent = {}
    g[start] = 0
    parent[start] = start
    print(f'the parent is {parent}')
    
    
    while len(openset)>0:
        n = None
        print(f'the open and is {openset}\nclose set is {closeset}')
        for v in openset:
            if n is None or g[v]+heurestic(v) < g[n] + heurestic(n):
                n = v
        print(f'now n is {n}')
        
        if n == goal:
            print("Goal part here")
            openset.remove(n)
            closeset.add(n)
            print(f'the open and is {openset}\nclose set is {closeset}')
            path = []
            while parent[n]!=n:
                path.append(n)
                n = parent[n]
                
            print(f'path is {path}')
            path.append(start)
            path.reverse()
            print(f'path is {path}')
            return path
         
        for (m,weight) in getneighbour(n):
            # 3 conditions 
            # if not in open and close them add in open , parent and cost update
            if m not in openset and m not in closeset:
                openset.add(m)
                parent[m] = n
                g[m] = g[n] + weight
                
            # update the weight and min proceeding with min only
            else:
                if g[m]>g[n]+weight:
                    g[m] = g[n]+weight
                    parent[m] = n
                    #if m in closed set,remove and add to open
                    if m in closeset:
                        openset.add(m)
                        closeset.remove(m)
        openset.remove(n)
        closeset.add(n)
        print(f'the open and is {openset}\nclose set is {closeset}')
        
        

astaralgo('S','G')