class Bicicleta:
    def __init__(self, ruedas, color, velocidad):
        self.ruedas=ruedas
        self.color=color
        self.velocidad=self.__validar_velocidad__(velocidad)

    def __str__(self):
        return 'La bicicleta tiene '+ str(self.ruedas) + ' ruedas y su velocidad actual es de '+ str(self.velocidad)

    def __eq__(self, otro: object):
        return (self.ruedas == otro.ruedas) and (self.color == otro.color)

    def __multiplicar__(self, otro: object):
        return Bicicleta((self.ruedas*otro.ruedas), '', '')

    def __validar_velocidad__(self, velocidad):
        if velocidad>80:
            return 80
        elif velocidad<0:
            return 0
        else:
            return velocidad

def main():
    bici1=Bicicleta(4,'marron',30)
    print(bici1.__str__())



main()