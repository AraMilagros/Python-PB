
def sumaMultiplos():
    suma = 0
    for i in range(1000):
        if ((i!= 0) and (i%3 == 0 or i%5 == 0)):
            print(i)
            suma += i
    print ('Suma total entre los múltiplos: ', suma)

sumaMultiplos()
