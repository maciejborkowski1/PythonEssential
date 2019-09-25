dictionary = {'Google':'1480','Email':'300','Natural Traffic':'440','TV Spot':'700'}
chanelsUpdate = {'Natural Traffic':'520','News':'600'}

dictionary.update(chanelsUpdate)


#print(dictionary['Email'])
print(dictionary.keys())

#print(dictionary.pop('Email'))

del dictionary['Email']

print(dictionary)
