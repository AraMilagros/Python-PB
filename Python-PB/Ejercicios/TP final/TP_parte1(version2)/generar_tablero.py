import pedir_datos_tablero

#Los uso para generar aleatoriamente tanto numeros como letras
import random
import string

#Guardara las posiciones de las palabras
diccionario={}

def mostrar_tablero(mtx):
    for i in range(len(mtx)):
        fila = ' '
        for j in range(len(mtx)):
            fila = fila+" | "+str(mtx[i][j])
        fila = fila+' |'
        print (fila)

def rellenar_matriz(mt):
    #mt: matriz con palabras ya insertadas
    # se utiliza random.choise para generar las letras aleatorias
    for i in range(len(mt)):
        for j in range(len(mt)):
            if mt[j][i] == ' ':
                mt[j][i] = random.choice(string.ascii_lowercase)
    return mt

def verificar_diccionario(posicion, diccionario):
    #posicion: es una tupla con los numeros de fila/columna de una palabra
    #diccionario: se guardan las palabras con sus posiciones, ya validadas

    #p_inicio: contiene la fila y columna del inicio de la palabra
    #p_fin: contiene la fila y columna del final de la palabra

    #Una vez que se tenga el inicio y fin(posiciones) de la ultima palabra que se quiere insertar
    #se recorre el diccionario para comprobar que estas ultimas posiciones no coincidan con otras

    #   inicio: seria la posicion(fila,columna) del inicio de una palabra ya validada
    #   fin: posicion(fila,columna) del final de una palabra ya validada

    #   p_inicio[0]: fila donde comienza la ultima palabra que se quiere insertar
    #   inicio[0]: fila donde comienza una palabra ya validada (y guardada en el diccionario)

    #   Con p_fin[0] y fin[0] es basicamente lo mismo, solamente que marcan el final de la palabra

    #En caso de que las ultimas posiciones generadas, esten entre las posiciones ya guardadas en el diccionario
    #   Se retornara un False para que en la funcion de donde fue llamada, generen nuevas posiciones
    #   Si las ultimas posiciones generadas son validas, se retornara un True para ser guardadas en el diccionario
    p_inicio=posicion[0]
    p_fin=posicion[1]

    for valor in diccionario.values():
        inicio=valor[0]
        fin=valor[1]

        #if (p_inicio[0] >= inicio[0] and p_inicio[0] <= fin[0]) or (p_fin[0] >= inicio[0] and p_fin[0] <= fin[0]):
        #   return False
    #return True
        if(not(p_inicio[1]>fin[1])and not(p_fin[1]<inicio[1])) or (not(p_inicio[0]>fin[0])and not(p_fin[0]< inicio[0])):
            return False
    return True

def generar_posiciones(palabra, limite):
    #palabra: palabra que se envia para determinar su posicion en la matriz
    #limite: el tamaño de largo de la matriz
    #diccionario: guarda las palabras con sus posiciones ya validadas

    #columna/fila: numero aleatorio entre 0 y la longitud de la matriz
    #direccion: determinara si la palabra se ingresara vertical u horizontalmente
    #           True: vertical _ False: horizontal
    #

    #Luego de generarse la direccion, se comprobara si la palabra entrara en la matriz
    #   Esto se comprueba restando el largo de la matriz con en num de fila/columna generada
    #   y si el num resultante es mayor o igual al largo de la palabra, se pasa a otra validacion

    #Si las posiciones son admitidas, se guardan en forma de tuplas
    #   Donde inicio/fin(fila,columna) marcaran el principio y final de la palabra respectivamente
    #   Dependiendo si sea vertical/horizontal, a la fila o columna sele aumentara la longitud de la palabra

    #Una vez guardadas, serán enviadas a otra funcion

    #Al finalizar, se enviará en un diccionario: todas las palabras con sus posiciones validadas

    bandera=False
    while bandera==False:
        columna=random.randint(0, limite)
        fila=random.randint(0, limite)
        direccion=bool(random.randint(0,1))

        if direccion:#vertical
            if (limite-fila) >= len(palabra):
                inicio=(fila, columna)
                fin=( (fila + (len(palabra)-1) ), columna)

                posiciones=(inicio, fin)
                bandera=verificar_diccionario(posiciones, diccionario)

            else:
                bandera=False

        else:#horizontal
            if(limite-columna) >= len(palabra):
                inicio=(fila, columna)
                fin=(fila, (columna+(len(palabra)-1)) )
                posiciones=(inicio, fin)

                bandera=verificar_diccionario(posiciones, diccionario)
            else:
                bandera=False

    return posiciones

def insertar_palabras(mt, palabras):
    #mt: matriz
    #palabras: lista de palabras para insertar en la matriz

    #limite: largo de la matriz
    #palabras_coordenadas: diccionario que guaradara las posiciones de las palabras en la matriz

    #Se recorre la lista de palabras pasadas
    # en cada iteracion se llamara a generar_posiciones y lo que retorne se guardará en el diccionario

    #Una vez que todas las palabras tengan sus posiciones validadas, se recorre una vez mas la lista
    #   pero esta vez ya para insertarlas en la matriz

    #   valor: posiciones de la palabra en la matriz
    #       valor=( (fila,columna), (fila,columna) )
    #   La primera tupla es el inicio de la palabra mientras que el segundo, es el final

    # inicio, fin = valor[0], valor[1] seria inicio = (fila,columna) | fin = (fila,columna)
    # fila, columna = inicio[0], inicio[1] seria fila=fila | columna = columna
    #   Estas ultimas 2 lineas explicadas, es más para que dentro del for sea más entendible

    # esHorizontal: boolean. Servira para saber si palabra tendra que ser insertada horizontal o vertical
    #   si da True, es horizontal y variara sólo la columna
    #   si es False, es vertical y variará la fila

    #   palabra[i-columna] o palabra[i-fila] regresara una letra de la palabra que se está insertando

    #Cuando se insertan todas las palabras,
    # se llamara a un ultimo metodo para llenar de letras random lo que resta de la matriz

    limite=len(mt[0])-1

    for palabra in palabras:
        diccionario[palabra]=generar_posiciones(palabra, limite)

    for palabra in palabras:
        valor = diccionario[palabra]

        inicio, fin=valor[0], valor[1]
        esHorizontal= inicio[0] == fin[0]

        fila, columna=inicio[0], inicio[1]

        if esHorizontal:
            for i in range(columna, columna+len(palabra)):
                mt[fila][i] = palabra[i-columna]

        else:
            for i in range(fila, fila+len(palabra)):
                mt[i][columna] = palabra[i-fila]

    return rellenar_matriz(mt)


def generar_tablero(n, lista_palabras):
    tablero = [[' ' for i in range(n)] for j in range(n)]
    return insertar_palabras(tablero, lista_palabras)


def main():
    #return (n, lista, nombre)
    tupla=()
    tupla=pedir_datos_tablero.main()
    matriz=generar_tablero(int(tupla[0]), tupla[1])
    mostrar_tablero(matriz)
    return matriz, diccionario, tupla[2]


if __name__ == "__main__":
    main()
