def AMinusculas(palabra):
    minuscula=str.lower(palabra)
    return minuscula

def ConvertirAcentos(palabra, acentos):#Modificado
    pconvertido=''
    for caracter in palabra:
        for i in acentos:
            if caracter == i:
                pconvertido = palabra.replace(caracter, acentos[i])

    if pconvertido == '':
        pconvertido=palabra

    return pconvertido

def EliminarDuplicados(palabras):
    sinDuplicado=[]
    for palabra in palabras:
        if palabra not in sinDuplicado:
            sinDuplicado.append(palabra)
    return sinDuplicado

def Ordenar(palabras):#Modificado
    ordenado=[]
    for p in sorted(palabras, key=str.casefold):
        ordenado.append(p)
    return ordenado

def RemoverPalabrasInvalidas(palabras, letra):#Modificado
    remover=[]
    newLista=[]
    for palabra in palabras:
        for caracter in palabra:
            if caracter in letra:
                remover.append(palabra)
                break
    for palabra in palabras:
        if palabra not in remover:
            newLista.append(palabra)
    return newLista

acentos = {
    'á' : 'a',
    'é' : 'e',
    'í' : 'i',
    'ó' : 'o',
    'ú' : 'u',
    'Á' : 'A',
    'É' : 'E',
    'Í' : 'I',
    'Ó' : 'O',
    'Ú' : 'U'
}
omitir=['k', 'w']

#prueba=['koku','lluvia', 'ol', 'ulu', 'washington', 'gato', 'kumbia', 'water']
#mayusculas = ['Zona', 'walteR', 'WALTER', 'BÉAR', 'INNER', 'CHILD', 'CHILD', 'KOOKY']

def ProcesarLista(palabras, acentos, omitir):
    minusculas=[]
#1ro todos los string a minuscula
    for palabra in palabras:
        minusculas.append(AMinusculas(palabra))
#2do eliminar posibles duplicados
    sinDuplicado=EliminarDuplicados(minusculas)
#3ro remover palabras no admitidas
    remover=RemoverPalabrasInvalidas(sinDuplicado, omitir)
#4to quitar acentos de las palabras que quedan
    sinAcento=[]
    for palabra in remover:
        sinAcento.append(ConvertirAcentos(palabra, acentos))
#5to por ultimo ordenar la lista y retornar
    return Ordenar(sinAcento)

def main():
    palabras = ['hola', 'María', 'kiosko', 'Mañana', 'camión', 'WALTER', 'árbOL', 'PERRO', 'buey', 'xilofón', 'porqué', 'búho', 'Camión']
    #print(palabras)
    print(ProcesarLista(palabras, acentos, omitir))

if __name__ == "__main__":  # no remover esta directiva!!
    main()
