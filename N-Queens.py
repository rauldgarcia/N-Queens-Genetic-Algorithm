import numpy as np
from random import *

nqueen=8 #se puede cambiar el numero de reinas (solo hay solución para n>=4)

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
    sr=np.sum(matriz, axis=1) #suma renglon
    sc=np.sum(matriz, axis=0) #suma columna

    for i in range(nqueen): #si en columna o renglon solo hay uno lo vuelve 0
        if sc[i]==1:
            sc[i]=0
        if sr[i]==1:
            sr[i]=0

    matrizflip=np.flip(m1,axis=1) #flip a matriz
    sumadiagonalid=0
    sumadiagonaldi=0
    for i in range(-nqueen,nqueen,1): #suma diagonales
        diagonalid=np.trace(matriz,offset=i)
        diagonaldi=np.trace(matrizflip,offset=i)
        if diagonalid>1:
            sumadiagonalid+=diagonalid
        if diagonaldi>1:
            sumadiagonaldi+=diagonaldi

    total=np.sum(sc)+np.sum(sr)+sumadiagonalid+sumadiagonaldi
    return total

m1=creamatriz()
print(m1)
print(cuentanqueen(m1))