import os

try:

    line = input('Please enter a price which you want pay for udemy course')

    path = input('Plese enter a output file path')

    file = open(path, 'w')
    file.write(line)
    file.close()
    value = int(line)
    print('The value saved in file is: %d' % value)

except FileNotFoundError as e:
    print('Error opening file, please check entered path')
    print('Error details:',e)

except ValueError as e:
    print('The value entered cannot be converted to a number')
    print('Error details:',e)

except:
    print('Sorry - we have an error')

else:
    print('Actions completed successfully')
