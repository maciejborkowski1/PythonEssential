import random
myNumber = random.randint(0,20)
trials = 0
guess = -1

print('This a simple game about number. For start i think some number from 0 to 20, and you try to guess my number!')

while myNumber != guess:
    guess = int(input())
    trials+=1
    if myNumber == guess:
        print('Congratulations, you guess my number with a', trials , 'times!')
    elif guess > myNumber:
        print('Sorry, my number is smaller than your guess, try again!')
    else:
        print('Sorry, my number is greater than your guess, try again!')


input('Press enter to exit')
   
    
    
