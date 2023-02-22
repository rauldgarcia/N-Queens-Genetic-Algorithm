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

def cuentanqueen (matriz):
    total=0
    matrizt=np.transpose(matriz)
    for i in range(nqueen):
        for j in range(nqueen):
            if matriz[i][j]==1:
                renglon=matriz[i].tolist()
                n=renglon.count(1)
                total+=n-1

            if matrizt[i][j]==1:
                renglon=matrizt[i].tolist()
                n=renglon.count(1)
                total+=n-1

    return total

m1=creamatriz()
print(m1)
print(cuentanqueen(m1))