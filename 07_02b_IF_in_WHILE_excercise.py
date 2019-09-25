texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

a = 0
max = len(texts)-1

while a < max:
    print (texts[a], texts[a+1])

    if len(texts[a]) == len(texts[a+1]):
        print('\tFOUND')

    a+=1
