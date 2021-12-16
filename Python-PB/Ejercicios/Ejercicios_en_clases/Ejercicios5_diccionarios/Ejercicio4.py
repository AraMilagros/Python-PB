#Recibir un txt y dic(que contenga palabras prohibidas)
#Con esas palabras, reemplazarlas en el txt, con ****

def reemplazar(txt, omitir):
    numero=0

    for i in omitir:
        numero = txt.count(i)
        if numero != 0:
            txt=txt.replace(i, '****', 1)
    return txt

texto='Hoy es lunes'
dic={'es', 'azul'}

print(reemplazar(texto, dic))

def reemplazar2(txt, omitir):
    for palabra in texto.split():
        for i in omitir:
            if palabra == i:
                txt=txt.replace(palabra, '****',1)
    return txt

print(reemplazar2(texto, dic))
