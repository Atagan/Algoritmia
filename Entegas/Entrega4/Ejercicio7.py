import numpy as np

first  = [0,1,1,0,1,0,1]
second = [1,0,1,0,0,1,0,0,1]    
findSubSeq(first, second)

def findSubSeq(frstSeq, sndSeq):
    a = len(frstSeq)
    b = len(sndSeq)
    seqAux = np.zeros((a,b))
    
    for i in range(a):
        for j in range(b):
            if frstSeq[i] == sndSeq[j]:
                if i == 0 or j == 0:
                    seqAux[i][j] = 1
                else:
                    seqAux[i][j] =  seqAux[i - 1][j - 1] + 1
            else:
                if i == 0 and j == 0:
                    seqAux[i][j] = 0
                elif i == 0 and j != 0:
                    seqAux[i][j] = seqAux[i][j-1]
                elif j == 0 and i != 0:
                    seqAux[i][j] = seqAux[i-1][j]
                else:
                    if seqAux[i - 1][j] > seqAux[i][j-1]:
                        seqAux[i][j] = seqAux[i - 1][j]
                    elif seqAux[i -1][j] < seqAux[i][j-1]:
                        seqAux[i][j] = seqAux[i][j - 1]
                    else:
                        seqAux[i][j] = seqAux[i - 1][j]   

    print("La longitud de la subsecuencia es: ", seqAux[len(frstSeq)-1][len(sndSeq)-1])
    
    i= 1
    j = 1
    l = 0
    cadena = []
    while (l < seqAux[a-1][b-1]):
        if (seqAux[a-1][b-1] == seqAux[a-2][b-2]+1): 
            l +=1
            cadena.append(frstSeq[i])
        if (i<a):
            i +=1
        if (i<b):
            j+=1
    print(cadena)
