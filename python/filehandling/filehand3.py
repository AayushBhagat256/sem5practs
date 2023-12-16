# same as file hand 2 but reversing the words

def revwords(word):
    return word[::-1]

# print(revwords("aayush")) --> hsuyaa

with open('./filehandling/myfile.txt','r') as t1:
    words = t1.read()
    
print(words)
print(revwords(words))
rev = revwords(words)
t1.close()

with open('./filehandling/revwords.txt','w') as t2:
    for words in rev:
        t2.write(words+"\n")
print("ho gaya")
t2.close()