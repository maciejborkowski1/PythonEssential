hitsTitles = ['BROTHER IN ARMS','BOHEMIAN RHAPSODY','STAIRWAY TO HEAVEN','RIDERS ON THE STORM','WISH YOU WERE HERE']
hitsTitles.append('CHILD IN TIME')
hitsTitles.append('AGAIN')
#print(hitsTitles)

hitsTitles.insert(2,'HOTEL CALIFORNIA')
#hitsTitles.insert(0,'THE SOUND OF SILENCE')
hitsTitles[0]='THE SOUND OF SILENCE'

hitsTitles.remove('HOTEL CALIFORNIA')

hitsTitles[0]='ENJOY THE SILENCE'

anotherHits = hitsTitles.copy()
anotherHits.reverse()
anotherHits.sort()

additionalSongs = ['NOTHING COMPARES 2 U','WISH YOU WERE HERE']
anotherHits.extend(additionalSongs)

print(hitsTitles)
print(anotherHits.pop(0))
print(anotherHits.pop(0))
print(anotherHits)
print(anotherHits.count('WISH YOU WERE HERE'),anotherHits.count('RIDERS ON THE STORM'))
#print(hitsTitles.index('THE SOUND OF SILENCE'))
anotherHits.clear()
print(anotherHits)
