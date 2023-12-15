incoming = [4, 2, 1, 4, 5]
pages = len(incoming)
frames = 3
fault = 0
temp = [-1] * frames
recently_used = [0] * frames

print("Data\t\tf1\tf2\tf3")
for i in range(pages):
    current_page = str(incoming[i])
    hit = 0

    # Check if the page is present in any frame or not
    for j in range(frames):
        if temp[j] == current_page:
            hit +=1
            recently_used[j] = i

    if hit == 0:
        fault += 1
        if fault <= frames:
            temp[i] = current_page
            recently_used[i] = i
        else:
            # Find the least recently used page
            min_used_index = recently_used.index(min(recently_used))
            temp[min_used_index] = current_page
            recently_used[min_used_index] = i

    print(current_page + "\t\t", end="")
    for j in range(frames):
        print(f'{temp[j]}\t\t', end="")
    print()
