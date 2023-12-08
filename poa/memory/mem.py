blockSize = [5, 10, 20]
processSize = [10, 20, 30]
m = len(blockSize)
n = len(processSize)

print("\nProcess No.\tProcess Size\tBlock no.\n")


def bestFit(blockSize, processSize, m, n):
    allocate = [-1] * n
    for i in range(n):
        allocate[i] = -1
    for i in range(n):
        j = 0
        while j < m:
            if blockSize[j] >= processSize[i] and allocate[i] == -1:
                allocate[i] = j+1
                blockSize[j] -= processSize[i]
            j += 1

    for i in range(n):
        print(f'{i + 1}\t{processSize[i]}\t{allocate[i]}')

def worstFit(blockSize, processSize):
    n = len(processSize)
    m = len(blockSize)
    allocate = [-1] * n
    for i in range(n):
        windex = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if windex == -1 or blockSize[windex] < blockSize[j]:
                    windex = j
        if windex != -1:
            allocate[i] = windex
            blockSize[windex] -= processSize[i]
    print("\nProcess No.\tProcess Size\tBlock no.\n")
    for i in range(n):
        print(f'{i + 1}\t{processSize[i]}\t{allocate[i]}')

bestFit(blockSize, processSize, m, n)
# worstFit(blockSize,processSize)