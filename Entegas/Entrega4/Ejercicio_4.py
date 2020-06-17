def alforjaAlgoritmo(capacidad, peso, valores, n):
    matrizTesoros = [[0 for x in range(capacidad + 1)] for x in range(n + 1)]   
    for i in range(n + 1):
        for j in range(capacidad + 1):
            if i == 0 or j == 0:
                matrizTesoros[i][j] = 0
            elif peso[i-1] <= j:
                matrizTesoros[i][j] = max(valores[i-1]+ matrizTesoros[i-1][j-peso[i-1]],  matrizTesoros[i-1][j])
            else:
                matrizTesoros[i][j] = matrizTesoros[i-1][j]

    return matrizTesoros[n][capacidad]

valores = [5,10,15,20,25,30,35,40]
peso = [1,5,7,10,3,11,20,50]
capacidad = 50
n = len(valores)
print("El maximo beneficio es:",alforjaAlgoritmo(capacidad, peso, valores, n))
