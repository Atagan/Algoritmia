vec = [1,5,2,4,6,6,66,22,4,12,45,5,234,53,234,13,563,10]

def max_min_vector(vev):
    comienzo = 0
    final = len(vec) - 1
    mitad = comienzo + (int)((final-comienzo+1)/2)+1
    for i in range(comienzo, mitad):
        if(vec[i] > vec[final-i+comienzo]):
            aux = vec[i]
            vec[i] = vec[final-i+comienzo]
            vec[final - i + comienzo] = aux

    minimo = vec[comienzo]
    for i in range(comienzo+1,mitad):
        if(vec[i] < minimo):
            minimo = vec[i]

    maximo = vec[final]
    for i in range(mitad, final-1):
        if(vec[i] > maximo):
            maximo = vec[i]

    return minimo,maximo

a,b=max_min_vector(vec)

print("El maximo es: ",b,", y el minimo es: ",a)
