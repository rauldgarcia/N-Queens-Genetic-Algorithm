import numpy as np
from random import *
import random

nqueen=8 #se puede cambiar el numero de reinas (solo hay solución para n>=4)
npoblacion=10 #se puede cambiar el numero de poblacion
npadres=int(npoblacion*0.2) #se puede cambiar el numero de padres
pcruza=0.5 #se puede cambiar porcentaje de cruza
pmuta=0.5 #se puede cambiar

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

def cruza(m1,m2):
    p=flip(pcruza) #volado si se cruzan o no
    if p==1:
        matriz=[[m1[0][0],m2[0][1],m2[0][2],m2[0][3],m2[0][4],m2[0][5],m2[0][6],m2[0][7]],
                [m1[1][0],m1[1][1],m2[1][2],m2[1][3],m2[1][4],m2[1][5],m2[1][6],m2[1][7]],
                [m1[2][0],m1[2][1],m1[2][2],m2[2][3],m2[2][4],m2[2][5],m2[2][6],m2[2][7]],
                [m1[3][0],m1[3][1],m1[3][2],m1[3][3],m2[3][4],m2[3][5],m2[3][6],m2[3][7]],
                [m1[4][0],m1[4][1],m1[4][2],m1[4][3],m2[4][4],m2[4][5],m2[4][6],m2[4][7]],
                [m1[5][0],m1[5][1],m1[5][2],m1[5][3],m1[5][4],m2[5][5],m2[5][6],m2[5][7]],
                [m1[6][0],m1[6][1],m1[6][2],m1[6][3],m1[6][4],m1[6][5],m2[6][6],m2[6][7]],
                [m1[7][0],m1[7][1],m1[7][2],m1[7][3],m1[7][4],m1[7][5],m1[7][6],m2[7][7]]]
        matriz=np.array(matriz)
    else: #si no se cruzan random para escoger matriz
        rand=random.randint(0, 1)
        if rand==1:
            matriz=m1
        else:
            matriz=m2
    return matriz

poblacion=[[i for i in range(3)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
for i in range(npoblacion): #crea la poblacion
    poblacion[i][0]=creamatriz()
    poblacion[i][1]=cuentanqueen(poblacion[i][0])
    
sumareinas=np.sum(poblacion,axis=0)[1] #suma el total de ataques de reinas
print(sumareinas)

for i in range(npoblacion): #calcula el porcentaje de ser padre
    poblacion[i][2]=1-(poblacion[i][1]/(sumareinas))

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

prueba=cruza(padres[0][0],padres[1][0])
print(prueba)
print(cuentanqueen(prueba))

#poner esto despues de muta y append de hijos y poblacion
poblacion.sort(key=lambda x:x[1]) #ordena la matriz de acuerdo a numero de ataques de menor a mayor
print(poblacion)