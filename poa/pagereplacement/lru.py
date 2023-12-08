incoming = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
pages = len(incoming)

frames = 3

# i, j = 0, 0
fault = 0

temp = [-1] * pages
last_use_time = [-1] * pages

print("Data\t\tframe1\t\tframe2\t\tframe3\t\t")
for i in range(pages):
    temp[i] = -1
    last_use_time[i] = -1

for i in range(pages):
    s = 0
    # no page hit condition
    for j in range(frames):
        if temp[j] == incoming[i]:
            s += 1
            fault -= 1
            last_use_time[j] = i

    # initial adding condition
    fault += 1
    if fault <= frames and s == 0:
        temp[i] = incoming[i]
        last_use_time[i] = i
    # LRU condition
    elif s == 0:
        min_val = 999
        min_index = 0
        for j in range(frames):
            if min_val > last_use_time[j]:
                min_val = last_use_time[j]
                min_index = j
        temp[min_index] = incoming[i]
        last_use_time[min_index] = i

    # print
    print(f"{incoming[i]}\t\t", end="")
    for j in range(frames):
        if temp[j] != -1:
            print(f"{temp[j]}\t\t ", end="")
        else:
            print(" - \t\t ", end="")
    print("\t\t" + str(s) + "\t\t" + str(fault))
    print()
