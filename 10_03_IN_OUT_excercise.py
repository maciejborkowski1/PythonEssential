import os

fileName = input('Enter last new file name')
dirName = os.getcwd()
filePath = os.path.join(dirName,fileName)

while not os.path.isfile(filePath):
    print('The file not exist, please enter correct file name')
    fileName = input('Enter last new file name')
    filePath = os.path.join(dirName,fileName)

webAddresses = []

with open(filePath, 'r') as file:
    for line in file:
        currentLine = line.replace('\n','')
        webAddresses.append(currentLine)

##for address in webAddresses:
##    if address.endswith('.pl'):
##        print('Address "%s" is polish site' % address)
##    else:
##        print('Address "s" isn\'t polish site' % address)


websPlFile = 'webs_pl.txt'
websOtherFile = 'webs_other.txt'


plFile = open(os.path.join(os.path.dirname(filePath), websPlFile), 'w')
otherFile = open(os.path.join(os.path.dirname(filePath), websOtherFile), 'w')
    
for address in webAddresses:
    if address.endswith('.pl'):
        plFile.write(address+'\n')
    else:
        otherFile.write(address+'\n')

plFile.close()
otherFile.close()
