import random
card_faces=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suites = ["Hearts","Diamonds","Clubs","Spades"]
deck=[]
for k in range(4):
    for l in range(13):
        card = (card_faces[l] + " of " + suites[k])
        deck.append(card)
random.shuffle(deck)

for m in range(52):
    print(deck[m])
