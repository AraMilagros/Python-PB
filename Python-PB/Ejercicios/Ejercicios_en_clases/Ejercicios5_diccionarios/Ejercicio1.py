#Recibe lista de tuplas, retorna un diccionario..
    #las claves son los primeros elementos de la tupla
    #y los valores son los segundos

paises=(('argentina', 'buenos aires'), ('colombia', 'bogota'), ('uruguay', 'montevideo'))

def devolver_diccionario(paises):
    dic={}
    for i in paises:
        dic[i[0]] = i[1]
    return dic

print(devolver_diccionario(paises))
