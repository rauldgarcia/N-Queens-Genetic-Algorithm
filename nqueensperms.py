import numpy as np
from random import *
import random
import time
inicio=time.time()

nqueen=8 
npoblacion=100 
npadres=5 
npadresreal=2
pcruza=1 #se puede cambiar porcentaje de cruza
pmuta=0.8 #se puede cambiar
iteraciones=10000

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
    if n<p:
        return 1
    else:
        return 0

def selpadres():
    spadres=[[k for k in range(2)]for l in range(npadres)] #crea una matriz de largo de los padres
    for i in range(npadres): #seleccion de padres
        numrandom=randint(0,npoblacion-1)
        spadres[i][0]=poblacion[numrandom][0] 
        spadres[i][1]=poblacion[numrandom][1]

    spadres.sort(key=lambda x:x[1]) #ordena la matriz de acuerdo a numero de ataques de menor a mayor
    del spadres[npadresreal:] #borra los peores y se queda con tamaño de poblacion igual
    return spadres

def cruza(padres):
    shijos=[[k for k in range(2)]for l in range(2)] #crea una matriz de largo de los hijos
    corte=randint(1,nqueen-2)

    p1=padres[0][0]
    p2=padres[1][0]
    h1=p1[0:corte]
    h2=p2[0:corte]

    for i in p2[corte:]:
        if i not in h1:
            h1=np.append(h1,i)
        else:
            h1=np.append(h1,8)

    for i in p1[corte:]:
        if i not in h2:
            h2=np.append(h2,i)
        else:
            h2=np.append(h2,8)

    #reparación
    aleat=np.random.permutation(8)
    aleat1=np.random.permutation(8)
    for i in aleat:
        if i not in h1:
            list1=h1.tolist()
            indice=list1.index(8)
            h1[indice]=i
    for i in aleat1:
        if i not in h2:
            list2=h2.tolist()
            indice=list2.index(8)
            h2[indice]=i

    shijos[0][0]=h1
    shijos[1][0]=h2
    return shijos

def muta(x):
    p=flip(pmuta) #volado si se muta o no
    if p==1:
        h1=x[0][0]
        h2=x[1][0]
        aleat1=randint(0,nqueen-1)
        aleat2=randint(0,nqueen-1)
        aleat3=randint(0,nqueen-1)
        aleat4=randint(0,nqueen-1)
        c1=h1[aleat1]
        c2=h1[aleat2]
        c3=h2[aleat3]
        c4=h2[aleat4]
        h1[aleat1]=c2
        h1[aleat2]=c1
        h2[aleat3]=c4
        h2[aleat4]=c3
        x[0][0]=h1
        x[1][0]=h2
    return x

poblacion=[[i for i in range(2)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
evaluaciones=0

for i in range(npoblacion): #crea la poblacion
    poblacion[i][0]=creaperm()
    poblacion[i][1]=cuentanqueen(poblacion[i][0])
    evaluaciones+=1

mejor=poblacion[0][0]
mejorscore=poblacion[0][1]
print("El número de evaluciones es:")
print(evaluaciones)
print("El mejor tablero es:")
print(pmatriz(mejor))
print("Tiene el siguiente numero de ataques:")
print(mejorscore)

vectorevaluaciones=np.array([[evaluaciones,mejorscore]])

while mejorscore>0 and evaluaciones<10000:
    padres=selpadres() #se seleccionan padres
    hijos=cruza(padres) #se obtienen hijos
    hijos=muta(hijos) #se mutan hijos

    for i in range(npadresreal): #se evaluan hijos
        hijos[i][1]=cuentanqueen(hijos[i][0])
        evaluaciones+=1

    poblacion.extend(hijos) #pega los hijos a la poblacion
    poblacion.sort(key=lambda x:x[1]) #ordena la matriz de acuerdo a numero de ataques de menor a mayor
    del poblacion[npoblacion:] #borra los peores y se queda con tamaño de poblacion igual

    mejor=poblacion[0][0]
    mejorscore=poblacion[0][1]
    print("El número de evaluciones es:")
    print(evaluaciones)
    print("El mejor tablero es:")
    print(pmatriz(mejor))
    print("Tiene el siguiente numero de ataques:")
    print(mejorscore)
    vectorevaluacionesac=np.array([[evaluaciones,mejorscore]])
    vectorevaluaciones=np.append(vectorevaluaciones,vectorevaluacionesac,axis=0)

fin=time.time()
print("El tiempo de ejecución fue:")
print(fin-inicio)
np.savetxt("nqueensperms30.csv",vectorevaluaciones,delimiter=",")