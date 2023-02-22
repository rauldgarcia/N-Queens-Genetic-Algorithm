import numpy as np
from random import *

nqueen=4 #se puede cambiar el numero de reinas (solo hay solución para n>=4)

#crea matrices aleatorias de n numeros de 1 
def creamatriz ():

    matriz=np.zeros((nqueen,nqueen))
    i=0
    while i < nqueen:
        randomx=randint(0,nqueen-1)
        randomy=randint(0,nqueen-1)
        if matriz[randomx][randomy]==0:
            matriz[randomx][randomy]=1
            i+=1

    return matriz

m1=creamatriz()
m2=creamatriz()
print(m1)
print(m2)