import csv
import pathlib
import os

#!Esta clase podría tener otro nombre que refleje mejor lo que hace
class Escritor:


    def __init__(self, tablero=0, diccionario=0, nombre=''):
        """
            El método constructor recibe 3 parametros: (tablero, diccionario, nombre), los cuales tienen valores por defecto
                Estos valores sirven para poder crear un objeto de esta clase sin tener que pasar valores, y
                    porder llamar a otros métodos 'independientes'

            Entonces, en caso de crear un objeto y pasar valores por parámetro
            tablero: es la sopa de letras. Lista de listas
            diccionario: es la solución de la sopa de letras
            nombre: es el nombre de cómo se guardará la sopa de letras

            Después hay un atributo más: self.solución, que se forma apartir del parámetro nombre

        """
        self.tablero = tablero
        self.diccionario = diccionario
        self.archivo = nombre+'.csv'
        self.solucion = nombre+'_solucion.csv'


    def __archivo__(self):
        with open(self.archivo, 'w', newline='') as f:
            escritor = csv.writer(f)
            for i in self.tablero:
                escritor.writerow(i)


    def __solucion__(self):
        with open(self.solucion, 'w', newline='') as f:
            columnas = ['palabra', 'x_inicial', 'y_inicial', 'x_final', 'y_final']
            escritor = csv.writer(f)
            escritor.writerow(columnas)
            for clave, valor in self.diccionario.items():
                escritor.writerow([clave, valor[0][0], valor[0][1], valor[1][0], valor[1][1]])


    def __existe__(self, nombre):

        """
            Este es uno de los métodos 'independientes'
            Lo uso para mostrarle al usuario los nombres de las sopas de letras que puede elegir

            Recibe de párametro: nombre. Es el nombre del archivo dónde está el tablero de la sopa de letras

            completo: se usa para terminar de formar el nombre del archivo.
                Desde donde es llamado este método, se pasa el nombre del archivo sin su extensión .csv

            #Nota mia: prácticamente este es el unico lugar dónde utilizo try except... no estaba segura de dónde más aplicarlos
                por otra parte, del modo en que manejo los archivos, tampoco sé si es tan necesario aquí.

        """
        completo = nombre+'.csv'
        try:
            tablero = []
            with open(completo, newline='') as file:
                f = csv.reader(file)
                tablero = list(f)
        except FileNotFoundError:
            print('El archivo no existe')
            exit()
        return tablero


    def __regresar_solucion__(self, nombre):
        """
            Es similar al método de __existe__(), solo cambia que vuelvo a formar un diccionario para retornarlo

        """
        completo = nombre+'_solucion.csv'
        with open(completo, newline='') as file:
            f = csv.reader(file)
            lista = list(f)
            diccionario = {}
            i = 1
            while i < len(lista):
                j = 0
                diccionario[lista[i][j]] = (int(lista[i][j+1]), int(lista[i][j+2])),(int(lista[i][j+3]), int(lista[i][j+4]))
                i += 1
        return diccionario


    def __enlistar__(self):
        """
        Este método lo utilizo para enlistar todos los archivos .csv que haya en el directorio actual
            tras enlistarlos, se los muestro al jugador para que elija el tablero con el que desea jugar

        Importé pathlib y os.

        pathActual: guarda el path dónde está actualmente este archivo pero sin mostrar el archivo en sí
            por ejemplo: home/Documentos/
                en vez de: home/Documentos/archivo.py

        lista: utilizando pathActual, se guarda todos los archivos que tengan de extensión .csv

        Después de tener todos los archivos con extensión .csv
            se recorre la lista para dejar de lado los csv que tengan la solución de las sopas de letras
            para eso utilizo find y buscar en el nombre un guión bajo sabiendo que nombre_solucion.csv
            en caso de que un find regrese -1, significa que ese nombre puede guardarse

            Por ultimo, antes de guardar el nombre, se le quita la extensión .csv con splitext

        """
        pathActual = pathlib.Path(__file__).parent.absolute()
        extension = '.csv'
        lista = [_ for _ in os.listdir(pathActual) if _.endswith(extension)]
        nombresArchivos = []

        for archivos in lista:
            final = archivos.find('_')
            if final == -1:
                nombresArchivos.append(os.path.splitext(archivos)[0])
        return nombresArchivos

