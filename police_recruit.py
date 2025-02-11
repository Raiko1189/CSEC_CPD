n = int(input())
m = list(map(int,input().split()))
available_police = 0
untreated = 0
for event in (m):
    if event == -1 :
        if available_police > 0 :
            available_police -= 1
        else:
            untreated += 1
    else :
        available_police += event

print(abs(untreated))


