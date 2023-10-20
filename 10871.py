N,X=map(int,input().split())
A=list(map(int,input().split()))
def isBiggerThenFive(y):
    return y<X
B = list(filter(isBiggerThenFive,A))
print(*B)