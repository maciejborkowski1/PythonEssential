def PrintAnimal(animal=''):
    #funkcja będzie zwracała odpowiednie zwierze w zaleznosci od przekazanego parametru
    if animal == 'cat': 

        txt = r'''
    |\---/|
    | o_o |
     \_^_/'''
        print(txt)
        return True

    elif animal == 'bear':

        print(r'''
    /  \.-"""-./  \
    \    -   -    /
     |   o   o   |
     \  .-'"'-.  /
      '-\__Y__/-'
         `---`''')
        return True
    
    elif animal == 'bat':

        txt = r'''
       /\                 /\
      / \'._   (\_/)   _.'/ \
     /_.''._'--('.')--'_.''._\
     | \_ / `;=/ " \=;` \ _/ |
      \/ `\__|`\___/`|__/`  \/
              \(/|\)/       '''
        print(txt)
        return True
    else:
        print('Cannot print: \'%s\'. Correct values for the parameter are: cat, bear, bat.' % (animal))
        return False

if PrintAnimal(''):
    print('Value is correct')
else:
    print('Incorrect value')


    



