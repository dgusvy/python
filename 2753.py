X = int(input())
if X%4==0 and not X%100==0 or X%400==0:
    print("1")
else:
    print("0")