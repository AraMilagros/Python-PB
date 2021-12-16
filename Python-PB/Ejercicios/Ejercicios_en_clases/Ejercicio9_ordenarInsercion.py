
def insercion(lista):
    for i in range(1, len(lista)):
        #print(lista)
        minimo = lista[i]
        j = i-1
        while j>=0 and lista[j]>minimo:
            lista[j+1] = lista[j]
            lista[j] = minimo
            #print(lista)
            j = j-1
        #lista[j+1] = minimo
    return lista

lista=[2, 5, 4, 3, 1, 9, 7]

print(insercion(lista))