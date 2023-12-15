blocksize = [5,10,20]
processsize = [10,20,30]

def bestfit(blocksize,processsize):
    allocated = [-1]*len(processsize)
    for i in range(len(processsize)):
        allocated[i] = -1
    for i in range(len(processsize)):
        j = 0
        while j<len(blocksize):
            if blocksize[j]>=processsize[i] and allocated[i]==-1:
                allocated[i] = j+1
                blocksize[j]-=processsize[i]
            j+=1
        print(f'{i}\t{processsize[i]}\t{allocated[i]}')
        
# bestfit(blocksize,processsize)

def worstFit(blocksize,processsize):
    allocated = [-1]*len(processsize)
    for i in range(len(processsize)):
        allocated[i] = -1
    for i in range(len(processsize)):
        windex = -1
        for j in range(len(blocksize)):
            if blocksize[j]>=processsize[i]:
                if windex==-1 or blocksize[j]>=blocksize[windex]:
                    windex = j
        if windex!=-1:
            allocated[i] = windex+1
            blocksize[windex]-=processsize[i]
        print(f'{i}\t{processsize[i]}\t{allocated[i]}')
        
worstFit(blocksize,processsize)