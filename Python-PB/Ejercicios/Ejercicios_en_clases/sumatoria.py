def sumatoria(numero):
    suma = 0
    for i in range(numero+1):
        suma+=i
    return suma

num = int(input('Ingrese un numero: '))

print(sumatoria(num))
