#funcion concatenar que reciba una tupla con multiples strings
# y un string como separador, y regrese un string que contenga a todos

def concatenar(str1, str2):
    tuplaFinal=""

    for i in range(len(str1)):
        tuplaFinal+=str1[i]

        if(i != len(str1)-1):
            tuplaFinal+=str2

    return tuplaFinal

##NOTA: cuando se quiere acceder al contenido de un elemento en la tupla,
##  se utiliza los [ corchetes ] por ej: tupla[posicion]
tupla=('hola', 'como', 'estan')
himno = ('el', 'grito', 'libertad', 'libertad', 'libertad')
separador = ('-')

print(concatenar(tupla, separador))
print(concatenar(himno, separador))