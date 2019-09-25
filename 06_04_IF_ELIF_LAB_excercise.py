musclePain = True
fever = False
weakness = False
isMan = True

##if musclePain and fever and weakness:
##    print('suspiction of influenza')
##else:
##    print('The flu is unlikely')

##if musclePain and fever and weakness:
##    print('suspiction of influenza')
##elif weakness and (not musclePain or not fever):
##    print('just take a rest!')
##else:
##    print('just may be cold')

if isMan and (musclePain or fever or weakness):
    print('suspiction of influenza')
elif musclePain and fever and weakness:
    print('suspiction of influenza')
elif not (musclePain or fever) and weakness:
    print('just take a rest')
else:
    print('just may be cold')

isCheckCompleted = False

print('CHECK IS COMPLETED' if isCheckCompleted else 'CHECK NOT DONE YET')
