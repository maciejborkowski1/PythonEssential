shoeSize=43
number=((shoeSize * 5 + 50) * 20 + 1019) - 1989
print('My shoes size is:', number //100)
print('I am', number %100,'years old.')


someNumber=7
five = (someNumber * 2 + 10) / 2 - someNumber
print('Five is always', five)

"""
presence = 0.85
average = 3.5
exam = False
"""

presence = 0.40
average = 2.5
exam = True

'''
    first variant:
'''
isHePassed = presence >= 0.80 and average >= 3.0 \
            or exam
#isHePassed = presence >= 0.80 and average >= 3.0 or exam

'''
    second variant:
'''

#isHePassed = presence >= 0.80 and average >= 3.0 and exam

print('Student pass semester:',isHePassed)
