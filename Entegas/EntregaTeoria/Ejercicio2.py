def mediaP2(listaN): #Unicamente funciona con potencias de dos
    if(len(listaN) == 2):
        a = (listaN[0] + listaN[1])/2
        return a
    else:
        listaA, listaB = split_list(listaN)
        a = (mediaP2(listaA) + mediaP2(listaB))/2
        return a

def mediaNoP2(listaN,n): 
    
    if(len(listaN) == 1):
        a = listaN[0]/n
        return a
    else:
        listaA, listaB = split_list(listaN)
        a = mediaNoP2(listaA,n) + mediaNoP2(listaB,n)
        return a

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def leerData(fichero): #Guarda los datos en una lista
    for line in fichero:
        inner_list = [int(elt.strip()) for elt in line.split(',')]
    return inner_list

def guardarData(lista):
    f = open("Data.txt","w+")
    stringA = "La media es: " + str(mediaNoP2(lista,len(lista))) + "\n"
    f.write(stringA)
       
guardarData(leerData(open("Notas.txt","r")))

