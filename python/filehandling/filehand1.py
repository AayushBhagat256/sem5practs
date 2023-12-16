# Take 10 numbers from the user. Add it to a file (lets say T1.txt). Read the contents of 
# the file and sort the data. Put the sorted data in a different file (T2.txt)

# newfile = open("./filehandling/myfile.txt","w") #create a new file 
n = int(input("Enter N numbers : "))
t1 = open("./filehandling/t1.txt","w")
for i in range(n):
    t1.write(str(input("Enter the number : "))+"\n")
print("number taken in")
t1.close()

t1read = open("./filehandling/t1.txt","r")
numlist = []
for num in t1read.readlines():
    numlist.append(int(num))
print(numlist)
numlist.sort()
print(numlist)
t1read.close()

t2 = open("./filehandling/t2.txt","w")
for i in range(len(numlist)): #or use in numlist
    t2.write(str(numlist[i])+"\t")
print("sorting done in t2")
t2.close()
