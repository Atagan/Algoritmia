# -*- coding: utf-8 -*-
"""
Created on june 2020

@author: laura Pérez Medeiro
@subject: Algoritmia y Complejidad
"""


import numpy as np

def findSubSeq(frstSeq, sndSeq):
    a = len(frstSeq)
    b = len(sndSeq)
    seqAux = np.zeros((a,b))
    
    matriz = calcularMatriz(a,b,seqAux)
    
    # La longitud será el valor que tome la matriz en la posición de la 
    # última fila y la última columna
    print("Longitud de la secuencia más larga es: ", int(matriz[a-1][b-1]))
    
    print("La matriz es: \n", matriz)
    
    seq = obtenerSeq (a,b, matriz)
    
    # Para obtener la secuencia, se realiza una especie de backtracking 
    # dentro de la matriz
    print("La secuencia más larga es: ", seq)
    

""" Funcion que retorna la matriz"""
    
def calcularMatriz(a, b, seqAux):
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
                    seqAux[i][j] = seqAux[i][j - 1]
                elif j == 0 and i != 0:
                    seqAux[i][j] = seqAux[i-1][j]
                else:
                    if seqAux[i - 1][j] > seqAux[i][j - 1]:
                        seqAux[i][j] = seqAux[i - 1][j]
                    elif seqAux[i -1][j] < seqAux[i][j - 1]:
                        seqAux[i][j] = seqAux[i][j - 1]
                    else:
                        seqAux[i][j] = seqAux[i - 1][j]   
    return seqAux

""" Funcion que retorna la secuencia de longitud máxima"""

def obtenerSeq(a,b,seq):
    countI= 1
    countJ = 1
  
    res = []
    for i in range (0, int(seq[a - 1][b - 1])):
        if (seq[a - 1][b - 1] == seq[a - 2][b - 2]+1): 
            res.append(frstSeq[i])
        if (i < a):
            countI +=1
        if (i < b):
            countJ+=1
    return res
             
frstSeq  = [0,1,1,0,1,0,1]
sndSeq   = [1,0,1,0,0,1,0,0,1]    
findSubSeq(frstSeq, sndSeq)
    
