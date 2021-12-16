#correo: irenya@hotmail.com

#Se utiliza el metodo lower para convertir toda la cadena en minusculas
def AMinusculas(palabra):#REHACER
    minuscula=str.lower(palabra)
    return minuscula
#1erFor: recorre la palabra, caracter por caracter (letra por letra)
#2doFor: recorre el dic(acentos), guiandose por las claves del dic (i)
    #if: compara la letra de la palabra con la clave del dic
        #de ser True, se reemplaza la letra/caracter actual con el valor del dic
#Por ultimo, retorna el string con los cambios hechos
def ConvertirAcentos(palabra, acentos):#REHACER
    pconvertido=''
    bandera=False
    for caracter in palabra:
        for i in acentos:
            if caracter == i:
                pconvertido = palabra.replace(caracter, acentos[i])
                bandera=True
    return pconvertido, bandera #retorna string sin acento, y una bandera que aumente

#Se recorre cada elemento de la lista pasada
    #Y si el elemento NO se encuentra en la nueva lista, se agrega
def EliminarDuplicados(palabras):#recibe una lista
    sinDuplicado=[]
    for palabra in palabras:
        if palabra not in sinDuplicado:
            sinDuplicado.append(palabra)
    return sinDuplicado

#Se utiliza el metodo sorted para ordenar la lista alfabeticamente
    #Y se retorna una nueva lista ordenada
def Ordenar(palabras):#REHACER
    ordenado=[]
    for p in sorted(palabras):
        ordenado.append(p)
    return ordenado

#1erFor: recorre palabra por palabra entre la lista pasada
#2doFor: recorrer cada letra/caracter de cada palabra
#3erFor: recorrer cada clave del diccionario pasado
    #cada clave es comparada por cada letra/caracter de una palabra
    #en caso de ser True, se agregara a una lista remover
def RemoverPalabrasInvalidas(palabras, letras):#REHACER
    remover = []
    newLista = []
    for palabra in palabras:
        for caracter in palabra:
            for letra in letras:
                if letra == caracter:
                    remover.append(palabra)
                    break#una vez que encuentra una letra no admitida, no necesita seguir recorriendo la palabra
#Este for es igual al 1ro..
    #se pregunta si una palabra NO se encuentra en la lista remover
    #si no se encuentra, se agregara la palabra a la lista que terminara retornando
    for palabra in palabras:
        if palabra not in remover:
            newLista.append(palabra)
    return newLista

#lo que mando
def otroRemover(palabras, letra):
    for palabra in palabras:
        for caracter in palabra:
            if caracter in letra:
                print('si esta')



acentos = {#en el for la clave seria i, mientras que el valor es acentos[i]
    'á' : 'a',
    'é' : 'e',
    'í' : 'i',
    'ó' : 'o',
    'ú' : 'u'
}

omitir=['k', 'w']
prueba=['koku','lluvia', 'ol', 'ulu', 'washington', 'gato', 'kumbia', 'water']
#mayusculas = ['Zona', 'walteR', 'WALTER', 'BÉAR', 'INNER', 'CHILD', 'CHILD', 'KOOKY']

def ProcesarLista(palabras, acentos, omitir):
    minusculas=[]
#1ro todos los string a minusculas
    for palabra in palabras:
        minusculas.append(AMinusculas(palabra))
#2do eliminar posibles duplicados
    sinDuplicado=EliminarDuplicados(minusculas)
#3ro remover palabras no admitidas
    remover=RemoverPalabrasInvalidas(sinDuplicado, omitir)
#4to quitar acentos de las palabras que quedan
    lista=[]
    for elemento in remover:
        string, bandera=ConvertirAcentos(elemento, acentos)
        if bandera:
            lista.append(string)
        else:
            lista.append(elemento)
#5to por ultimo ordenar la lista y retornar
    lista = Ordenar(lista)
    return lista


def main():
    palabras = ['hola', 'María', 'kiosko', 'Mañana', 'camión', 'WALTER', 'árbOL', 'PERRO', 'buey', 'xilofón', 'porqué', 'búho', 'Camión']
    print(palabras)
    print(ProcesarLista(palabras, acentos, omitir))

if __name__ == "__main__":  # no remover esta directiva!!
    main()
