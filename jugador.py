import localidades

_localidad_actual = localidades.VESTIBULO

def localidad_actual():               # getter, selectora
    return _localidad_actual

def mover_jugador(destino):
    global _localidad_actual
    _localidad_actual = destino
    describe_localidad_actual()

def describe_localidad_actual():
    localidad = localidades.localidad(_localidad_actual)
    print(localidades.corta(localidad))
    print(localidades.larga(localidad))

def intentar_mover(verbo):
    salidas = localidades.conexiones[localidad_actual()]
    if verbo in salidas:
        mover_jugador(salidas[verbo])
        return True
    return False
