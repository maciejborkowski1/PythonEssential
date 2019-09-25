#helloMessage='Hello %s!'
#print(helloMessage %('Kate'))
#print(helloMessage %('Chris'))

#helloMessage='Hello {0:s}!'
#print(helloMessage.format('Kate'))
#print(helloMessage.format('Chris'))

#helloMessage='%s has %d %s'
#print(helloMessage % ('Kate',1,'animal'))
#print(helloMessage % ('Chris',10000,'$'))

helloMessage='{0:s} has {1:d} {2:s}'
print(helloMessage.format('Kate',1,'animal'))
print(helloMessage.format('Chris',1000,'$'))

line='{0:20s} costs {1:6d} €'
print(line.format('IceCream',3).upper())
print(line.format('Trip to Venice',119).upper())
print(line.format('Pizza Hawaii',6).upper())
