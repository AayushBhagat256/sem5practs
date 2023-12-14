list1 = []

while True:
    print('Enter the values in [lvl,heu]')
    level = input("Enter the level: ")
    
    if level == '0':
        break
    
    heu = int(input("Enter the heuristic: "))
    list1.append([level, heu])

print(list1)

list2 = []

for i in range(1, len(list1) + 1):
    level = [x[1] for x in list1 if x[0] == str(i)]
    
    if len(level) == 0:
        continue
    
    list2.append(level)

path = []

minimum = float('inf')  # Initialize minimum to positive infinity

for i in range(len(list2)):
    if min(list2[i]) < minimum:
        minimum = min(list2[i])
        path = min(list2[i])

print(path)
