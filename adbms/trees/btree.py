from BTrees.IIBTree import IIBTree
import time

t = IIBTree()
insertTimeS = time.time()
for i in range(1000):
    t.update({i:2*i})
insertTimeE = time.time()
print(f'The time take is {round((insertTimeE-insertTimeS)*1000,3)} ms')
key = int(input('Enter the key : '))
searchTimeS = time.time()
if t.has_key(key):
    print(t[key])
searchTimeE = time.time()
print(f'The time take is {round((searchTimeE-searchTimeS)*1000,3)} ms')