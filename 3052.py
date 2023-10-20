L = []
for _ in range(10):
    a = int(input())
    L.append(a%42)
L = set(L)
L= list(L)
print(len(L))