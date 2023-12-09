def add(a,b):
    maxlen = max(len(a),len(b))
    a = a.zfill(maxlen)
    b = b.zfill(maxlen)
    result = ""
    carry = 0
    for i in range(maxlen-1,-1,-1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r%2==1 else '0')+result
        carry = 0 if r<2 else 1
    if carry!=0:
        result = '1'+result
    return result.zfill(maxlen)

def complement(a):
    res = ''
    for i in a:
        if i == '1':
            res+='0'
        if i == '0':
            res+='1'
    res = add(res,'1')
    return res

def ls(a,q):
    a = a[1:]+q[0]
    q = q[1:]+'-'
    return a,q

def nres(a,Q,M,n,nlen):
    print(f"{n}\t{a}\t\t{Q}")
    if n == 0:
        if a[0]=='1':
            a = add(a,M)
            if len(a)>nlen:
                a = a[1:]
        return print(f'A is {a} and Q is {Q}')
    a,Q = ls(a,Q)
    print(f"{n}\t{a}\t\t{Q}\t\tAfter LRS ")
    if a[0]=='1':
        a = add(a,M)
        if len(a)>nlen:
            a = a[1:]
        print(f"{n}\t{a}\t\t{Q}\t\tAfter A = A+M ") 
        Q = Q.replace('-','1') if a[0]=='0' else Q.replace('-','0')
    elif a[0] == '0':
        a = add(a,complement(M))
        if len(a)>nlen:
            a = a[1:]
        print(f"{n}\t{a}\t\t{Q}\t\tAfter A = A-M ")
        Q = Q.replace('-','1') if a[0]=='0' else Q.replace('-','0')
    return nres(a,Q,M,n-1,nlen)
        
        

def main():
    Q = int(input("Enter the Q : "))
    M = int(input("Enter the M : "))
    n = len(bin(max(abs(Q),abs(M)))[2:])+1
    
    Q = bin(Q)[2:].zfill(n-1) if Q>=0 else complement(bin(Q)[3:].zfill(n))
    M = bin(M)[2:].zfill(n) if M>=0 else complement(bin(M)[3:].zfill(n))
    
    print(f"M = {M}, Q = {Q}, A={'0'*n}")
    print(f'M is {M} Q is {Q} and n is {n}')
    print("Count\tA\t\tQ\t\tAny action")
    print("---------------------------------------------------------------")
    print(nres('0'*n,Q.zfill(n-1),M.zfill(n),n-1,n))
    
main()
    