
def hayCambio(valores, cantidad, precio):
    mAux = [[None] * precio] * len(valores)
    cambioT = [None] * 20
    for i in range(0, len(valores)):
        mAux[i][0] = 0
    for i in range(1, precio):
        mAux[0][i] = 100000000000000000
        print (mAux)
    for i in range(1, len(valores)):
        for j in range(1, precio):
            minimo = mAux[i-1][j]
            if(valores[i] <= j):
                if(valores[i]*cantidad[i] >= j):
                    minimo = min(minimo, mAux[i-1][j-valores[i]] +
                                 1, mAux[i][j-valores[i]]+1)
                else:
                    minimo = min(minimo, mAux[i-1][j-cantidad[i]] *
                                 valores[i]+cantidad[i])
            mAux[i][j] = minimo
    for i in range(1, len(valores)):
        cambioT[1] = 0
    if(mAux[len(valores)][precio] < 100000000000000000):
        i = len(valores)
        j = precio
        while(i > 0 and j > 0):
            if(mAux[i][j] == mAux[i-1][j]):
                i = i-1
            else:
                cambioT[i] = cambioT[i]+1
                j = j-valores[1]
        return True, cambioT
    else:
        return False


V = [1, 3, 5]
C = [3, 5, 2]

print(hayCambio(V, C, 10))
