
MATRIZ=[['',"a","b","c","d"],
["a","b","b","a","d"],
["b","c","a","d","a"],
["c","b","a","c","c"],
["d","d","c","d","b"]]
    
def sustitucion(cadena, matriz, objetivo, pasosC):
    print(pasosC)
    #print(cadena)
    if(cadena == objetivo):  #cadena(Str) == objetivo(Str)
        pasosC.append(cadena)
        print(pasosC)
        return True, pasosC
        
    elif(len(cadena)!= 1):
        for i in range(1,len(matriz)): #filas
            for j in range(1,len(matriz[1])):  #columnas
                stringAux=""+str(matriz[i][0]+matriz[0][j])
                if(stringAux in cadena):
                    cadenaAux=cadena.replace(stringAux, ""+str(matriz[i][j]),1)
                   #print(stringAux in cadena)
                    pasosC.append(cadena)
                    if(sustitucion(cadenaAux, matriz, objetivo, pasosC)):
                        return True,pasosC
                    else:
                        pasosC.pop()
                        
    else:
      return False

pasosC = []  
#print(MATRIZ)
sustitucion("acabada", MATRIZ, "d", pasosC)
