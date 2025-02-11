n = list(map(int,input().split()))
count = 0
for i in range(4):
    for j in range(i+1,4):
        if n[i]==n[j]:
            count+=1
            break
print(count)
