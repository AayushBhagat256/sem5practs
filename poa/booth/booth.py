def add(a,b):
    maxlen = max(len(a),len(b))
    a = a.zfill(maxlen)
    b = b.zfill(maxlen)
    result = ''
    carry = 0
    for i in range(maxlen-1,-1,-1):
        r = carry
        r+=1 if a[i]=='1'else 0
        r+=1 if b[i]=='1'else 0
        result = ('1' if r%2==1 else '0')+result
        carry = 0 if r<2 else 1
    if carry!=0:
        result = '1'+result
    return result

def ars(a,Q,q):
    q = Q[-1]
    Q = a[-1]+Q[:-1]
    a = a[0]+a[:-1]
    return a,Q,q

def complement(a):
    res = ''
    for i in a:
        if i == '1':
            res += '0'
        elif i == '0':
            res += '1'
    res = add(res,'1')
    return res

def booth(a,Q,q,n,nlen,M):
    print(f'{n}\t{a}\t\t{Q}\t\t{q}')
    if n==0:
        return print(f"A is {a} and Q is {Q}")
    elif Q[-1]=='1' and q[-1]=='0':
        print("10<--")
        a = add(a,complement(M.zfill(nlen)))
        if len(a)!=nlen:
            a = a[1:]
        print(f"{n}\t{a}\t\t{Q}\t\t{q}\t before ars")
        a,Q,q = ars(a,Q,q)
    elif Q[-1]=='0' and q[-1]=='1':
        print("01<---")
        a = add(a,M)
        if len(a)!=nlen:
            a = a[1:]
        print(f"{n}\t{a}\t\t{Q}\t\t{q}\t before ars")
        a,Q,q = ars(a,Q,q)
    elif (Q[-1]=='1' and q[-1]=='1') or (Q[-1]=='0' and q[-1]=='0'):
        print("00 or 11 <-----")
        a,Q,q = ars(a,Q,q)
    return booth(a,Q,q,n-1,nlen,M)
        
        
        

def main():
    a = int(input("Enter Q : "))
    b = int(input("Enter M : "))
    n = len(bin(max(abs(a),abs(b)))[2:])+1
    
    a = bin(a)[2:].zfill(n) if a>=0 else complement(bin(a)[3:].zfill(n))
    b = bin(b)[2:].zfill(n) if b>=0 else complement(bin(b)[3:].zfill(n))
    
    print(f'M is {b} Q is {a} and n is {n}')
    print("Count\tA\tQ\tq")
    print('-------------------------------------------')
    print(booth('0'*n,a.zfill(n),'0',n,n,b.zfill(n)))
    
    
main()
    
    
    