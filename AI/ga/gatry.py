from random import randint

def selection(inp):
    dec = list(map(lambda x : int(x,2),inp))
    fit = list(map(lambda x: x*x,dec))
    s = sum(fit)
    avg = s/n 
    exe = list(map(lambda x: round(x/avg,3),fit))
    ac = list(map(lambda x: round(x),exe))
    return dec,fit,exe,ac

def pp(input,n,ac):
    co = []
    temp = []
    index = []
    for i in range(n):
        if ac[i] == 1:
            co.append(input[i])
        elif ac[i] >=2:
            for j in range(ac[i]-1):
                temp.append(input[i])
            co.append(input[i])
        elif ac[i]==0 and len(temp)!=0:
            co.append(temp[0])
            temp.pop(0)
        elif ac[i]==0 and len(temp)==0:
            index.append(i)
    if len(index)!=0 and len(temp)!=0:
        for i in index:
            co.insert(i,temp[0])
            temp.pop(0)
    elif len(index)!=0 and len(temp)==0:
        co.insert(i,input[i])
    return co

def crs(x):
    s = 0
    for i in x:
        if i == '1':
            s = s + 1
    return s

def cross(inp,n):
    cross = []
    for i in range(0,n,2):
        temp1 = inp[i]
        j = i + 1
        temp2 = inp[j]
        crossover = crs(temp1)
        print("The crosspoint for string"+str(i)+" is "+str(crossover))
        temp3 = temp1[crossover:]
        temp4 = temp2[crossover:]
        temp1 = temp1[0:crossover]+temp4
        temp2 = temp2[0:crossover]+temp3
    cross.append(temp1)
    cross.append(temp2)
    return cross

def mutation(inp,n):
    mut = []
    for i in inp:
        j = randint(0,n-1)
        print("For pair " + str(i) + ", the bit that will be changed is " + str(j))
        if i[j] =='1':
            i = i[0:j]+'0'+i[j+1:]
            mut.append(i)
        if i[j] =='0':
            i = i[0:j]+'1'+i[j+1:]
            mut.append(i)
    return mut

n = int(input("Enter the number of samples : "))
samples = []
for i in range(n):
    samples.append(input("Enter the gene: "))
m = int(input("Enter the number of generations : "))

for i in range(m):
    dec, fit, exe, ac = selection(samples)
    s = sum(ac)
    if s>n:
        maxi = max(ac)
        k = ac.index(maxi)
        ac[k] -=1
    if s<n:
        maxi = max(ac)
        k = ac.index(maxi)
        ac[k] +=1
    print("\n--------------------------------GENERATION TABLE "+str(i) +" -----------------------\n")
    print(f'Samples\tdec\tfit\texe\tac')
    for j in range(n):
        print(f'{samples[j]}\t\t{dec[j]}\t\t{fit[j]}\t\t{exe[j]}\t\t{ac[j]}\t\t')
    co = pp(samples,n,ac)
    print(f'The genes for crossover are : {co}')
    crossover = cross(samples,n)
    print(f'The genes after crossover are : {crossover}')
    mut = mutation(samples,n)
    print(f'The genes after mutation are : {mut}')