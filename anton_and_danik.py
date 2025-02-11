n = int(input())
S =input().strip()
anton_wins = S.count("A")
danik_wins = S.count("D")
if anton_wins > danik_wins :
    print("Anton")
elif anton_wins < danik_wins :
    print("Danik")
else:
    print ("Friendship")
