import numpy as np
from random import *
import random
import time
inicio=time.time()

nqueen=8 #se puede cambiar el numero de reinas (solo hay solución para n>=4)
npoblacion=100 #se puede cambiar el numero de poblacion
npadres=int(npoblacion*0.2) #se puede cambiar el numero de padres
pcruza=0.7 #se puede cambiar porcentaje de cruza
pmuta=0.7 #se puede cambiar
iteraciones=2000

#crea matrices aleatorias de n numeros de 1 
def creaperm():
    return np.random.permutation(8)

def cuentanqueen(perm):

    matriz=np.zeros((nqueen,nqueen))
    for i in range(nqueen):
        matriz[i][perm[i]]=1

    matrizflip=np.flip(matriz,axis=1) #flip a matriz
    sumadiagonalid=0
    sumadiagonaldi=0

    for i in range(-nqueen+1,nqueen,1): #suma diagonales
        diagonalid=np.trace(matriz,offset=i)
        diagonaldi=np.trace(matrizflip,offset=i)
        if diagonalid>1:
            sumadiagonalid+=diagonalid
        if diagonaldi>1:
            sumadiagonaldi+=diagonaldi

    total=sumadiagonalid+sumadiagonaldi
    return total

def pmatriz(perm):
    matriz=np.zeros((nqueen,nqueen))
    for i in range(nqueen):
        matriz[i][perm[i]]=1

    return matriz

def flip(p):
    n=random.random()
    if n>p:
        return 1
    else:
        return 0

prueba=creaperm()
print(prueba)
print(cuentanqueen(prueba))
print(pmatriz(prueba))

poblacion=[[i for i in range(3)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
for i in range(npoblacion): #crea la poblacion
    poblacion[i][0]=creaperm()
    poblacion[i][1]=cuentanqueen(poblacion[i][0])

print(poblacion)