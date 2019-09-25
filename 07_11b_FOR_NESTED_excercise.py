i = 10
result = 1
 
for x in range(1, i+1):
 
    if x == 1:
        print("%s! jest rowna 1" % str(x))
 
    else:
        
        # petla dla textu z mnozeniem liczb
        for z in range(1, x):  
            if z == 1:
                text = str(z)
            else:
                text += "*" + str(z)
 
        result *= x
 
        print("%s! to inaczej %s*%s i jest rowna %d" % (str(x), text, str(x), result))
