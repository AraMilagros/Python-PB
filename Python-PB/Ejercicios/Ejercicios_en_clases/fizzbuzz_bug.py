# 1: las comparaciones del if, siempre daria False
    #ya que se comparaba un int con un string -> '0'
# 2: por más que se ingrese un multiplo de 3 Y 5, nunca regresara FizzBuzz
    #ya que el ultimo if deberia ser el primero (engloba todas las condiciones)
    #despues de verificar que no cumple las 2 condiciones juntas, se sigue por descarte
def obtener_fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    if n % 3 == 0:
        return 'Fizz'
    if n % 5 == 0:
        return 'Buzz'
    return n

#Añadi un print para que muestre la salida por pantalla
    #de otro modo, sólo veriamos cómo ingresamos un valor y nada más
def fizzbuzz(n):
    for i in range(n+1):
        print(obtener_fizzbuzz(i))

#En esta parte, el nombre del método estaba mal -> fizzbuz(n)
    #es por eso que marcaba error
def main():
    n = int(input("Ingrese un entero: "))
    fizzbuzz(n)

main()
