
def area_base(r):
    area=2*3.1415*r
    return area

def volumen_cilindro(h, r):
    area = area_base(r)
    volumen = area*h
    return volumen, area

#def validar(n):
#    aprobar=False
#    if(n>0):
#        aprobar=True
#    else: aprobar=False
#    return aprobar

#Principal
bandera = True

while(bandera):
    print('#Ingrese un número positivo#')
    h = int(input('     Altura: '))
    if(h>0):
        print('#Ingrese un número positivo#')
        r = int(input('     Radio: '))

        if(r>0):
            print()
            print('#Resultados#')
            volumen, area = volumen_cilindro(h, r)
            print('     El área base es: ',area)
            print('     El volumen del cilindro es: ', volumen)
            #Saldra del while recien cuando se realicen los cálculos,
            # es decir, una vez que se ingrese los valores permitidos
            bandera = False
        else:
            print()
            print('### No se aceptan valores menores a cero ###')
            print()

    else:
        print()
        print('### No se aceptan valores menores a cero ###')
        print()
