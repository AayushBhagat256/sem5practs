from bplustree import BPlusTree
import time

t = BPlusTree('./tree.db',order=50)

for i in range(1000):
    data = (2*i).to_bytes(10,'big')
    t[i] = data
    
key = int(input("Enter a key: "))
searchtimestart = time.time()
byteData = t.get(key)
search_end_time = time.time()
intdata = int.from_bytes(byteData,'big')
print("Value : ", intdata)
print("Time taken : ", ((search_end_time-searchtimestart)*1000), " ms")