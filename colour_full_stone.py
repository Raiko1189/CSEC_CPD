n = input()
t = input()

d = 1

for i in range(len(t)):
    if d <= len(n) and n[d - 1] == t[i]:
        d += 1
print(d)
