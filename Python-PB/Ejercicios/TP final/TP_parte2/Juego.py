from Obtener_Datos import Obtener_Datos
from Tablero import Tablero
from Escritor import Escritor
from Jugador import Jugador

class Juego:


    def __init__(self, tablero = '', usuario = ''):
        """
        Este método constructor recibe como párametros tablero y usuario que tienen valores por defecto
            y ahora viéndolo por última vez para explicarlo, creo que podría sacarlos. Pero bueno.

        """
        self.tablero = tablero
        self.usuario = usuario


    def __iniciar__(self):
        """
        Este método es llamado desde Principal, y antes de comenzar a pedir datos
            verifica si en la carpeta actual existe algún archivo para jugar a la sopa de letras
            con: lista = escritor.__enlistar__(). Creando un objeto de la clase Escritor()
            en caso de no haber ninguno, directamente se llamará: self.__armando_tableros__()
                luego de haber creado el tablero, llamara self.usuario__() para empezar a jugar


        """
        escritor = Escritor()
        lista = escritor.__enlistar__()
        if len(lista) > 0:
            datos = Obtener_Datos()
            msj1='¿Desea crear un tablero antes de empezar a jugar? (Si/No)'
            entrada = datos.__entrada__(msj1, True)
    #!Verificar bien la entrada.. que sea solamente sí para que continue crando tableros
            while entrada.casefold() != 'no':
                self.__armando_tableros__()
                entrada = datos.__entrada__(msj1, True)
            self.__usuario__()

        else:
            print('Primero cree un tablero para poder jugar')
            self.__armando_tableros__()
            self.__usuario__()


    def __armando_tableros__(self):

        """
            Aqui creo un objeto de la clase Obtener_Datos() para los datos ingresados
                datos = Obter_Datos()

            A diferencia de la parte 1 del TP, donde tenía 1 sola función que validaba tanto la entrada
                como el limite de una palabra o número, aquí tengo 2 funciones distintas
                Es por eso que antes de que la entrada se guarde en n, se llama a 2 funciones
                    1: datos.__entrada__(mensaje, bool) que recibe el msj que verá el jugador
                        y un bool, que sirve para saber si se espera una entrada tipo texto o numérico
                    2: datos.__validar_limite__(entrada, limite, bool) también recibe un bool para
                        saber si se valida una entrada de tipo texto o numérico
                        entrada: es la entrada validada que ahora se verifica si cumple con la condición de límite
                        limite: es el límite de la entrada

            limite=int(n)//3: se obtiene el limite que no tendrá que sobrepasar las palabras que se ingresen

            while i < limite: controlara la cantidad de palabras que se ingresará
                Al igual cuando se capturó n, ocurre lo mismo con cada palabra
                Se llama a 2 funciones __entrada__() y __validar_limite__()
                Lo que cambia es el último parámetro que ahora es True, al esperar una entrada de tipo texto

            Y ocurre lo mismo al momento de capturar el nombre para el tablero

            Con los datos validados y guardados, se crea un objeto de Tablero para generar el tablero
            Y luego se crea un objeto de la clase Escritor para crear los archivos que contendran
                el tablero de la sopa de letra que se mostrará al jugador
                y luego también un archivo que contendrá la solución, es decir la posición de todas las palabras

        """

        datos = Obtener_Datos()

        msj1 = 'Ingrese la cantidad de filas y columnas para la sopa de letras: '
        n = datos.__validar_limite__(datos.__entrada__(msj1, False), 15, False)

        limite=int(n)//3
        lista = []
        i = 0
        msj2 = 'Ingrese las palabras para la sopa de letras: '
        while i < limite:
            palabra = datos.__validar_limite__(datos.__entrada__(msj2, True), limite, True)

            if palabra.casefold() == 'fin':
                break
            else:
                lista.append(palabra.lower())
            i += 1

        msj3 = 'Ingrese un nombre para el tablero: '
        nombre = datos.__validar_limite__(datos.__entrada__(msj3, True), 30, True)

        #Generando tablero
        tablerito = Tablero(n, nombre)
        tablerito.__generar__(lista)

        #Creando archivos
        escritor = Escritor(tablerito.tablero, tablerito.diccionario, tablerito.nombre)
        escritor.__archivo__()
        escritor.__solucion__()


    def __usuario__(self):

        """
            nombreJugador: se guarda el nombre del mismo modo que se capturó los anteriores datos de tablero

            lista=escritor.__enlistar__()
                En la clase Escritor() hay un método enlistar() que extrae los nombres de todo archivo con extension .csv (en este caso)
                Lo llamo aquí para mostrarle al jugador los tableros disponibles para jugar
                Lo que se hace en el siguiente for
                    for item in range(len(lista))....

            num: se le pide al jugador ingresar el número del tablero que desea

            tablero: con la elección del jugador, se llama a __existe__() que nos regresará el tablero guardado en ese archivo
            diccionario: obtenemos también la solución del tablero guardado

            Ahora se crea un objeto de Tablero: tableritoFinal. Para guardar el tablero y el diccionario recién recibidos
            Sucede lo mismo con jugador. Se guarda tanto el nombre ingresado como el tablero elegido,
                pero también una lista de las palabras que se encuentran en el tablero, apartir del diccionario recibido

            Por ultimo se actualiza los atributos de la clase Juego
                asignándoles a usuario y tablero los objetos de las clases Jugador y Tablero, respectivamente

            Al final se llama self.__mostrar__()
        """

        datos = Obtener_Datos()

        msj1 = 'Ingrese un nombre para su jugador: '
        nombreJugador = datos.__validar_limite__(datos.__entrada__(msj1,True), 40, True)

        #=======
        escritor = Escritor()
        lista = escritor.__enlistar__()
        for item in range(len(lista)):
            print(item+1,': ',lista[item])

        msj = 'Elija un tablero para jugar. Elija un número: '
        num = datos.__validar_limite__(datos.__entrada__(msj, False), len(lista))

        #=======
        tablero = escritor.__existe__(lista[int(num)-1])
        diccionario = escritor.__regresar_solucion__(lista[int(num)-1])

        #=======
    #!Esto podría hacerse en una funcion
        tableritoFinal = Tablero()
        tableritoFinal.tablero = tablero
        tableritoFinal.diccionario.update(diccionario)

        jugador = Jugador(nombreJugador, tablero)
        jugador.total_palabras=list(tableritoFinal.diccionario.keys())

        self.usuario = jugador
        self.tablero = tableritoFinal

        #=======
        self.__mostrar__()


    def __mostrar__(self):

        """

            self.tablero.__mostrar_tablero__()
                se utiliza los atributos de esta clase para mostrar el tablero que se guardó
                    en el atributo tablero de la clase Jugador

            entrada: se pide al jugador ingresar una palabra que encontró
                luego de ser validada (verificar si era texto), se buscará la palabra
                con self.tablero.__encontrar_palabra__(entrada)
                    este método regresa True o False en caso de encontrar la palabra o no
                    Si es True, se procede a guardar la palabra encontrada y aumentar puntaje
                        con self.usuario.__actualizar__(entrada)
                    Luego se vuelve a mostrar el tablero, que en caso de haberse encontrado una palabra,
                        dicha palabra ahora aparecerá en mayúsculas

            if len(self.usuario.palabras_encontradas) == len(self.usuario.total_palabras):
                controla que en caso de que palabras_encontradas coincida con total_palabras,
                    significa que no hay más palabras que encontrar y termina de salir del while

            Al final, ya sea si se encontró todas las palabras o el jugador ingresó 'fin' para finalizar
                se mostrará el puntaje del jugador, al igual que las palabras que encontró y las que no
        """
        datos = Obtener_Datos()

        print(' -Ingrese las palabras que encuentre-\n\n')
        self.tablero.__mostrar_tablero__(self.usuario.tablero)


        entrada = datos.__entrada__(' > ', True)
        while entrada != 'fin':

            if self.tablero.__encontrar_palabra__(entrada):
                self.usuario.__actualizar__(entrada)
            self.tablero.__mostrar_tablero__(self.usuario.tablero)

            if len(self.usuario.palabras_encontradas) == len(self.usuario.total_palabras):
                break

            entrada = datos.__entrada__(' >> ', True)

        self.usuario.__mostrar_puntaje__()


