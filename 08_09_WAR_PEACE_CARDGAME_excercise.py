colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
        {'Figure':'Ace',  'Power':14},
        {'Figure':'King', 'Power':13},
        {'Figure':'Queen','Power':12},
        {'Figure':'Jack', 'Power':11},
        {'Figure':'10',   'Power':10},
        {'Figure':'9',    'Power':9}]
allCards = []

for currentColor in colors:
    for currentFigure in figures:
        aCard = currentFigure.copy()
        aCard['Color'] = currentColor
        allCards.append(aCard)

import random

random.shuffle(allCards)

##print(allCards)

maks = len(allCards)
playerOne = []
playerTwo = []

for i in range (0, maks):
    if i % 2 == 0:
        playerOne.append(allCards[i])
    else:
        playerTwo.append(allCards[i])

print(len(playerOne))
print(len(playerTwo))

while len(playerOne) > 0 and len(playerTwo) > 0:
    cardOne = playerOne.pop(0)
    cardTwo = playerTwo.pop(0)
    if cardOne['Power'] == cardTwo['Power']:
        playerOne.append(cardOne)
        playerTwo.append(cardTwo)
        print('DRAW')
    elif cardOne['Power'] > cardTwo['Power']:
        playerOne.append(cardOne)
        playerOne.append(cardTwo)
        print('Round for PlayerOne', 'P1 has %d cards, P2 has %d cards' % (len(playerOne), len(playerTwo)))
    else:
        playerTwo.append(cardTwo)
        playerTwo.append(cardOne)
        print('Round for PlayerTwo', 'P1 has %d cards, P2 has %d cards' % (len(playerOne), len(playerTwo)))

if len(playerOne) > len(playerTwo):
    print('PlayerOne WON!')
else:
    print('PlayerTwo WON!')
