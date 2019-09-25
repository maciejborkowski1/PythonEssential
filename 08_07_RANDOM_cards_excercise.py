colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
allCards = []

for colorsList in colors:
    for figuresList in figures:
        card = colorsList + ' ' + figuresList
        allCards.append(card)

print(allCards)

import random

random.shuffle(allCards)

print(allCards)

playerOne = []
playerTwo = []

maks = len(allCards)

for i in range (0, maks-1):
    if i % 2 == 0:
        playerOne.append(allCards[i])
    else:
        playerTwo.append(allCards[i])

print(playerOne)
print(playerTwo)

'''
    OR
'''

player1 = allCards[:12]
player2 = allCards[12:]

print(playerOne)
print(playerTwo)
