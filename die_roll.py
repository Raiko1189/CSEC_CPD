from fractions import Fraction
m = list(map(int,input().split()))
n = max(m)
count = 0
for i in range (n,7):
    count+=1
if count==6:
    print("1/1")
else:
    m =(Fraction(count,6))
    print(m)
