number = 20730906
tmpNumber = number
sumOfDigit = 0

while tmpNumber >0:
    digit = tmpNumber % 10
    sumOfDigit+= digit
    tmpNumber = tmpNumber //10
else:
    print(sumOfDigit)


''' lepszy sposób z pętlą for '''

number = 20730906
sum = 0
for d in str(number):
    sum += int(d)
print("sum =", sum)
