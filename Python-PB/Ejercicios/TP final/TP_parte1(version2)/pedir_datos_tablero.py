import re
LIM_CARACTER=30
LIM_TABLERO=15

def validar_numero(num):
    #num: valor ingresado del usuario
    #1ro: se comprueba que se haya ingresado algo
    #   en caso de no, False

    #2do: si se ingreso algo, se comprueba que no hayan letras
    #   si no hay letras, se comprueba que sea mayor o igual a 15
    if len(num)<=0:
        return False
    if re.match("\d+$", num):
        return int(num)>=LIM_TABLERO
    return False

def validar_palabra(palabra, lim=0):
    #palabra: ingreso del usuario
    #lim: marca el limite de caracteres que debe tener una palabra

    #1ro: se verifica que el usuario realmente haya ingresado algo
    #   en caso de haber recibido una entrada vacía, se retorna False

    #2do: si se ingresó algo, se verifica que no hayan numeros
    #   en caso de haberlos, False

    #Ahora, sino se encuentran numeros en lo que se haya ingresado
    #   si lim no es 0, se comprobara que no se sobrepase
    #   en caso de que lim = 0, se usa una constante como otro limite
    if len(palabra)<=0:
        return False
    if re.search('[0-9]',palabra):
        return False
    else:
        if lim==0:
            return len(palabra)<LIM_CARACTER
        else:
            return len(palabra)<=lim


def pedir_datos(mensaje, func, lim=0):
    #mensaje: es el mensaje que se le mostrara al usuario
    #func: funcion que servirá para validar lo que se ingrese
    #lim: sirve de guia. Algunas funciones reciben 2 parametros.
    #   lo hice de esta forma para evitar aumentar un argumento de relleno en validar_numero

    #Cuando el valor ingresado es aceptable, se retorna dicho valor
    entrada=input(mensaje)
    if lim==0:
        while  not func(entrada):
            print('Ingrese bien los datos')
            entrada=input(mensaje)
        return entrada
    else:
        while not func(entrada, lim):
            print('Ingrese bien los datos')
            entrada=input(mensaje)
        return entrada

def pedir_dato_tablero():
    #n: guardara la cantidad de filas y columnas que tendra la matriz
    #lista: contendra las palabras que ingrese el usuario
    #limite: marcará la cant de palabras a ingresar, como tambien los caracteres de cada palabra

    #Tanto para n, lista y nombre, se llamara a una funcion -> pedir_datos()
    #   Se encargara de tomar el ingreso del usuario para guardarlos solamente cuando sean válidos

    #Nota: palabra.casefold() servira para detectar la palabra 'fin' aún si está en mayuscula o minuscula

    # El if(len(lista)) controlara que el usuario ingrese aunque sea 1 palabra

    #Cuando los datos sean validos, se retorna una tupla con los datos

    n=pedir_datos('Ingrese la cantidad de filas y columnas para la sopa de letras: ', validar_numero)

    lista=[]
    limite=int(n)//3
    print('Lista de palabras \n   Cant. de palabras: ', limite, '\n   Cant. de caracter por palabra: ', limite, '\n   Si no desea ingresar más palabras: "Fin"')

    i=0
    while i < limite:
        palabra=pedir_datos('> ', validar_palabra, limite)
        if palabra.casefold()!='fin':
            lista.append(palabra.lower())
            i+=1
        else:
            if len(lista)>0:
                break

    nombre=pedir_datos('Ingrese un nombre para el tablero: ', validar_palabra)

    return (n, lista, nombre)


def main():
    return pedir_dato_tablero()

if __name__ == "__main__":
    main()
