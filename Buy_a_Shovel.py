k,r = map(int,input().split())
burley = 10
for i in range (1,10):
    if (i*k-r)%10 == 0:
       print(i)
       break
    elif (i*k)%10==0:
       print(i)
       break
