
##sumar_matrices, recibe 2 matrices de igual tamaño
##representadas como lista de listas. Retornar 1 matriz con la suma de sus elem

def sumar_matrices(matriz1, matriz2):
    suma = []
    fila1 = []

    for i in range(len(matriz1)):#recorre filas
        for j in range(len(matriz2[i])):#recorre cada elemento en la fila
            fila1.append(matriz1[i][j] + matriz2[i][j])
        suma.append(fila1)
        fila1=[]

    return suma

matriz1=[[1,2,3],[3,4,5]]
matriz2=[[2,2,2],[1,1,1]]
print('matriz 1: ', matriz1)
print('matriz 2: ', matriz2)
print(sumar_matrices(matriz1, matriz2))