import random
import string

#Git AndrejPetelin _ irenenaya
class Tablero:


    def __init__(self, n='', nombre=''):
        self.n = n
        self.nombre = nombre
        self.tablero = []
        self.diccionario = {}


    def __mostrar_tablero__(self, mtx):
        for i in range(len(mtx)):
            fila = ' '
            for j in range(len(mtx)):

                fila = fila+" | "+str(mtx[i][j])
            fila = fila+' |'
            print (fila)


    def __encontrar_palabra__(self, palabra):

        """
            1er if: se pregunta si la palabra pasada se encuentra en el diccionario
                en caso de estar, se procede a buscar su ubicación con la ayuda del diccionario

                if esHorizontal: aquí es dónde se convierte la palabra pasada en mayúsculas
                    es el mismo procedimiento que se hace para insertar la palabra en el tablero
                        solaemente que se añade .upper() dentro de los for

            En caso de que la palabra no se encuentre se manda un msj para el jugador
                además de un False que sirve para controlar (desde donde fue llamada la función) si
                    se debe aumentar el puntaje del jugador o no
        """

        if palabra in self.diccionario:
            valor = self.diccionario[palabra]
            inicio, fin = valor[0], valor[1]
            fila, columna = inicio[0], inicio[1]

            esHorizontal = inicio[0] == fin[0]
            if esHorizontal:
                for i in range(columna, columna+len(palabra)):
                    self.tablero[fila][i] = palabra[i-columna].upper()
            else:
                for i in range(fila, fila+len(palabra)):
                    self.tablero[i][columna] = palabra[i-fila].upper()
        else:
            print('La palabra no se encuentra en la Sopa de Letras\n\n')
            return False
        return True


    def __rellenar_matriz__(self, tablerito):
        for i in range(len(tablerito)):
            for j in range(len(tablerito)):
                if tablerito[j][i] == ' ':
                    tablerito[j][i] = random.choice(string.ascii_lowercase)
        return tablerito


    def __verificar__(self, posicion, diccionario):
        p_inicio = posicion[0]
        p_fin = posicion[1]

        for valor in diccionario.values():
            inicio, fin = valor[0], valor[1]

            if(not(p_inicio[1]>fin[1])and not(p_fin[1]<inicio[1])) and (not(p_inicio[0]>fin[0])and not(p_fin[0]< inicio[0])):
                return False
        return True


    def __posiciones__(self, lista):
        for palabra in lista:
            b=False

            while b==False:

                colum, fila, sentido = random.randint(0, int(self.n)-1), random.randint(0,int(self.n)-1), bool(random.randint(0,1))

                inicio = (fila, colum)

                if sentido:
                    if((int(self.n)-1) - fila) >= len(palabra):
                        fin = ((fila+(len(palabra)-1)), colum)
                        posiciones = (inicio, fin)
                        b = self.__verificar__(posiciones, self.diccionario)
                    else:
                        b = False
                else:
                    if((int(self.n)-1) - colum) >= len(palabra):
                        fin = (fila, (colum+(len(palabra)-1)))
                        posiciones = (inicio, fin)
                        b = self.__verificar__(posiciones, self.diccionario)
                    else:
                        b = False
            self.diccionario[palabra] = posiciones


    def __insetar__(self, tablerito, lista):
        self.__posiciones__(lista)

        for palabra in lista:
            valor = self.diccionario[palabra]
            inicio, fin=valor[0], valor[1]
            esHorizontal= inicio[0] == fin[0]
            fila, columna=inicio[0], inicio[1]

            if esHorizontal:
                for i in range(columna, columna+len(palabra)):
                    tablerito[fila][i] = palabra[i-columna]

            else:
                for i in range(fila, fila+len(palabra)):
                    tablerito[i][columna] = palabra[i-fila]

        self.tablero = self.__rellenar_matriz__(tablerito)


    def __generar__(self, lista):
        tablerito = [[' ' for i in range(int(self.n))] for j in range(int(self.n))]
        self.tablero.append(self.__insetar__(tablerito, lista))


