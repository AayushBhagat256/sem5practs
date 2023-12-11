from bplustree import BPlusTree
import time

tree = BPlusTree('./tree.db',order=50)
for i in range(1000):
    data = (i*2).to_bytes(10,'big')
    tree[i] = data
key = int(input("Enter the key : "))
start = time.time()
byteData = tree.get(key)
end = time.time()
intdata = int.from_bytes(byteData,'big')
print("Value : ",intdata)
print("Time taken : ",(end-start)*1000," ms")
