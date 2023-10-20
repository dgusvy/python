M,N = map(int,input().split())
L = [i+1 for i in range(M)]
for _ in range(N):
    i, j = map(int,input().split())
    L[i-1], L[j-1] = L[j-1], L[i-1]
print(*L)