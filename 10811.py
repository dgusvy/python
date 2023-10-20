N, M = map(int,input().split())
L = [a+1 for a in range(N)]
for _ in range(M):
    i, j = map(int,input().split())
    for y in range(i,(j+i+1)//2):
        x = j + i - y - 2
        temp = L[y]
        L[y] = L[x]
        L[x] = temp
        print(*L)
print(L)