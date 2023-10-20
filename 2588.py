A = int(input())
B = int(input())
A = int(A)
B = int(B)
B1 = B//100
B2 = B//10-B1*10
B3 = (B-(B2*10+B1*100))
print(A*B3, A*B2 , A*B1, A*B , sep='\n')