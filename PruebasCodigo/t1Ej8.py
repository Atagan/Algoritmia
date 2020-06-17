def reverso(n):
    if(n//10==0):
        return n
    else:
        aux=n%10
        aux=10*aux
        aux+=reverso(n//10)
        return aux

 
