import re


class Obtener_Datos:


    def __entrada__(self, msj, bool):
        """
            Es similar a la función de la parte1, solamente que sólo controla el tipo de entrada
            Es decir si es de tipo texto o numérico

            bool: me sirve de guía para saber si se quiere validar un texto o un número
        """
        entrada = input(msj)

        if bool:#Si se pasa True es para validar texto
            while not self.__texto__(entrada):
                print('La entrada no es un texto')
                entrada = input(msj)
            return entrada
        else:#Si se pasa False, es para numeros
            while not self.__numero__(entrada):
                print('La entrada no es número')
                entrada = input(msj)
            return entrada


    def __validar_limite__(self, entrada, limite, bool=None):

        """
            bool: Tambie es de guía para validar texto o numérico

            if bool == True:
                valida tanto el nombre del jugador como el nombre del tablero

            else bool == False:
                valida el límite de las filas/columnas que puede tener un tablero

            else:
                en la clase Juego (creo) se muestra una lista de archivos .csv
                    que contienen los tablero con lo que se jugará a la sopa de letras.
                    Estos archivos se muestran en una lista númerica, y se le al jugador ingresar una de esas opciones
                Entonces, aquí se valida que el usuario elija y que ese número esté dentro del rango permitido
        """

        if bool == True:
            while not self.__limite_texto__(entrada, limite):
                print('Vuelva a ingresar.')
                entrada = self.__entrada__(' >', True)
            return entrada
        elif bool == False:
            while not self.__limite_tablero__(entrada, limite):
                print('Vuelva a ingresar.')
                entrada = self.__entrada__(' >', False)
            return entrada
        else:
            while not self.__limite_lista__(entrada, limite):
                print('Vuelva a ingresar')
                entrada = self.__entrada__(' >', False)
            return entrada


    def __texto__(self, entrada):
        """
            1er if: valida que la entrada no esté vacia
            2do if: verifica que la entrada no tenga ningun numero
            
            Al final se retorna la entrada validada
        """
        if len(entrada) <= 0:
            return False
        if re.search('[0-9]', entrada):
            return False
        return entrada


    def __numero__(self, entrada):
        """
            1er if: se valida que la entrada no esté vacia
            2do if: se verifica que la entrada no tenga ningun caracter

            Al final se retorna la entrada validada
        """
        if len(entrada) <= 0:
            return False
        if re.match("\d+$", entrada):
            return entrada


    """
        Las siguientes 3 funciones, validan lo que dice sus nombres
        limite_texto: es el limite que puede tener el nombre de un tablero o el jugador
        limite_tablero: es el limite de fila/columnas de un tablero
        limite_lista: es el limite de opciones a elejir de una lista
    """

    def __limite_texto__(self, entrada, limite):
        return len(entrada) <= limite


    def __limite_tablero__(self, entrada, limite):
        return int(entrada) >= limite


    def __limite_lista__(self, entrada, limite):
        return int(entrada) <= limite

