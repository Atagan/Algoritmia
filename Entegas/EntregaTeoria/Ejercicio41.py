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
def camion (x,y, numMov, mapa, direccion, numDirDer,listaMovimientos):
    movimientos=[[0,0,0],[0,0,0]]
    if mapa[x][y] == '2':
        mostrarMatriz(0,0,4,4, mapa)
        print("Ruta conseguida en ",numMov,"movimientos con ",numDirDer," giros a la derecha.")
        print("Coordenadas de la ruta seguida:")
        mostrarMatriz(0,0,len(listaMovimientos),2,listaMovimientos)
        
        f = open("Output.txt","w+")
        stringA=""
        for i in mapa :
            stringA += str(i)+"\n"
        f.write(stringA)
        stringA="Ruta conseguida en "+str(numMov)+"movimientos con "+str(numDirDer)+" giros a la derecha.\n"
        f.write(stringA)
        f.write("Coordenadas de la ruta seguida:\n")
        stringA=""
        for i in listaMovimientos:
            stringA+=str(i)+"\n"
        f.write(stringA)
        
        return True

    else:
        if direccion == 8:
            movimientos[0][0] = x-1
            movimientos[0][1] = y
            movimientos[1][0] = x
            movimientos[1][1] = y+1
            movimientos[0][2] = 8
            movimientos[1][2] = 6
             
        elif direccion == 6:
            movimientos[0][0] = x   #NuevaX
            movimientos[0][1] = y+1 #NuevaY
            movimientos[1][0] = x+1 #NuevaX1
            movimientos[1][1] = y   #NuevaY1
            movimientos[0][2] = 6   #NuevaDirección
            movimientos[1][2] = 2   #NuevaDirección1
             
        elif direccion == 4:
            movimientos[0][0] = x
            movimientos[0][1] = y-1
            movimientos[1][0] = x-1
            movimientos[1][1] = y
            movimientos[0][2] = 4
            movimientos[1][2] = 8
            
        elif direccion == 2:
            movimientos[0][0] = x+1
            movimientos[0][1] = y
            movimientos[1][0] = x
            movimientos[1][1] = y-1
            movimientos[0][2] = 2
            movimientos[1][2] = 4
            
        else:
            print("Pues la has cagao")

        for i in range(len(movimientos)):
            if(valido(movimientos[i][0],movimientos[i][1],mapa)):
                listaMovimientos.append(movimientos[i])
                if(i==1):
                    if(camion(movimientos[i][0],movimientos[i][1],numMov+1,mapa,movimientos[i][2],numDirDer+1,listaMovimientos)):
                       return True
                else:
                    if(camion(movimientos[i][0],movimientos[i][1],numMov+1,mapa,movimientos[i][2],numDirDer,listaMovimientos)):
                       return True 
                listaMovimientos.pop()
        print("El tablero no tiene solucion")
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
     d = leerData("Ejemplo_1.txt")
     # print(d)
     filas, columnas, mapa = init(d)

     x,y = encontrar(mapa)

     #isrutita,rutita, numrutita=camion(x,y,1,mapa,4,0)
     camion(x,y,1,mapa,4,0,[])
    
main()
