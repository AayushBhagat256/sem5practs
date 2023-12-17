n = 5
#square pattern
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print()
    
print("----------------------------")
#left right angle triangle
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("----------------------------")
#decressing right angle triangle 5 4 3 2 1
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()
    
print("----------------------------")
#right right angle triangle 5 4 3 2 1
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
print("----------------------------")
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
print("----------------------------")
print("Pyramid")
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
    
print("----------------------------")

""" 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
----------------------------
* 
* * 
* * * 
* * * * 
* * * * * 
----------------------------
* * * * * 
* * * * 
* * *
* *
*
----------------------------
          *
        * *
      * * *
    * * * *
  * * * * *
----------------------------
  * * * * *
    * * * *
      * * *
        * *
          *
----------------------------
Pyramid
     *
    * *
   * * *
  * * * *
 * * * * *
"""