import generar_tablero
import csv

def escribir_juego(mt, diccionario, nombre):

    #Archivo que contiene la sopa de letras
    with open((nombre+'.csv'), 'w', newline='') as linea:
        escritor=csv.writer(linea)
        lista=[]
        for fila in mt:
            lista.append(fila)
            escritor.writerow(lista)
            lista.clear()

    #Archivo que contendrá la posicion de todas las palabras en la SP
    with open((nombre+'_solucion.csv'), 'w', newline='') as linea:
        columnas=['palabra', 'x_inicial', 'y_inicial', 'x_final', 'y_final']
        escritor=csv.writer(linea)
        escritor.writerow(columnas)
    #Cada elemento del diccionario esta formado como >> clave:valor <<
    #   Donde >>clave = palabra y >>valor = (3,2),(3,7)/(x,y),(x,y)
    #   Por lo tal >>valor[0][0]=3 >>valor[0][1]=2 y >>valor[1][0]=3 >>valor[1][1]=7
        for clave, valor in diccionario.items():
            escritor.writerow([clave, valor[0][0], valor[0][1], valor[1][0], valor[1][1]])

def main():
    #return matriz, diccionario, nombre
    matriz, diccionario, nombre = generar_tablero.main()
    escribir_juego(matriz, diccionario, nombre)


if __name__ == "__main__":
    main()