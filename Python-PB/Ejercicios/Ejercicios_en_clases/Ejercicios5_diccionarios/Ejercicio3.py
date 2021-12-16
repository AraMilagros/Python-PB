#recibir 2 frases y retorna
    #si con las letras de la primera se puede formar la 2da

frase1='Ironicamente'
frase2='Renacimiento'

fraseA='Sol'
fraseB='Palabra'

def contar_letras(frase):
    dic={}
    minuscula=frase.lower()
    for letra in minuscula:
        if(letra != ' '):
            dic[letra] = minuscula.count(letra)
    return dic

def anagrama(f1, f2):
    bandera=False
    dic1={}
    dic2={}

    dic1.update(contar_letras(f1))
    dic2.update(contar_letras(f2))
#comparo solamente las claves de ambos diccionarios, es decir las letras
    #con las que están formadas las frases
    if dic1.keys() == dic2.keys():
        bandera=True
    else:
        bandera=False
    return bandera

print(anagrama(frase1, frase2))
print(anagrama(fraseA, fraseB))