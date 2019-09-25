'''
zmienna i ma wartość 10, korzystajac z petli for obliczamy silnia z i
'''
i=10
y=1
for j in range (1,11):
    y *= j
    print(i, y)

print('-------------------')


'''
tutaj korzystajac z petli deklarujemy wartości od 1 do 10,
a w zagnieżdzonej pętli wyznaczamy silnie kolejno dla każdej z tej wartości
'''
for a in range (1,11):
    line = a
    for z in range (1,a):
        line *= z
    print (a, '\t', line)

print('-------------------')

'''
Utwórz pętlę for iterującą przez listę rzeczowników i zagnieżdżoną w niej pętlę
for iterującą przez listę przymiotników. Wyświetl wszystkie pary przymiotnik
- rzeczownik
'''
x = 1
listNoun = ['dog', 'potato', 'meal', 'icecream', 'car']
listAdj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for listA in listNoun:
    for listB in listAdj:

        print (listB, listA)
