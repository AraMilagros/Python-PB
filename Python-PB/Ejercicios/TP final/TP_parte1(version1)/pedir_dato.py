import re
LIM_CARACTER=30

def validar_numero(num):
    if len(num)<=0:
        return False
    if re.match("[-+]?\d+$", num):#es True solo si NO se encuentra una letra
        return int(num)>=15
    return False

def validar_palabra(palabra, lim=0):
    if len(palabra)<=0:
        return False
    if re.search('[0-9]',palabra):
        return False
    else:
        if lim==0:
            return len(palabra)<LIM_CARACTER
        else:
            return len(palabra)<lim

#Lo hice de esta forma para evitar aumentar un argumento de relleno en validar_numero
def ingresar_input(mensaje, func, lim=0):
    entrada=input(mensaje)
    if lim==0:
        while  not func(entrada):
            print('Ingrese bien los datos')
            entrada=input(mensaje)
        return entrada
    else:
        while not func(entrada, lim):
            print('Ingrese bien los datos')
            entrada=input(mensaje)
        return entrada
