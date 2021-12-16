LIM_CARACTER=30

def validar_numero(num):
    if len(num)<=0:
        return False

    return int(num)>=15

def limite_palabra(palabra, lim=0):
    if lim==0:
        return len(palabra)>0 and len(palabra)<LIM_CARACTER
    return len(palabra)>0 and len(palabra)<lim

#Lo hice de esta forma para evitar aumentar un argumento de relleno en validar_numero
def ingresar_input(mensaje, func, lim=0):
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

def pedir_tablero():
    n=ingresar_input('Ingrese la cantidad de filas y columnas para la sopa de letras: ', validar_numero)

    lista=[]
    limite=round(int(n)/3)
    print('Lista de palabras \n   Cant. de palabras: ', limite, '\n   Cant. de caracter por palabra: ', limite, '\n   Si no desea ingresar más palabras: "Fin"')
    for i in range(limite):
        palabra=ingresar_input('> ', limite_palabra, limite)
        if palabra.casefold()=='fin':
            break

        lista.append(palabra.lower())

    nombre=ingresar_input('Ingrese un nombre para el tablero: ', limite_palabra)

    return (n, lista, nombre)

print(pedir_tablero())












##Controlar tambien que se ingrese al menos una palabra para la lista!!