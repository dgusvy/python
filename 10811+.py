N, M = map(int,input().split())
L = [a+1 for a in range(N)]

for _ in range(M):
    i, j = map(int,input().split())
    
    print(*L)