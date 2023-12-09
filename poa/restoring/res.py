def add(a,b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
    if carry != 0:
        result = '1' + result
    return result.zfill(max_len)

def complement(a):
    res = ''
    for i in a:
        if i=='1':
            res+='0'
        elif i=='0':
            res+='1'
    res = add(res,'1')
    return res

def ls(a,Q):
    a = a[1:]+Q[0]
    Q = Q[1:]+'-'
    return a,Q

def res(a,Q,M,n,nlen):
    if n==0:
      return print(f'A is {a} and Q is {Q}')
    a,Q = ls(a,Q)
    print(f"{n}\t{a}\t\t{Q}\t\tAfter LRS ")
    a = add(a,complement(M))  
    if len(a)>nlen:
        a = a[1:]
    print(f"{n}\t{a}\t\t{Q}\t\tAfter A = A-M ")
    if a[0]=='1':
        print('A<0')
        Q = Q.replace('-','0')
        a = add(a,M)
        if len(a)>nlen:
            a = a[1:]
        print(f"{n}\t{a}\t\t{Q}\t\tAfter A = A+M ") 
    elif a[0]=='0':
        print('A is >0')
        Q = Q.replace('-','1')
    return res(a,Q,M,n-1,nlen)
    
        
    
    

def main():
    Q = int(input("Enter the Q: "))
    M = int(input("Enter the M : "))
    
    n = len(bin(max(abs(Q),abs(M)))[2:])+1
    
    Q = bin(Q)[2:].zfill(n) if Q>=0 else complement(bin(Q)[3:].zfill(n))
    M = bin(M)[2:].zfill(n) if M>=0 else complement(bin(M)[3:].zfill(n))
    
    print(f'M is {M} Q is {Q} and n is {n}')
    print("Count\tA\t\tQ\t\tAny action")
    print("---------------------------------------------------------------")
    print(res('0' *n,Q.zfill(n),M.zfill(n),n,n))
    
    
    
main()