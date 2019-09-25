from geom import *

def giveGeomSeqElement(a1=2,factor=2,index=2):
##funkcja do obliczania wartości danego elementu w ciągu gemetrycznym, domyslnie index=2
    indexValue = a1 * pow(factor,index-1)
    return indexValue
print(giveGeomSeqElement())
print(giveGeomSeqElement(1,2,64))
print('----------------------------------------')

a1=3
factor=2
maxindex=10

for i in range (1,maxindex):
    print(giveGeomSeqElement(a1=3,index=i))

print('----------------------------------------')


def giveFactorForGeomSeq (term, nextTerm):
##określenie wartości współczynnika przy znanych dwóch kolejnych wyrazach ciągu
    factorValue = nextTerm / term
    return factorValue
print(giveFactorForGeomSeq(12,24))
print('----------------------------------------')

def giveSumOfNElementsGeomSeq(a1=2,factor=2,n=2):
##wyliczenie sumy pierwszych wyrazow ciagu(n-ile wyrazow do sumy)
    sumValue = a1 * (1-(pow(factor,n))/(1-factor))
    return sumValue
print (giveSumOfNElementsGeomSeq(factor=3, n=4))
