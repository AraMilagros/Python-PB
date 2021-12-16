#Funcion buscar que reciba lista de entero y un entero
#devuelve la posicion de n en la lista o None sino lo encuentra

def buscar(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            return i

lista=[1,12,4,241,2]
n=2

print(lista)
print('Posición de ', n ,' en la lista: ', buscar(lista,n))