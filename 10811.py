M, N = map(int,input().split())
L = [i+1 for i in range(M)]
for _ in range(N):
    i, j = map(int,input().split())
    for a in range(i-1,j-1):
        L[a], L[j-a-1] = L[j-a-1], L[a]
    print(L)
print(*L)