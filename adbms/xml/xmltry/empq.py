import xml.etree.cElementTree as EL

tree = EL.parse('emp.xml')
root = tree.getroot()

employees = root.findall(".//emp")
for emp in employees:
    print("Emp id is : ",emp.get('id'))
    print("Emp name is : ",emp.find('name').text)
    print("Emp sal is : ",emp.find('salary').text)
    print("Emp post is : ",emp.find('post').text)
print("---------------------------------------------")

print('Employee with post SDE')
sdes = root.findall(".//emp[post='SDE']")
for emp in sdes:
    print("Emp id is : ",emp.get('id'))
    print("Emp name is : ",emp.find('name').text)
    print("Emp sal is : ",emp.find('salary').text)
    print("Emp post is : ",emp.find('post').text)
    
print("------------------------------")
print('Employee with salary less than 1000')
salemp = root.findall(".//emp")
for emp in salemp:
    eid = emp.get('id')
    ename = emp.find("name").text
    sal = int(emp.find("salary").text)
    if sal<1000:
        print(f'emp id is {eid} emp name is {ename} empsal is {sal}')
print("------------------------------")
print("chnaging salary of emp with 1")
target = root.find(".//emp[@id='1']")
if target is not None:
    newSal = '1000'
    target.find('salary').text = newSal
    tree.write('emp.xml')
    print('Salary updated')
else:
    print("No id found")
    
print('------------------------')
print("Delete id 2")
targetdel = root.find(".//emp[@id='2']")
if targetdel is not None:
    root.remove(targetdel)
    tree.write("emp.xml")
    print("user Deleted")
else:
    print("id not found")
    
    
print('-------------------------------------------')
print('Add a new Employee')
newemp = EL.Element("emp")
newemp.set('id','7')

name = EL.SubElement(newemp,"name")
name.text = "messi"
sal = EL.SubElement(newemp,"sal")
sal.text = "500"
post = EL.SubElement(newemp,"post")
post.text = "FB"

root.append(newemp)
tree.write('emp.xml')
print("Emp added")
