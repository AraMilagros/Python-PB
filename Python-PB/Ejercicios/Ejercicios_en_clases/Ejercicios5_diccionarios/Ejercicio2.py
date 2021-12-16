#Recibe frase y devuelve diccionario
    #cuenta la cantidad de aparciones de cada letra

frase="Hoy es cuatrO de octubre hoy"

def contar_letras(frase):
    dic={}
    minuscula=frase.lower()

    for letra in minuscula:
        if(letra != ' '):
            dic[letra] = minuscula.count(letra)
    return dic

dic={}
dic.update(contar_letras(frase))
print(dic)

