import numpy as np
def init(filas, columnas):
    tablero = np.zeros((filas, columnas))
    movimiento = np.zeros((2, 8))
    
    fila1= [1,2,2,1,-1,-2,-2,-1]
    fila2= [2,1,-1,-2,-2,-1,1,2]
    
    movimiento[0,:] = fila1
    movimiento[1,:] = fila2
    
    return(tablero, movimiento)

def valido (x,y):
    # return (x>0 and x<=filas and y>0 and y<=columnas)
    return (x>=0 and y>=0 and x<filas and y<columnas)

def caballo (x,y, numMov, tablero, movimiento):
    tablero[x][y] = numMov
    # print(tablero)
    if numMov == len(tablero) * len(tablero[1]):
        print(tablero)
        return True
        
    for i in range (1,7):
        nuevoX = int (x + movimiento[0][i] )
        nuevoY = int (y + movimiento[1][i] )
        
        #type(nuevoX)
        #print(nuevoX, nuevoY)
        
        if valido(nuevoX,nuevoY):
            #print("******")
            if tablero[nuevoX][nuevoY] == 0:
                if caballo(nuevoX, nuevoY, numMov+1, tablero, movimiento):
                    return True
    tablero[x][y]=0
    return False
       
filas=8
columnas = 8
tablero, movimiento = init(filas,columnas)
caballo(0,0,1, tablero, movimiento)
