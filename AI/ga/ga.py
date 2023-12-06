from random import randint

# defining a selection function 
# to calculate fitness,expectedcount and actual count
def selection(input):
    #converting bin to dec
    dec = list(map(lambda x: int(x,2),input))
    # print(dec)
    # calulating fitness by squaring
    fit = list(map(lambda x: x*x,dec))
    #calculating the sum of fitness values 
    # values are stored in a array so sum of those elements
    s = sum(fit)
    #probabilities for each gene x/s,3 3=>rounded upto 3 digits
    prob = list(map(lambda x: round(x/s,3),fit))
    avg = s/n
    
    #expected count fit/avg
    exe = list(map(lambda x:round(x/avg,3),fit))
    
    #actual count -> roundoff the expected count
    ac = list(map(lambda x:round(x),exe))
    
    return dec,fit,prob,exe,ac
    
#  the pp function takes a list of genes, their actual counts, and the total number of genes. It selects genes for crossover based on the actual counts and returns the list of selected genes (co). It also handles cases where genes need to be duplicated or inserted at specific indices.

def pp(input,ac,n):
    # co = []: Initialize an empty list co to store selected genes for crossover.
    # temp = []: Initialize an empty list temp to temporarily store genes for duplication.
    # index = []: Initialize an empty list index to store the indices where actual count is 0.
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
        elif ac[i] == 0 and len(temp)!=0:
            co.append(temp[0])
            temp.pop(0)
        elif ac[i] ==0 and len(temp)==0:
            index.append(i)
    if len(index) !=0 and len(temp)!=0:
        for i in index:
            co.insert(i,temp[0])
            temp.pop(0)
    elif len(index)!=0 and len(temp)==0:
        co.insert(i,input[i])
    return co

# a function that return the count of 1s 
def cr(x):
    s = 0
    for i in x:
        if i =='1':
            s = s + 1
    return s
"""
This function performs the crossover operation on a population of genes.
It iterates through the genes in pairs (assuming n is even), where each pair consists of temp1 and temp2.
The crossover point is determined using the cr function, which calculates the count of '1' bits in temp1.
The crossover point is printed for each pair.
The crossover is then performed by swapping the substrings after the crossover point between temp1 and temp2.
The modified genes (temp1 and temp2) are appended to the crossed list.
The function returns the list of genes after crossover.
"""
def crossing(input,n):
    crossed = []
    for i in range(0,n,2):
        temp1 = input[i]
        j = i+1 
        temp2 = input[j]
        crosspoint = cr(temp1)
        print(f'The crosspoint for pair {str(i)} is {str(crosspoint)}')
        temp3 = temp1[crosspoint:]     
        temp4 = temp2[crosspoint:]
        temp1 = temp1[0:crosspoint]+temp4
        temp2 = temp2[0:crosspoint]+temp3
        crossed.append(temp1)
        crossed.append(temp2)
    return crossed

# mutation is 1->0 and 0->1 for this we will use random
def mutation(input,n):
    mut = []
    for i in input:
        j = randint(0,n-1) #generated random integers between 0 and n-1
        print("For pair " + str(i) + ", the bit that will be changed is " + str(j))
        if i[j] == '1':
            i = i[0:j]+'0'+i[j+1:]
            mut.append(i)
        elif i[j] == '0':
            i = i[0 : j] + '1' +i[j + 1 : ]
            mut.append(i) 
    return mut       

n = int(input("Enter the number of samples")) 
sample = [] 
for i in range(n):
    sample.append(input("Enter gene : "))
m = int(input("Enter the number of generation you want to count"))
crossed = sample.copy()
for i in range(m):
    dec, fit, prob, exe, ac = selection(crossed)
    s = sum(ac)
    if s < n:
        maxi = max(ac)
        k = ac.index(maxi - 1)
        ac[k] += 1
    if s > n:
        maxi = max(ac)
        k = ac.index(maxi)
        ac[k] -= 1
    print("\n----------------------------------------------- GENERATION ", i, "-----------------------------------------------")
    print("Initial Population\tX Value\t\tFitness Value\tProbability\tExpected Count\t\tActual Count")
    for j in range(n):
        print(crossed[j], "\t\t", dec[j], "\t\t", fit[j], "\t", prob[j], "\t\t", exe[j], "\t\t\t", ac[j])
    co = pp(crossed, ac, n)
    print("\nSelected Genes for Crossover - \n", co)
    crossed = crossing(co, n)
    print("\nCrossover - \n", crossed)
    crossed = mutation(crossed, n)
    print("\nMutated - \n", crossed)
print("\nGENERATION ", (m + 1), " - ", crossed)
     