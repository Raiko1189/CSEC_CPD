n = int(input())  # Number of cards
cards = list(map(int, input().split()))  

sereja_score = 0
dima_score = 0
turn = 0  
while cards:
    
    if cards[0] > cards[-1]:
        chosen = cards.pop(0)  
    else:
        chosen = cards.pop()  
    
    
    if turn % 2 == 0:
        sereja_score += chosen  
    else:
        dima_score += chosen  
   
    turn += 1

print(sereja_score, dima_score)
