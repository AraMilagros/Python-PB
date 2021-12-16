import random
import string

def generar_tablero(n, lista):
    tablero = [[' ' for i in range(n)] for j in range(n)]

    #matrizFinal=insertar_palabras(tablero, lista)
    return tablero

p=generar_tablero(15, 'lista de palabras')



def mostrar_tablero(mtx):
    for i in range(len(mtx)):
        fila = ' '
        for e in range(len(mtx)):
            fila = fila+" | "+str(mtx[i][e])
        fila = fila+' |'
        print (fila)

#Recibe de parametro:
    #palabra: la palabra a insertar
    #matriz.. que serviria para sacar la longitud admitida
    #posiciones: diccionario. Donde se guardan las posiciones de palabras ya insertadas
def generar_posiciones(palabra, limite, diccionario):
    #True: vertical. False: horizontal
    #print(matriz[fila][columna])
    #i = columna _ j = fila
    bandera=False
    while bandera==False:
        columna=random.randint(0, limite)
        fila=random.randint(0, limite)
        direccion=bool(random.randint(0,1))#Determinara si la palabra se ingresara vertical u horizontal
    #limite-fila=posiciones libres
        if direccion:#vertical
            if (limite-fila) >= len(palabra):
                inicio=(fila, columna)
                fin=( (fila+(len(palabra)-1) ), columna)
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

    diccionario[palabra]=posiciones
    return diccionario

#Regresara True, en caso de que NO coincidan
def verificar_diccionario(posicion, diccionario):

    p_inicio=posicion[0] #inicio(fila, columna)
    p_fin=posicion[1] #fin (fila, columna)

    for valor in diccionario.values():
        inicio=valor[0]
        fin=valor[1]

        if (p_inicio[0] >= inicio[0] and p_inicio[0] <= fin[0]) or (p_fin[0] >= inicio[0] and p_fin[0] <= fin[0]):
            return False
    return True


palabras=['uno', 'dos', 'tres', 'cuat']

def insertar_palabras(mt, palabras):
    limite=len(mt[0])-1
    palabras_coordenadas={}
    for palabra in palabras:
        palabras_coordenadas=generar_posiciones(palabra, limite, palabras_coordenadas)

    for palabra in palabras:
        valor = palabras_coordenadas[palabra]
        inicio, fin=valor[0], valor[1]

        ban= inicio[0] == fin[0]
        fila, columna=inicio[0], inicio[1]

        if ban:
            for i in range(columna, columna+len(palabra)):
                mt[fila][i] = palabra[i-columna]
        else:
            for i in range(fila, fila+len(palabra)):
                mt[i][columna] = palabra[i-fila]
    print(palabras_coordenadas)
    return mt


def rellenar_matriz(mt):
    for i in range(len(mt)):
        for j in range(len(mt)):
            if mt[j][i] == ' ':
                mt[j][i] = random.choice(string.ascii_lowercase)
    return mt


kk=insertar_palabras(p, palabras)
lol=rellenar_matriz(kk)
mostrar_tablero(lol)
