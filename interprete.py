import vocabulario as voc

verbo = None
nombre = None

def interpretar(orden):
    global verbo
    global nombre
    lista = orden.upper().split()
    verbo, nombre = None, None
    if len(lista) == 0:
        return
    if len(lista) == 1:
        buscar_verbo_primera_palabra(lista)
        return
    if len(lista) == 2:
        buscar_verbo_primera_palabra(lista)
        buscar_nombre_segunda_palabra(lista)

def buscar_verbo_primera_palabra(lista):
    global verbo
    global nombre
    for palabra in voc.palabras:
        if lista[0] == palabra[0]:
            if palabra[1] == voc.VERBO:
                verbo = lista[0]
                nombre = None
            elif palabra[1] == voc.NOMBRE:
                marcar_error_sintactico()
                nombre = None
            break

def buscar_nombre_segunda_palabra(lista):
    global verbo
    global nombre
    for palabra in voc.palabras:
        if lista[1] == palabra[0]:
            if palabra[1] == voc.NOMBRE:
                nombre = lista[1]
            else:
                marcar_error_sintactico()

def marcar_error_sintactico():
    global verbo
    verbo = None

def hay_error_sintactico():
    return verbo is None
