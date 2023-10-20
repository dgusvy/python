H, M = map(int, input().split())
A = int(input())
X = (H + (M+A)//60)%24
Y = (M+A)%60
print(X,Y)