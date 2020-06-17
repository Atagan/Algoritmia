
def max_min_vector(vector):
    longitud = len(vector)
    par = [vector[0], vector[1]]
    long_par = longitud % 2 == 0

    if long_par:
        minimo, maximo = min(par), max(par)
        idx = 2
    else:
        minimo = maximo = vector[0]
        idx = 1

    while idx < longitud - 1:
        new_min = vector[idx] < vector[idx + 1]

        if new_min:
            maximo = max(maximo, vector[idx + 1])
            minimo = min(minimo, vector[idx])
        else:
            maximo = max(maximo, vector[idx])
            minimo = min(minimo, vector[idx + 1])

        idx += 2

    return 'El numero min es: ', minimo, 'y el numero max es: ', maximo

V=[12,6,3,10,9,5,4,11,1,2,13,16,7,15,8,14]

print(max_min_vector(V))