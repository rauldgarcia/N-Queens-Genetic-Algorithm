import numpy as np
from random import *
import random
import time
import copy
inicio=time.time()

nqueen=8 #se puede cambiar el numero de reinas (solo hay solución para n>=4)
npoblacion=100 #se puede cambiar el numero de poblacion
npadres=20 #se puede cambiar el numero de padres
pcruza=0.8 #se puede cambiar porcentaje de cruza
pmuta=0.8 #se puede cambiar
iteraciones=10000

def creamatriz (): #crea matrices aleatorias de n numeros de 1 
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

    for i in range(-nqueen+1,nqueen,1): #suma diagonales
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
    if n<p:
        return 1
    else:
        return 0

def selpadres():
    spadres=[[k for k in range(3)]for l in range(npadres)] #crea una matriz de largo de los padres
    cont=0
    while cont<npadres: #seleccion de padres
        for i in range(npoblacion):
            if cont<npadres:
                if flip(poblacionn[i][2])==1:
                    spadres[cont][0]=poblacionn[i][0]
                    cont+=1
            else:
                break
       
    return spadres

def cruza(padres):

    hijos=[[i for i in range(3)]for j in range(10)] #crea a los hijos
    conta=0
    for i in range(0,npadres,2):
        m1=padres[i][0]
        m2=padres[i+1][0]

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
            suma=np.sum(matriz, axis=0) #suma columna
            total=np.sum(suma) #suma total

            while total>nqueen: #repara si hay mas reinas
                randomx=randint(0,nqueen-1)
                randomy=randint(0,nqueen-1)
                if matriz[randomx][randomy]==1:
                    matriz[randomx][randomy]=0
                    total-=1
            
            while total<nqueen: #repara si hay menos reinas
                randomx=randint(0,nqueen-1)
                randomy=randint(0,nqueen-1)
                if matriz[randomx][randomy]==0:
                    matriz[randomx][randomy]=1
                    total+=1        
            
        else: #si no se cruzan random para escoger matriz
            rand=random.randint(0, 1)
            if rand==1:
                matriz=m1
            else:
                matriz=m2
        hijos[conta][0]=matriz
        conta+=1
        
    return hijos

def mutacion(hijosm):
    hijosmutados=[[i for i in range(3)]for j in range(10)] #crea a los hijos
    for i in range(len(hijosm)):
        matrizmut=hijosm[i][0]
        p=flip(pmuta) #volado si se muta o no
        if p==1:
            unos=np.where(matrizmut==1) #ubicacion 1
            aleat=randint(0,nqueen-1)
            ceros=np.where(matrizmut==0) #ubicacion 0
            aleat0=randint(0,55)
            matrizmut[unos[0][aleat]][unos[1][aleat]]=0
            matrizmut[ceros[0][aleat0]][ceros[1][aleat0]]=1
            hijosmutados[i][0]=matrizmut
        else:
            hijosmutados[i][0]=hijosm[i][0]

    return hijosmutados

evaluacion=0
poblacion=[[i for i in range(3)]for j in range(npoblacion)] #crea matriz de largo de la poblacion
for i in range(npoblacion): #crea la poblacion
    poblacion[i][0]=creamatriz()
    poblacion[i][1]=cuentanqueen(poblacion[i][0])
    evaluacion+=1

poblacion.sort(key=lambda x:x[1]) #ordena la matriz de acuerdo a numero de ataques de menor a mayor
mejor=poblacion[0][0]
mejorscore=poblacion[0][1]
print("El mejor tablero es:")
print(mejor)
print("Tiene el siguiente numero de ataques:")
print(mejorscore)

while mejorscore>0 and evaluacion<iteraciones:
    
    sumareinas=0
    for i in range(npoblacion):
        sumareinas+=poblacion[i][1]
    
    promata=sumareinas/npoblacion
    poblacionn=poblacion
    for j in range(npoblacion): #calcula el porcentaje de ser padre
        poblacionn[j][2]=1-(poblacionn[j][1]/(promata+0.1)) #al casi converger a 0 toda la poblacion tiene ataques==promedio
    
    
    padres=selpadres() #selecciona a los padres
    
    hijos=cruza(padres)#se cruzan padres

    prueba=copy.deepcopy(poblacion)
    
    hijosmu=mutacion(hijos)#se mutan hijos

    for x in range(10):
        hijosmu[x][1]=cuentanqueen(hijosmu[x][0]) #se evaluan
        evaluacion+=1
    
    hijosmu.sort(key=lambda x:x[1]) #ordena la lista de acuerdo a numero de ataques de menor a mayor
    poblacion=prueba   
    poblacion.extend(hijosmu) #pega los hijos a la poblacion
    
    #print(poblacion)
    poblacion.sort(key=lambda x:x[1]) #ordena la lista de acuerdo a numero de ataques de menor a mayor
    del poblacion[npoblacion:] #borra los peores y se queda con tamaño de poblacion igual
    #print(poblacion)

    if poblacion[0][1]<mejorscore:
        mejor=copy.deepcopy(poblacion[0][0])
        mejorscore=copy.deepcopy(poblacion[0][1])

    print("Iteración número:")
    print(evaluacion)
    print("El mejor tablero es:")
    print(mejor)
    print("Tiene el siguiente numero de ataques:")
    print(mejorscore)

fin=time.time()
print("El tiempo de ejecución fue:")
print(fin-inicio)
print(cuentanqueen(mejor))