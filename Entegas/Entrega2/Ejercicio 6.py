escaleras = [3,30,4,5,14,16,21,13,24,6]
salida = [0,0,0,0,0,0,0,0,0,0]          
def EscalerasDeShrek(arrayE, arrayS):
    arrayE.sort()
    eVal1 = 0
    sVal21 = 0
    guar22 = 0
    iterar = 1
    coste = 0
    while(iterar == 1):
        if(sVal21 == guar22 - 1 and eVal1 == len(arrayE) - 1): 
            operacion = 3
            iterar = 0
        elif(sVal21 < guar22-1 and eVal1 == len(arrayE) -1 ): 
            if(arrayS[sVal21+1] < arrayE[eVal1]):
                operacion = 1
            else:
                operacion = 3
        elif(sVal21 == guar22 - 1 and eVal1 < len(arrayE) - 1): 
           if(arrayE[eVal1 + 1] < arrayS[sVal21]):
               operacion = 2
           else:
               operacion = 3
        elif (sVal21 < guar22 - 1 and eVal1 < len(arrayE) - 1): 
            if(arrayS[sVal21+1] < arrayE[eVal1]):
                operacion = 1
            elif(arrayE[eVal1 + 1] < arrayS[sVal21]):
                operacion = 2
            else:
                operacion = 3
        elif(sVal21 < guar22 - 1):
            operacion = 1
        elif(eVal1 < len(arrayE) - 1): 
            operacion = 2
        else: 
            operacion = 0
            iterar = 0
        if(operacion > 0):
            if(operacion == 1):
                arrayS[guar22] = arrayS[sVal21] + arrayS[sVal21 + 1]
                guar22 = guar22 + 1
                sVal21 = sVal21 + 2
            elif(operacion == 2):
                arrayS[guar22] = arrayE[eVal1] + arrayE[eVal1 + 1]
                guar22 = guar22 + 1
                eVal1 = eVal1 + 2
            else:
                arrayS[guar22] = arrayE[eVal1] + arrayS[sVal21]
                guar22 = guar22 + 1
                eVal1 = eVal1 + 1
                sVal21 = sVal21 + 1
    for i in range(len(arrayS)): 
        coste += arrayS[i]
    return coste

print(EscalerasDeShrek(escaleras, salida))
