text = 'United Space Alliance: This company provides major support to NASA for various projects, such as the space shuttle. One of its projects is to create Workflow Automation System (WAS), an application designed to manage NASA and other third-party projects. The setup uses a central Oracle database as a repository for information. Python was chosen overlanguages such as Java and C++ because it provides dynamic typing and pseudo-code–like syntax and it has an interpreter. The result is that the application is developed faster, and unit testing each piece is easier.'

words = text.split(' ')
wordLenght = 6
shortWords = 0
longWords = 0
i = 0

while i < len(words):
    if len(words[i]) > wordLenght:
        longWords+=1
    else:
        shortWords+=1
    i+=1

print(longWords)

##print(words)
