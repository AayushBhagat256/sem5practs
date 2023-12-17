#reading the file :
file = open("./regex/reg.txt",'r')
text = file.read()
print(text)
print(type(text)) #str

import re
#pattern for name
patternNames = r'[M][rs]+[\.] [a-zA-z]+'

names = re.findall(patternNames,text)
print(names)

# pattern for email
patternEmail = r'[a-zA-Z0-9_\-\.]+@[a-z]+\.[a-z]{2,3}'
email = re.findall(patternEmail,text)
print(email)

#pattern for phone numbers
patternphones = r'[0-9]+[*\-]?[0-9]+[*\-]?[0-9]+'
numbers = re.findall(patternphones,text)
print(numbers)

#pattern for websites
# patternSites = r'http?s?://[w]+\.[a-zA-Z]+\.[a-zA-Z\.a-zA-z]+' #correct for www
patternSites = r'http?s?://[wplus]+\.[a-zA-Z]+\.[a-zA-Z\.a-zA-z]+' #correct for www and plus
sites = re.findall(patternSites,text)
print(sites)

#without http https and ://
patternSites = r'[wplus]+\.[a-zA-Z]+\.[a-zA-Z\.a-zA-z]+' #correct for www and plus
sites = re.findall(patternSites,text)
print(sites)

""" 
Mr. Anderson
Ms. Thareja
Mrs. Morris
Mr. Roy
Ms. Gandhi
Mrs. Modi
https://www.google.com
http://www.udemy.com
www.udacity.com
https://www.stackoverflow.com
http://www.djsce.ac.in
https://plus.google.com
rishit.grover@gmail.com
kapeesh.grover@yahoo.co.in
abhishek.shah@gmail.com
shahp98@gmail.com
demo_user@gmail.com
rolflmoa@yahoo.co.in
27777647
233*333*88
455-78-888
022-240-93836
02642*221*381

"""