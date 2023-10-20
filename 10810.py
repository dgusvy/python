N,M=map(int,input().split())
L = [0 for i in range(N)] #바구니
for i in range(M):
    i,j,k = map(int,input().split())
    for a in range(i-1,j):
        L[a] = k
print(*L)