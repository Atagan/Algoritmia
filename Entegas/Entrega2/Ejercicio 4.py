grafo = [[4, 2, 3, 6, 8],[2, 1, 3, 2, 35],[3, 3, 8, 3, 7], [6, 2, 3, 2, 9],[8, 35, 7, 9, 0]]
vertices = 5
def minA(valoresAristas, incluidos):
    indiceAristaMin = -1
    min = 100000000000000000000 
    for i in range(vertices):
        if(incluidos[i] == False and valoresAristas[i] < min):
            min=valoresAristas[i]
            indiceAristaMin = i
    return indiceAristaMin

def mostrarCost(arbol, grafo):  
    print("Arista    Peso")
    for i in range(1,vertices):
        print(arbol[i] , " - " , i ,"  ", grafo[i][arbol[i]])

def algoritmoPrim(grafo):

    arbolResultado = [None] * vertices
    valoresAristas = [100000000000000000000] * vertices
    incluidos = [False] * vertices

    valoresAristas[0] = 0 
    arbolResultado [0] = -1 

    for i in range(vertices):
        arista = minA(valoresAristas,incluidos)
        incluidos[arista] = True
        for j in range(vertices):
            if (grafo[arista][j] != 0 and incluidos[j] == False and grafo[arista][j] < valoresAristas[j]):
                arbolResultado[j] = arista
                valoresAristas[j] = grafo[arista][j]

    mostrarCost(arbolResultado, grafo)


algoritmoPrim(grafo)
