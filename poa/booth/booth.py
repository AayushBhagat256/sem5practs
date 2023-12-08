def decimalToBinary(dec,n):
    binary = format(int(dec),f'0{n}b')
    return binary
# print(decimalToBinary(3,3))

def twoComplement(a,n):
    res = ""
    for i in a:
        if i == '0':
            res+= '1'
        elif i == '1':
            res+= '0'
    result = addBinary(res,'1',n)
    return result
    

def negativeDec(dec,n):
    absolute = abs(int(dec))
    binary = decimalToBinary(absolute,n)
    # now we find twos complement of binary
    result = twoComplement(binary,n)
    return result
    
    
def addBinary(b1,b2,n):
    result = bin(int(b1,2)+int(b2,2))
    resultbin = result[2:]
    return resultbin

# print(negativeDec('-7',4))
# print(decimalToBinary('3',4))

def ars(a,Q,q):
    q = Q[-1]
    Q = a[-1]+Q[:-1]
    a = a[0]+a[:-1]
    return a,Q,q

def booth(a,Q,q,M,minusM,n):
    while n!=0:
        if Q[-1]=='0' and q[0]=='1':
            a = addBinary(a,M,4)
            a,Q,q = ars(a,Q,q)
            print(f'A={a},Q={Q},q={q} --> A=A+M,ARS')
        elif Q[-1]=='1' and q[0] == '0':
            a = addBinary(a,minusM,4)
            a,Q,q = ars(a,Q,q)
            print(f'A={a},Q={Q},q={q} --> A=A+(-M),ARS')
        else:
            a,Q,q = ars(a,Q,q)
            print(f'A={a},Q={Q},q={q} --> ARS') 
        n-=1
    print(f'The A is {a} the Q is {Q} the q is{q}')
        

def main():
    Q = '3'
    M = '-7'
    Qbin = decimalToBinary(Q,4)
    MBin = negativeDec(M,4)
    MminusBin = decimalToBinary(str(int(abs(int('-7')))),4)
    
    print(f'Q is {Qbin}')
    print(f'M is {MBin}')
    print(f'-M is {MminusBin}')
    booth('0000','0011','0',MBin,MminusBin,4)
    
main()
    

    