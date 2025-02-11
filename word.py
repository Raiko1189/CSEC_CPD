n = input()
def count_upper_lower(text):
    upper_count = 0
    lower_count = 0

    for char in n:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count
upper_count, lower_count = count_upper_lower(n)
if upper_count > lower_count:
    print(n.upper())
elif upper_count == lower_count:
    print(n.lower())
else:
    print(n.lower())
