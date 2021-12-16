
class Jugador:

    def __init__(self, nombre, tablero):
        """

            nombre: nombre del jugador
            tablero: tablero que el jugador eligió

            self.puntaje: son los puntos por cada palabra encontrada
            self.total_palabras: son todas las palabras que están en el tablero elegido
            self.palabras_encontradas: son las palabras que el jugador va encontrando mientras juega
        """
        self.nombre = nombre
        self.tablero = tablero
        self.puntaje = 0
        self.total_palabras = ''
        self.palabras_encontradas = []


    def __mostrar_puntaje__(self):
        """
            if len(self.palabras_encontradas) < len(self.total_palabras):
                Se verifica si la 1ra lista es menor en numero con la 2da lista
                Si es así, quiere decir que aún hay palabras que no se encontró

                for palabra in self.total_palabra_:
                    se recorre la lista donde están todas las palabras del tablero
                    if palabra not in self.palabras_encontradas:
                        sólo las quen o se encuentren en dicha lista, se guardará en otra lista
                        para mostrarle al jugador las palabras faltantes

            for p in sorted(faltantes, key....)
                se supone que ordena la lista independientemente si es mayuscula o minuscula
                pero creo que podría obviar de esto, ya que al momento de guardar las palabras (cuando creo el tablero)
                    siempre las guardo en minuscula, utilizanod .lower()

            Al final se muestra las palabras que encontró y las que no
        """
        print('Jugador: '+str(self.nombre)+'. Puntaje actual: '+str(self.puntaje))

        if len(self.palabras_encontradas) < len(self.total_palabras):
            faltantes=[]

            for palabra in self.total_palabras:
                if palabra not in self.palabras_encontradas:
                    faltantes.append(palabra)
            ordenado = []
            for p in sorted(faltantes, key=str.casefold):
                ordenado.append(p)

        print('Palabras encontradas: ', self.palabras_encontradas)
        print('Palabras faltantes: ', ordenado)


    def __palabras_faltantes__(self):
        for palabra in self.palabras_faltantes.sorted():
            print(' > '+palabra)


    def __actualizar__(self, entrada):
        """
            self.puntaje: aumenta los puntos a medida que se encuentra una palabra
            self.palabras_encontradas: se va guardando las palabras encontradas
        """
        self.puntaje += 1
        self.palabras_encontradas.append(entrada)