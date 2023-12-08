# incoming = [4, 2, 1, 4, 5]
incoming = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
pages = len(incoming)

frame = 3
fault = 0
temp = ['-1'] * frame

print("Data\t\tframe1\t\tframe2\t\tframe3\t\tHit\t\tFault")
for i in range(pages):
    current_page = str(incoming[i])
    hit_count = 0
    # check if the page is already present or not
    for j in range(frame):
        if temp[j] == current_page:
            hit_count += 1
            fault -= 1

    # initial condition
    fault += 1
    if fault <= frame and hit_count == 0:
        temp[i] = current_page
    elif hit_count == 0:  # fifo condition
        temp[(fault - 1) % frame] = current_page

    print(current_page + "\t\t", end="")
    for j in range(frame):
        if temp[j] == '-1':
            temp[j] = '-'
        print(temp[j] + "\t\t", end="")
    print("\t\t" + str(hit_count) + "\t\t" + str(fault))
