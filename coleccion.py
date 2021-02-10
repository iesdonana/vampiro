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

class Coleccion:
    def __init__(self):
        """Inicializa la colección."""
        self.__coleccion = {}

    def elemento(self, k):
        """
        Devuelve el elemento cuya clave es k.

        Lanza una excepción KeyError si la clave k no está.
        """
        return self.__coleccion[k]

    def set_elemento(self, k, e):
        """
        Inserta el elemento e con la clave k.
        """
        self.__coleccion[k] = e

    def del_elemento(self, k):
        """
        Quita de la colección elemento con clave k.

        Lanza una excepción KeyError si la clave k no existe.
        """
        del self.__coleccion[k]
