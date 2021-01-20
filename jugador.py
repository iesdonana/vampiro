import localidades

localidad_actual = localidades.VESTIBULO

def mover_jugador(destino):
    global localidad_actual
    localidad_actual = destino
    describe_localidad_actual()

def describe_localidad_actual():
    localidad = localidades.localidades[localidad_actual]
    print(localidad[1])
    print(localidad[0])
