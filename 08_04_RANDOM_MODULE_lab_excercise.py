import random

for i in range(10):
    print (random.randint(1,100))

number1 = random.randint(1,100)
counter = 1
number2 = random.randint(1,100)
print('Po %d próbie wylosowaliśmy %d' % (counter, number2))
while number2 is not number1:
    counter+=1
    number2 = random.randint(1,100)
    print('Po %d próbie wylosowaliśmy %d' % (counter, number2))

print('Po %d próbie wylosowaliśmy %d równe number1, czyli %d' % (counter, number2, number1))
print('----------------------------')
countries = [
        'Uruguay',
        'Russia',
        'Saudi Arabia',
        'Egypt',
        'Spain',
        'Portugal',
        'Iran',
        'Morocco',
        'France',
        'Denmark',
        'Peru',
        'Australia',
        'Croatia',
        'Argentina',
        'Nigeria',
        'Iceland',
        'Brazil',
        'Switzerland',
        'Serbia',
        'Costa Rica',
        'Sweden',
        'Mexico',
        'Korea Republic',
        'Germany',
        'Belgium',
        'England',
        'Tunisia',
        'Panama',
        'Colombia',
        'Japan',
        'Senegal',
        'Poland'
        ]

random.shuffle(countries)
groupNumber = 0

for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber+=1
        print('---Grupa %d---' % (groupNumber))
    print(countries[i])
