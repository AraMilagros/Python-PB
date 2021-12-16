import csv

path='myFile.csv'

def recorrer_archivo(path, num):
    listaDeDict=[]
    with open(path) as archivo:
        lector=csv.DictReader(archivo)
        for linea in lector:
            if int(linea['precio']) > num:
                listaDeDict.append(linea)
    return listaDeDict

def crear_csv(path, num):
    with open('ultimo.csv', 'w') as nombre:
        print(nombre)
        titulo=['producto', 'precio', 'descripcion']
        escritor=csv.writer(nombre)
        escritor.writerow(titulo)

        general=[]
        itemCsv=[]
        general=recorrer_archivo(path, num)

        for item in range(len(general)):# genera[item] seria cada diccionario
            for valor in general[item].values():
    #En c/diccionario, se guarda los valores que no tengan de clave 'id'
                if valor != general[item]['id']:
                    itemCsv.append(valor)
            escritor.writerow(itemCsv)
            itemCsv.clear()

crear_csv(path, 30)
