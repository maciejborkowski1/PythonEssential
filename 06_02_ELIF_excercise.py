minLikes = 500
minShares = 100

numLikes = 501
numShares = 101

if numLikes >= minLikes and numShares >= minShares:
    print('Promotion is working')
else:
    if numLikes < minLikes and numShares < minShares:
        print('We need more likes and shares to procces promotion')
    else:
        if numLikes < minLikes:
            print('Enough shares, but still we need more likes')
        else:
            print('Enough likes, but still we need more shares')

print('------')

if numLikes >= minLikes and numShares >= minShares:
    print('Promotion is working')
elif numLikes < minLikes and numShares < minShares:
    print('We need more likes and shares to procces promotion')
elif numLikes < minLikes:
    print('Enough shares, but still we need more likes')
else:
    print('Enough likes, but still we need more shares')
