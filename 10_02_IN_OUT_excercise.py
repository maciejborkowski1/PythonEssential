import os

webAddresses = []

line = input('Please enter site address')

while line:
    webAddresses.append(line)
    line = input('Please enter site address')

dirName = os.getcwd()

fileName = input('Please enter new file name')

filePath = os.path.join(dirName,fileName)

with open(filePath, 'w') as file:
    for address in webAddresses:
        file.write(address+'\n')
