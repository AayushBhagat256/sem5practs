incoming = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
pages = len(incoming)
fault = 0
frames = 3

temp = ['-1']*pages
print(temp)

print('input\t\tframe1\t\tframe2\t\tframe3\t\thits\t\tfault')
for i in range(pages):
    hit = 0
    curpage = str(incoming[i])
    #page is already present
    for j in range(frames):
        if temp[j] == curpage:
            hit +=1
            fault-=1
    
    # fifo iniital
    fault+=1 
    if fault<=frames and hit == 0:
        temp[i] = curpage
    if hit == 0: #main fifo condition
        temp[(fault-1)%frames] = curpage
    
    print(curpage + "\t\t", end="")
    for j in range(frames):
        if temp[j] == '-1':
            temp[j] = '-'
        print(temp[j] + "\t\t", end="")
    print("\t\t" + str(hit) + "\t\t" + str(fault))