# Escribir una función que permita calcular la duración en segundos 
# de un intervalo dado en horas, minutos y segundos

def convertir_a_intervalo(horas, minutos , segundos):
    # 1 min = 60 segundos
    # 1 h = 60 minutos
    # 1 min ________60 segundos
    # minutos_______ x=minutos*60
    horas *= 3600 #Horas a segundos
    minutos *= 60 #Minutos a segundos

    return horas + minutos + segundos

# Escribir una función que permita calcular la duración en horas, minutos y segundos 
# de un intervalo dado en segundos
def convertir_a_horas_min_seg(intervalo): 
    # El intervalo viene en segundos
    # 1 h ____________ 3600 seg
    #     ___________ intervalo
    # 20000 segundos
    # segundos = intervalo
    # minutos = intervalo/60
    horas = intervalo//3600
    auxiliar = intervalo % 3600 #Lo que sobra de segundos
    minutos = auxiliar//60
    segundos = auxiliar % 60 #Lo que sobra de segundos

    return horas,minutos,segundos

# Usando las funciones de los puntos A y B, generar un programa que le pida 
# al usuario dos intervalos expresados en horas, minutos y segundos; sume 
# sus duraciones y muestre por pantalla la duración total en horas, minutos
#  y segundos

duracion1 = convertir_a_intervalo(1, 50 , 30) #6630 segundos
duracion2 = convertir_a_intervalo(0, 30 , 15) #1815 segundos

suma = duracion1 + duracion2   #8445

print(convertir_a_horas_min_seg(suma)) #2 h 20 min 45 seg

