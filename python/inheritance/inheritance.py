""" 
Python Code to implement following inheritance example:
Classes: Employee, Developer, Tester, Manager.
Developer, tester, Manager inherit Employee.
Manager handles Developer, tester.
Manager class: implement functions to add Developer/Tester and Remove Developer/ 
Tester.
Display to see the list of employees he manages.
"""

class Employee:
    def __init__(self,empId,empName,role):
        self.empId = empId
        self.empName = empName
        self.role = role
    def printinfo(self):
        print(f'Emp id is {self.empId} empName is {self.empName} empRole is {self.role}')
        
class Developer(Employee):
    def __init__(self, empId, empName, role = "developer"):
        super().__init__(empId, empName, role)
        
class Tester(Employee):
    def __init__(self, empId, empName, role = "Tester"):
        super().__init__(empId, empName, role)
        
class Manager(Employee):
    def __init__(self, empId, empName, role = "manager"):
        super().__init__(empId, empName, role)
        self.empList = []
        
    def addEmployee(self,employee): #employee be any object and w'll check if its in class Developer or Tester
        if isinstance(employee,(Developer,Tester)):
            print(f'Employee is added to manager team : {employee.empName} role {employee.role}')
            self.empList.append(employee)
            
    def removeEmployee(self,employee):
        if isinstance(employee,(Developer,Tester)):
            print(f'{employee.role} {employee.empName} -> {employee.empId} is removed from this team')
            self.empList.remove(employee)
            
    def printTeam(self):
        print(f'Manager is {self.empId} {self.empName} {self.role}')
        for emp in self.empList:
            emp.printinfo()
        
# creating emp objects 
dev1 = Developer('1',"aayush")
dev2 = Developer('2',"Tony")
tester1 = Tester("1","Hulk")
tester2 = Tester("2","batman")

mag1 = Manager("1","bruce")

mag1.addEmployee(dev2)
mag1.addEmployee(tester1)

mag1.printTeam()

"""
Employee is added to manager team : Tony role developer
Employee is added to manager team : Hulk role Tester
Manager is 1 bruce manager
Emp id is 2 empName is Tony empRole is developer
Emp id is 1 empName is Hulk empRole is Tester
"""