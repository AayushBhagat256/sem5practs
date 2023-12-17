class Person:
    def __init__(self,fname,lname,age): #init function is basically used for initializing the values with a fixed parameter as self
        self.fname = fname
        self.lname = lname
        self.age = age
        
    def printFun(self):
        print(f'The name is {self.fname} {self.lname} and age is {self.age}')
        
p1 = Person(input('Enter your fname : '),input('Enter your lname: '),input('Enter your age: '))
p1.printFun()

#modifying
p1.age = '30'
p1.printFun()

#deleting obj property
del p1.age
p1.printFun()

#deleting obj
del p1
p1.printfun()