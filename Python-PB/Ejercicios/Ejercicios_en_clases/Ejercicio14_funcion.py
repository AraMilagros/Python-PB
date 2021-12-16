#utilizar filter, map, lambdas...
#recibe lista de numeros y retorna otra con numeros pares
#de la original elevados al cuadrado

#Funcion comprar, recibe lista de precios y un saldo total..
#calcular vuelto.
#En caso de saldo insuficiente lanzar una excepcion "saldoinsuficiente"
#incluir en el msj el saldo y total de la compras
lista=[1,2,3,4,5,6,7,8,9,10]
def espar(numero):
    return ((numero%2) == 0)
resultado1 = filter(espar, lista)
cuadrado = lambda n: n * n
#print (list(resultado1))
resultado = map(cuadrado, resultado1)
#print(list(resultado))

def compra(precios, saldo):
    try:
        g=calcular_gasto(precios)
        g>saldo
    except:
        print('Saldo insuficiente')

def calcular_gasto(precios):
    gasto=0
    for precio in precios:
        gasto+=precio
    return gasto