Matriz = [[0, 1, 0, 0],
          [1, 1, 0, 1],
          [0, 0, 0, 0],
          [1, 0, 1, 0]]


def cambioTraspuesto(filaC, columC, filaF, columF, matriz):

    if(filaF-filaC <= 2 and columF - columC <= 2):
        for fila in range(filaC, filaF):
            for columna in range(columC, columF):
                aux = matriz[fila][columna]
                matriz[fila][columna] = matriz[columna][fila]
                matriz[columna][fila] = aux
    else:
        filaM = (filaC + filaF) // 2
        columM = (columC + columF) // 2
        cambioTraspuesto(filaC, columC, filaM, columM)
        cambioTraspuesto(filaM, columC, filaF, columM)
        cambioTraspuesto(filaC, columM, filaM, columF)
        cambioTraspuesto(filaM, columM, filaF, columF)


def transponer(matriz, comienzo, final):
    if(comienzo - final <= 2):
        for fila in range(comienzo, final-1):
            for columna in range(comienzo+1, final):
                aux = matriz[fila][columna]
                matriz[fila][columna] = matriz[columna][fila]
                matriz[columna][fila] = aux
    else:
        medio = (comienzo + final) // 2
        transponer(matriz, comienzo, medio)
        transponer(matriz, medio, final)
        cambioTraspuesto(medio, comienzo, final, medio, matriz)


def mostrarMatriz(filaC, columC, filaF, columF, matriz):
    for fila in range(filaC, filaF):
        for columna in range(columC, columF):
            print(str(matriz[fila][columna]) + " ", end='')
        print("\n")


transponer(Matriz, 0, 4)
mostrarMatriz(0, 0, 4, 4, Matriz)
