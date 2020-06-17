# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:47:45 2020

@author: laura
"""


# -*- coding: utf-8 -*-
"""
Created Jun 2020

@author: laura Pérez Medeiro
@subject: Algoritmia y complejidad
"""


import numpy as np

""" 
    Función que inicializa el tablero y la matriz de movimientos
"""



def leerData(fichero): #Guarda los datos en una lista
    fichero = open(fichero, "r")
    datos = []
    for line in fichero:
        inner_list = line.split('\t')
        datos.append(inner_list)
    fichero.close()
    for i in range(len(datos)):
         datos[i][len(datos[i])-1] = datos[i][len(datos[i])-1].strip('\n')
    return datos


def init(datos):
    # Se inicializa la matriz que representa el tablero a cero
   filas = datos [0][0]
   columnas = datos [1][0]
   
   datos.pop(0)
   datos.pop(0)
   mapa = datos
    
   return filas, columnas, mapa

"""
    Función que comprueba que dado un x y un y, son movimientos que
    se encuentran dentro del tablero
"""
def valido (x,y, mapa):
    filas = len(mapa)
    columnas = len(mapa[1])
    if (x>=0 and x<=filas and y>=0 and y<=columnas):
        if mapa[x][y] != 'X' and mapa[x][y] == 0:
            return True
        else:
            return False
    return False

""" 
    Función con la que el caballo recorre el tablero partiendo de
    un posicion (x,y) y un numero de movimientos
    
     
        8 -> arriba
        6 -> derecha
        4 -> izquierda
        2 -> abajo

"""
def camion (x,y, numMov, mapa, direccion, numDirDer):
    mapa[x][y] = numMov
    
    if mapa[x][y] == 2:
        return True, mapa, numDirDer

    else:
        if direccion == 8:
            nuevoX = x-1
            nuevoY = y
            nuevoX1 = x
            nuevoY1 = y+1
            nuevaDireccion = 8
            nuevoDireccion1 = 6
             
        elif direccion == 6:
            nuevoX = x
            nuevoY = y+1
            nuevoX1 = x-1
            nuevoY1 = y
            nuevaDireccion = 6
            nuevoDireccion1 = 2
             
        elif direccion == 4:
            nuevoX = x
            nuevoY = y-1
            nuevoX1 = x-1
            nuevoY1 = y
            nuevaDireccion = 4
            nuevoDireccion1 = 8
            
        elif direccion == 2:
            nuevoX = x+1
            nuevoY = y
            nuevoX1 = x
            nuevoY1 = y-1
            nuevaDireccion = 2
            nuevoDireccion1 = 4
            
        else:
            print("Pues la has cagao")
            
        if valido(nuevoX,nuevoY,mapa):
            if camion(nuevoX, nuevoY, numMov+1, mapa, nuevaDireccion, numDirDer):
                return True, mapa, numDirDer
            else:
                return False
            
        if valido(nuevoX1, nuevoY1, mapa):
             if camion(nuevoX, nuevoY, numMov+1, mapa, nuevoDireccion1, numDirDer+1):
                return True, mapa, numDirDer
             else:
                return False
            
        mapa[x][y] = 0
        return False
    
def encontrar(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[1])):
            if mapa[i][j]=='1':
                return i,j
            
def main():
     d = leerData("test.txt")
     # print(d)
     filas, columnas, mapa = init(d)
     print(mapa)
     x,y = encontrar(mapa)
     print(x,y)
     
     print(camion(x,y,0,mapa,6,0))
     
    
main()
