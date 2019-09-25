def PrintAnimal(*animals):
    #funkcja będzie zwracała odpowiednie zwierze w zaleznosci od przekazanego parametru

    for animal in animals:
        if animal == 'cat': 

            txt = r'''
        |\---/|
        | o_o |
         \_^_/'''
            print(txt)

        elif animal == 'bear':

            print(r'''
        /  \.-"""-./  \
        \    -   -    /
         |   o   o   |
         \  .-'"'-.  /
          '-\__Y__/-'
             `---`''')
        
        elif animal == 'bat':

            txt = r'''
           /\                 /\
          / \'._   (\_/)   _.'/ \
         /_.''._'--('.')--'_.''._\
         | \_ / `;=/ " \=;` \ _/ |
          \/ `\__|`\___/`|__/`  \/
                  \(/|\)/       '''
            print(txt)
        else:
            print('Cannot print. Correct values for the parameter are: cat, bear, bat.')
    return

PrintAnimal('cat','bear')
print('--------------------------------')
PrintAnimal('cat','cow')
print('--------------------------------')
PrintAnimal('cat','bat','bear')
print('--------------------------------')
PrintAnimal('dog','chicken','lizard')


    



