n = input()
text = set(n)
count = len(text)
if count % 2 == 1:
    print("IGNORE HIM!")
elif count % 2 == 0:
    print("CHAT WITH HER!")
