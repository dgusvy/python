T = int(input())
for _ in range(T):
    F = ""
    R, S = input().split()
    R = int(R)
    for i in range(len(S)):
        F = F + S[i]*R
    print(F)