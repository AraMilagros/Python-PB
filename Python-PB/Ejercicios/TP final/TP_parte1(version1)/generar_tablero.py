import random
#hola=[]
#hola=generar_tablero(3, 'hola')
#print('Tablero')
#print(hola)
#for fila in hola:
#    print(fila)


#Funcion que genera tablero de la SP
#   recibe un N y lista de palabras
#   RETORNA matriz NxN
#las palabras de la lista deben estar de forma horizontal/vertical
#MINUSCULAS

#python random https://docs.python.org/es/3/library/random.html

def generar_tablero(n, palabras):

    tablero=[]
    fila=[]
    for i in range(n):
        #tablero.append('*')
        fila.append('*')
        for j in range(n-1):
            fila.append('*')
        tablero.append(fila)
        fila=[]
#Ejemplo quedaria:
    # * - - - sale y regresa al primero: * - - - y etc etc
#entra al primer FOR y sigue al segundo
    #es el 2d FOR que termina su ciclo y sale para volver al 1ro
    return tablero

tabla=[]
tabla=generar_tablero(15,'ohas')
# random.randint(0,9)
palabras=['catorcemil', 'dos', 'tres', 'cuat', 'cinc']


def mostrar_tablero(mtx):
    for i in range(len(mtx)):
        fila = ' '
        for e in range(len(mtx)):
            fila = fila+" | "+str(mtx[i][e])
        fila = fila+' |'
        print (fila)

def insertar_palabras(palabras, tablero):
    posicion_inicial=0
    posicion_final=len(tablero[0])

    for i in tablero:
        print(i)
        posicion_inicial=random.randint(0, posicion_final)

        print('random: ',posicion_inicial)

        posiciones_libres=posicion_final-posicion_inicial

        if posiciones_libres>=len(palabras[1]):
            print('puede ingresarse')
            print('posiciones libres: ', posiciones_libres)
            print('cant de caracteres: ',len(palabras[1]))
            for i in palabras[1]:
                for letra in i:
                    print(letra)
                    for num in range(posicion_inicial, posicion_final):
                        tablero[num]=letra
            print('tablero despues del for: ')
            mostrar_tablero(tablero)
        else:
            print('nose puede ingresar')
insertar_palabras(palabras, tabla)

def intento(palabras, tablero):

    for columna in tablero:
        inicio=random.randint(0, len(columna))
        final=len(columna)
        posicion_libre=final-inicio

        for elemento in palabras:
            if posicion_libre >= len(elemento):
                pass