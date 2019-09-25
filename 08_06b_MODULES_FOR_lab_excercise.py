inputdata = [0,1,2,3,5,8,13,21,34,55,89]

import random
import math





for i in range (len(inputdata)):
    minvalue = (inputdata[i] - random.random()) * inputdata[i]
    maxvalue = (inputdata[i] + random.random()) * inputdata[i]
    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print('for %d line min is %f, max is %f, maxint is %d, minint is %d' % (i+1, minvalue, maxvalue, mininteger, maxinteger))




        
        
