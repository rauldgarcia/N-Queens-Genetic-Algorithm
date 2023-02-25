import numpy as np
from random import *
import random

nqueen=8 #se puede cambiar el numero de reinas (solo hay solución para n>=4)
npoblacion=4 #se puede cambiar el numero de poblacion
npadres=int(npoblacion*0.5) #se puede cambiar el numero de padres

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

    matrizflip=np.flip(matriz,axis=1) #flip a matriz
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

def flip(p):
    n=random.random()
    if n>p:
        return 1
    else:
        return 0

poblacion=[[i for i in range(3)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
for i in range(npoblacion): #crea la poblacion
    poblacion[i][0]=creamatriz()
    poblacion[i][1]=cuentanqueen(poblacion[i][0])
    
sumareinas=np.sum(poblacion,axis=0)[1] #suma el total de ataques de reinas
print(sumareinas)
for i in range(npoblacion): #calcula el porcentaje de ser padre
    poblacion[i][2]=poblacion[i][1]/sumareinas

poblacion.sort(key=lambda x:x[1]) #ordena la matriz de acuerdo a numero de ataques de menor a mayor
print(poblacion)

padres=[[i for i in range(3)]for j in range(npadres)] #crea una matriz de largo de los padres
cont=0
while cont<npadres: #seleccion de padres
    for i in range(npoblacion):
        if cont<npadres:
            if flip(poblacion[i][2])==1:
                padres[cont][0]=poblacion[i][0]
                cont+=1
        else:
            break

print(padres)