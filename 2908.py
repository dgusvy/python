A, B = input().split()
C = int(A[::-1])
D = int(B[::-1])
if C > D:
    print(C)
else:
    print(D)