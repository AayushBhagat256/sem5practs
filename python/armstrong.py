inpnumber = input('Enter the number: ')
number = int(inpnumber)
temp = number
num_digits = len(inpnumber)
armstrong_sum = 0

while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp = temp // 10

if armstrong_sum == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
print(str(153//10)) #15

revnumber  = inpnumber[::-1]
print(revnumber)