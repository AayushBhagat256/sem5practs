# Take a myfile.txt file with several words in it. Sort the words lexicographically and put 
# the sorted words in a different file lexi.txt.

with open('./filehandling/myfile.txt','r') as t1:
    words = t1.read().split()
    
print(words)
sortedWords = sorted(words)
print(sortedWords)

with open('./filehandling/lexi.txt','w') as t2:
    for words in sortedWords:
        t2.write(words + "\n")
print("lexi sorting done")