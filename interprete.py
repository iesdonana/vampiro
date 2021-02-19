"""
Se encarga de todo lo relacionado con la interpretación de la
entrada del jugador.

El módulo almacena el último verbo y el último nombre reconocidos.

El análisis de la entrada del jugador se lleva a cabo en la función
interpretar.
"""

import vocabulario as voc

class Interprete:
    __verbo = None
    __nombre = None

    @staticmethod
    def verbo():
        """
        Devuelve el último verbo reconocido.

        Args:
            - No tiene

        Returns:
            - El último verbo reconocido, o None si no se
            ha reconocido ninguno.
        """
        return Interprete.__verbo

    @staticmethod
    def nombre():
        """Devuelve el último nombre reconocido."""
        return Interprete.__nombre

    @staticmethod
    def interpretar(orden):
        """
        Interpreta la orden del jugador.

        Args:
            - orden: str => La orden del jugador.

        Returns:
            - None

        Modifica:
            - Las variables globales _verbo y _nombre.
        """
        Interprete.__verbo, Interprete.__nombre = None, None
        lista = orden.upper().split()
        if len(lista) >= 1:
            Interprete.__buscar_verbo_primera_palabra(lista)
        if len(lista) >= 2:
            Interprete.__buscar_nombre_segunda_palabra(lista)

    @staticmethod
    def marcar_error_sintactico():
        Interprete.__verbo = None

    @staticmethod
    def hay_error_sintactico():
        return Interprete.__verbo is None

    @staticmethod
    def verbo_es_direccion():
        return voc.es_direccion(Interprete.__verbo)

    @staticmethod
    def __buscar_verbo_primera_palabra(lista):
        for palabra in voc.palabras:
            if lista[0] == palabra[0]:
                if palabra[1] == voc.VERBO:
                    Interprete.__verbo = lista[0]
                    Interprete.__nombre = None
                elif palabra[1] == voc.NOMBRE:
                    Interprete.marcar_error_sintactico()
                    Interprete.__nombre = None
                break

    @staticmethod
    def __buscar_nombre_segunda_palabra(lista):
        for palabra in voc.palabras:
            if lista[1] == palabra[0]:
                if palabra[1] == voc.NOMBRE:
                    Interprete.__nombre = lista[1]
                else:
                    Interprete.marcar_error_sintactico()
