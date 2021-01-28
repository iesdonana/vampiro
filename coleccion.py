"""
TAD Coleccion: colección de elementos a los que se puede acceder
               a través de un identificador o etiqueta.

- Generadora:
    - coleccion() -> Coleccion

- Selectora:
    - elemento(c: Coleccion, k: Clave) -> Elemento

- Mutadoras:
    - insertar(c: Coleccion, k: Clave, e: Elemento)
    - quitar(c: Coleccion, k: Clave)
"""

def coleccion():
    """Devuelve una colección vacía."""
    return {}

def elemento(c, k):
    """
    Devuelve el elemento cuya clave es k de la colección c.

    Lanza una excepción KeyError si la clave k no está en c.
    """
    return c[k]

def insertar(c, k, e):
    """
    Inserta en la colección c el elemento e con la clave k.

    Lanza una excepción KeyError si la clave k ya existe en c.
    """
    if k in c:
        raise KeyError('La clave ya existe en la colección.')
    c[k] = e

def quitar(c, k):
    """
    Quita de la colección c el elemento con clave k.

    Lanza una excepción KeyError si la clave k no existe en c.
    """
    del c[k]
