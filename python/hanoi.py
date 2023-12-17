N = int(input("Enter number of discs : "))

def hanoi(N,fromRod,torod,auxRod):
    if N==0:
        return
    hanoi(N-1,fromRod,auxRod,torod)
    print(f'Moved disc {N} from {fromRod} to rod{auxRod}')
    hanoi(N-1,auxRod,torod,fromRod)

hanoi(N,'A','C','B')