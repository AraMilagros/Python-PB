#Se dispone un archivo con numeros uno por linea
#la funcion recibe el path, retorna suma de los numeros
import csv

path='archivo.txt'

def archivo(path): #archivo ya creado..
    numero=0
    with open(path) as archivo:
        for linea in archivo:
            numero+=int(linea)
    return numero

print(archivo(path))

with open('ar.csv', 'w') as nombre:
    print(nombre)
    titulo=['numero', 'cuadrado', 'cubo']
    escritor=csv.writer(nombre)
    escritor.writerow(titulo)
    for i in range(1,11):
        lista=[str(i)]
        lista.append(str(i**2))
        lista.append(str(i**3))
        escritor.writerow(lista)

#https://extendsclass.com/csv-generator.html