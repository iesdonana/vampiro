VESTIBULO = 0
MITAD_PASILLO = 1
COCINA = 2
BIBLIOTECA = 3

localidades = {
    VESTIBULO: ['Estás en el vestíbulo del castillo.', 'VESTÍBULO'],
    MITAD_PASILLO: ['Estás en mitad del pasillo.', 'MITAD PASILLO'],
    COCINA: ['Estás en la cocina.', 'COCINA'],
    BIBLIOTECA: ['Estás en la biblioteca.', 'BIBLIOTECA'],
}

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
