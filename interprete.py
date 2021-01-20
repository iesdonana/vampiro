import vocabulario as voc

_verbo = None
_nombre = None

def verbo():
    return _verbo

def nombre():
    return _nombre

def interpretar(orden):
    global _verbo
    global _nombre
    lista = orden.upper().split()
    _verbo, _nombre = None, None
    if len(lista) == 0:
        return
    if len(lista) == 1:
        buscar_verbo_primera_palabra(lista)
        return
    if len(lista) == 2:
        buscar_verbo_primera_palabra(lista)
        buscar_nombre_segunda_palabra(lista)

def buscar_verbo_primera_palabra(lista):
    global _verbo
    global _nombre
    for palabra in voc.palabras:
        if lista[0] == palabra[0]:
            if palabra[1] == voc.VERBO:
                _verbo = lista[0]
                _nombre = None
            elif palabra[1] == voc.NOMBRE:
                marcar_error_sintactico()
                _nombre = None
            break

def buscar_nombre_segunda_palabra(lista):
    global _verbo
    global _nombre
    for palabra in voc.palabras:
        if lista[1] == palabra[0]:
            if palabra[1] == voc.NOMBRE:
                _nombre = lista[1]
            else:
                marcar_error_sintactico()

def marcar_error_sintactico():
    global _verbo
    _verbo = None

def hay_error_sintactico():
    return _verbo is None
