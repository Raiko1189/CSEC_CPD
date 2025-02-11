def min_rotation_steps(s):
    pos = 'a' 
    steps = 0

    for char in s:
        diff = abs(ord(char) - ord(pos))
        steps += min(diff, 26 - diff)  
        pos = char 

    return steps
s = input().strip()
print(min_rotation_steps(s))
