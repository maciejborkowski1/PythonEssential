number = 1
previus_number = 0
     
while number<50:
    print(number + previus_number)
    previus_number=number
    number = number+1 ## number+=1 is correct too
'''
the reason was in the last line
WAS: number+1

'''

text = ''
number = 10
condition = True
     
while condition:
'''
Here is a correct
'''
    if len(text)>number:
        condition=False 
    text+='x'
    print(text)
'''
Here is a bug
'''
##if len(text)>number:
##    condition=False        


'''
The reason of the bug: if is a wrong place.\
'''

