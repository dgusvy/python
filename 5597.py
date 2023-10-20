L = [i+1 for i in range(30)]
for _ in range(28):
    a = int(input())
    L.remove(a)
print(*L, sep="\n")