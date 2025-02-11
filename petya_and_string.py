n = input()
m = input()
if n.casefold()>m.casefold():
    print("1")
elif m.casefold()>n.casefold():
    print("-1")
else :
    print("0")
