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
    if(x>=0 and x<(len(mapa)-1) and y>=0 and y<(len(mapa[y])-1)):
        if(not mapa[x][y]=='X'):
            return True
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
    mostrarMatriz(0,0,4,4,mapa)
    if mapa[x][y] == 'Z':
        print("True")
        mostrarMatriz(0,0,4,4, mapa)
        return True, mapa, numDirDer

    else:
        mapa[x][y] = numMov
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
            nuevoX1 = x+1
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
            
        if(valido(nuevoX,nuevoY, mapa)):
            if(mapa[nuevoX][nuevoY]=='0'):
                if(camion(nuevoX, nuevoY, numMov+1,mapa,nuevaDireccion, numDirDer)):
                    mostrarMatriz(0,0,4,4,mapa)
                    return True, mapa, numDirDer
        if(valido(nuevoX1,nuevoY1,mapa)):
            if(mapa[nuevoX1][nuevoY1]=='0'):
                if(camion(nuevoX1,nuevoY1,numMov+1,mapa,nuevoDireccion1,numDirDer+1)):
                   mostrarMatriz(0,0,4,4,mapa)
                   return True, mapa, numDirDer
        mostrarMatriz(0,0,4,4,mapa)
        mapa[x][y]='0'
        return False
            
            
        
def encontrar(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[1])):
            if mapa[i][j]=='1':
                return i,j

def mostrarMatriz(filaC, columC, filaF, columF, matriz):
    for fila in range(filaC, filaF):
        for columna in range(columC, columF):
            print(str(matriz[fila][columna]) + " ", end='')
        print("\n")
    print("\n")



def main():
     d = leerData("test.txt")
     # print(d)
     filas, columnas, mapa = init(d)

     x,y = encontrar(mapa)

     
     #isrutita,rutita, numrutita=camion(x,y,1,mapa,4,0)
     camion(x,y,1,mapa,4,0)
     print(mapa)
    
main()
