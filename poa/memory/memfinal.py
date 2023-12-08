blockSize = [5, 10, 20]
processSize = [10, 20, 30]
m = len(blockSize)
n = len(processSize)

print("\nProcess No.\tProcess Size\tBlock no.\n")

def bestfit(bs,ps,m,n):
    allocated = [-1]*n
    for i in range(n):
        allocated[i] = -1
    
    for i in range(n):
        j = 0
        while j<m:
            if bs[j]>=ps[i] and allocated[i]==-1:
                allocated[i] = j+1
                bs[j]-=ps[i]
            j+=1
        print(f'{i+1}\t{ps[i]}\t{allocated[i]}')
        
def worstfit(bs,ps,m,n):
    allocated = [-1]*n
    for i in range(n):
        allocated[i] = -1
    
    for i in range(n):
        windex = -1
        for j in range(m):
           if bs[j]>=ps[i]:
               if windex==-1 or bs[windex]<=bs[j]:
                   windex = j
        if windex!=-1:
            allocated[i] = windex+1
            bs[windex]-=ps[i]
        print(f'{i+1}\t{ps[i]}\t{allocated[i]}')
            
       
            
        
# bestfit(blockSize,processSize,m,n)
worstfit(blockSize,processSize,m,n)