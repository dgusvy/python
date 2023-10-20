버킷리스트=[]
for _ in range(9):
    a=int(input())
    버킷리스트.append(a)
print(max(버킷리스트))
b = max(버킷리스트)
print(버킷리스트.index(b)+1)