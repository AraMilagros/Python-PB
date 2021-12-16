#Implementar funcion contar_tuplas que reciba una tupla
# con tuplas en su interior, y devuelva una tupla con la
# cantidad de tuplas que habia y la cantidad total de elementos (entre las tuplas)

def contar_tuplas(tuplas):
    tMadre=0
    tHijos=len(tuplas)

    for indice in tuplas:
        tMadre+=len(indice)
    return tMadre, tHijos

#Tuplas
hijo1= (1,2,3)
hijo2=('verde','rojo','naranja')
hijo3=('faku', 'lorenzo')

tuplaMadre=((hijo1),(hijo2),(hijo3))

madre, hijos = contar_tuplas(tuplaMadre)
print('TuplaMadre: ',tuplaMadre)
print('Cantidad de elementos en la tupla: ', madre)
print('Cantidad de tuplas, en tuplaMadre: ', hijos)