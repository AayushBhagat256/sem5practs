incoming = [4,2,1,4,5]
pages = len(incoming)
frames = 3
fault = 0
temp = [-1]*frames

print("Data\t\tf1\tf2\tf3")
for i in range(pages):
    currentpage = str(incoming[i])
    hit = 0
    #check if page present in any frame or not
    for j in range(frames):
        if temp[j]==currentpage:
            hit+=1
            fault-=1
    
    fault+=1
    if fault<=frames and hit==0:
        temp[i] = currentpage
    elif hit == 0:
        temp[(fault-1)%frames] = currentpage
    print(currentpage+"\t\t",end="")
    for j in range(frames):
        print(f'{temp[j]}\t\t',end="")
    print()
