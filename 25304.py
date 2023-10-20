X = int(input())
N = int(input())
sum = 0
for _ in range(N):
    a,b = map(int,input().split())
    C = a*b
    sum = sum + C
if sum == X:
    print("Yes")
else:
    print("No")