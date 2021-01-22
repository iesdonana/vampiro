VESTIBULO = 0
MITAD_PASILLO = 1
COCINA = 2
BIBLIOTECA = 3

DESC_CORTA = 0
DESC_LARGA = 1

_localidades = {
    VESTIBULO: {
        DESC_CORTA: 'VESTÍBULO',
        DESC_LARGA: 'Estás en el vestíbulo del castillo.',
    },
    MITAD_PASILLO: {
        DESC_LARGA: 'Estás en mitad del pasillo.',
        DESC_CORTA: 'MITAD PASILLO'
    },
    COCINA: {
        DESC_LARGA: 'Estás en la cocina.',
        DESC_CORTA: 'COCINA'
    },
    BIBLIOTECA: {
        DESC_LARGA: 'Estás en la biblioteca.',
        DESC_CORTA: 'BIBLIOTECA'
    },
}

"""
Cocina --- Mitad pasillo --- Biblioteca
                |
            Vestíbulo
"""

_conexiones = {
    VESTIBULO: {
        'N': MITAD_PASILLO
    },
    MITAD_PASILLO: {
        'S': VESTIBULO,
        'E': BIBLIOTECA,
        'O': COCINA,
    },
    BIBLIOTECA: {
        'O': MITAD_PASILLO,
    },
    COCINA: {
        'E': MITAD_PASILLO,
    },
}

def localidad(ident):
    return _localidades[ident]

def corta(loc):
    return loc[DESC_CORTA]

def larga(loc):
    return loc[DESC_LARGA]

def salida_hacia(localidad_actual, verbo):
    salidas = _conexiones[localidad_actual]
    return salidas.get(verbo)
