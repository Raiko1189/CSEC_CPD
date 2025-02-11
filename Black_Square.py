m = list(map(int, input().split()))
n = input().strip()  


total = 0


for char in n:
    index = int(char) - 1  
    if 0 <= index < len(m): 
        total += m[index]  

print(total)
