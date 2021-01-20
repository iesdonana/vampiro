VESTIBULO = 0
MITAD_PASILLO = 1
COCINA = 2
BIBLIOTECA = 3

localidades = {
    VESTIBULO: {
        'corta': 'VESTÍBULO',
        'larga': 'Estás en el vestíbulo del castillo.',
    },
    MITAD_PASILLO: {
        'larga': 'Estás en mitad del pasillo.',
        'corta': 'MITAD PASILLO'
    },
    COCINA: {
        'larga': 'Estás en la cocina.',
        'corta': 'COCINA'
    },
    BIBLIOTECA: {
        'larga': 'Estás en la biblioteca.',
        'corta': 'BIBLIOTECA'
    },
}

def localidad(ident):
    return localidades[ident]

def corta(loc):
    return loc['corta']

def larga(loc):
    return loc['larga']

"""
Cocina --- Mitad pasillo --- Biblioteca
                |
            Vestíbulo
"""

conexiones = [
    (VESTIBULO, 'N', MITAD_PASILLO),
    (MITAD_PASILLO, 'S', VESTIBULO),
    (MITAD_PASILLO, 'E', BIBLIOTECA),
    (BIBLIOTECA, 'O', MITAD_PASILLO),
    (MITAD_PASILLO, 'O', COCINA),
    (COCINA, 'E', MITAD_PASILLO),
]
