Tapones=[1,3,4,2]
Botellas=[3,2,4,1]

def Entaponar(tapones, botellas, inicio):
    if inicio < len(tapones) and inicio < len(botellas):
        if(tapones[inicio] != botellas[inicio]):
            for i in range(inicio + 1, len(botellas)):
                if (tapones[inicio] == botellas[i]):
                    baux=botellas[inicio]
                    botellas[inicio] = botellas[i]
                    botellas[i]=baux
                    break
        inicio=inicio+1
        Entaponar(tapones, botellas,inicio)
    return tapones, botellas

print(Entaponar(Tapones, Botellas, 0))
