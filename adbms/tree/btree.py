from BTrees.IIBTree import IIBTree
import time
t = IIBTree()

insertionTimeStart = time.time()
for i in range(1000):
    t.update({i:2*i})
insertionTimeEnd = time.time()

key = int(input("Enter a key: "))
searchtimestart = time.time()
if t.has_key(key):
    print(t[key])
searchtimeend = time.time()
print(f'The time is : {round((searchtimeend-searchtimestart)*1000,3)}ms')