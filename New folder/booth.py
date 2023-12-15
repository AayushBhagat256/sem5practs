def add(a,b):
    maxlen = max(len(a), len(b))
    a = a.zfill(maxlen)
    b = b.zfill(maxlen)
    result = ''
    carry = 0
    for i in range(maxlen-1,-1,-1):
        r = carry
        r+=1 if a[i]=='1' else 0
        r+=1 if b[i]=='1' else 0
        result = ('1' if r%2==1 else '0')+result
        carry = 0 if r<2 else 1
    if carry!=0:
        result = '1'+result
    return result.zfill(maxlen)
    
def complement(x):
    res = ''
    for i in x:
        if i == '1':
            res+='0'
        if i == '0':
            res+='1'
    res = add(res,'1')
    return res

def ars(a,Q,q):
    q = Q[-1]
    Q = a[-1]+Q[:-1]
    a = a[0]+a[:-1]
    return a ,Q , q

def booth(a, Q, q, M, n, nlen):
    print(f'{n}\t{a}\t\t{Q}\t\t{q}')
    if n == 0:
        return print(f'The A is {a} Q is {Q} and q is {q}')
    elif Q[-1] == '1' and q[-1] == '0':
        print("10<--")
        a = add(a, complement(M.zfill(nlen)))
        if len(a) != nlen:
            a = a[1:]
        print(f"{n}\t{a}\t\t{Q}\t\t{q}\t before ars")
        a, Q, q = ars(a, Q, q)
    elif Q[-1] == '0' and q[-1] == '1':
        print("01<---")
        a = add(a, M)
        if len(a) != nlen:
            a = a[1:]
        print(f"{n}\t{a}\t\t{Q}\t\t{q}\t before ars")
        a, Q, q = ars(a, Q, q)
    elif (Q[-1] == '1' and q[-1] == '1') or (Q[-1] == '0' and q[-1] == '0'):
        print("00 or 11 <-----")
        a, Q, q = ars(a, Q, q)
    return booth(a, Q, q, M, n - 1, nlen)

Q = int(input("Enter the Q : "))
M = int(input("Enter the M : "))

n = len(bin(max(abs(Q),abs(M)))[2:])+1
print(f'The n is {n}')

Q = bin(Q)[2:].zfill(n) if Q>=0 else complement(bin(Q)[3:].zfill(n))
# M = bin(M)[2:].zfill(n) if M>=0 else complement(bin(M)[3:].zfill(n))
if M < 0:
    M = complement(bin(M)[3:].zfill(n))
else:
    M = bin(M)[2:].zfill(n)

print(f'M is {M} Q is {Q} and n is {n}')

print(f'n\tA\t\tQ\t\tq')
print(booth('0000',Q.zfill(n),'0',M.zfill(n),n,n))
        