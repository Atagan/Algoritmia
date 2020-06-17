def crearGrupos(matriz, listaP):
    #print(len(listaP))
    if(len(listaP)==0):
        return matriz
    else:
        contactos = listaP[0]
        listaP.pop(0)
        encontrado=False
        if(len(matriz[0])==0):
            matriz[0]=meter(matriz[0],contactos)
        else:
            for i in range(len(matriz)):
                for j in range(len(contactos)):
                    if(contactos[j] in matriz[i]):
                        matriz[i]=meter(matriz[i],contactos)
                        encontrado=True
            if(not encontrado):
                matriz.append([])
                matriz[len(matriz)-1]=meter(matriz[len(matriz)-1],contactos)
        matrizS=crearGrupos(matriz, listaP)
        return matrizS

def meter(matriz, lista):
    for i in lista:
        if(not i in matriz):
            matriz.append(i)
    return matriz

def leerData(fichero):
    lista=[]
    for line in fichero:
        inner_list = [elt.strip() for elt in line.split(',')]
        lista.append(inner_list)
    return lista

def guardarData(matriz, n):
    f= open("Data.txt","w+")

    stringAux="Numero de grupos: " + str(len(matriz)) + ".\n\n"
    f.write(stringAux)

    stringAux= "Grado de conexión: "+ str(len(matriz)/n)+".\n\n"
    f.write(stringAux)

    stringAux= "GRUPOS:           PERTENECIENTES: \n\n"
    f.write(stringAux)
    
    for i in range(len(matriz)):
        stringAux="Grupo "+str(i+1)+":          "

        for j in matriz[i]:
            stringAux= stringAux + j + " "
        stringAux+="\n"
        f.write(stringAux)

matriz=[[]]
fichero = open("ejemplo_voraz.txt","r")
listaP=leerData(fichero)
n=len(listaP)
matrizData=crearGrupos(matriz,listaP)
guardarData(matrizData,n)
