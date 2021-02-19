class Token:
    def __init__(self, ident):
        self.__ident = ident

    def __repr__(self):
        return self.__ident

class Vocabulario:
    def __init__(self, dic):
        self.__voc = {}
        for token, palabras in dic.items():
            for palabra in palabras:
                self.__voc[palabra] = token

    def token(self, palabra):
        return self.__voc.get(palabra)


PALABRA_VERBO = 0
PALABRA_NOMBRE = 1

TIPO_PALABRA = 0
SIGNIF_PALABRA = 1

# Significados:
COGER = 0
DEJAR = 1
TRAJE = 2
CUCHILLO = 3

palabras = [
    ['COGER', PALABRA_VERBO, COGER],
    ['COGE', PALABRA_VERBO, COGER],
    ['DEJAR', PALABRA_VERBO, DEJAR],
    ['TRAJE', PALABRA_NOMBRE, TRAJE],
    ['CUCHILLO', PALABRA_NOMBRE, CUCHILLO],
    ['NAVAJA', PALABRA_NOMBRE, CUCHILLO],
    ['N', PALABRA_VERBO],
    ['S', PALABRA_VERBO],
    ['E', PALABRA_VERBO],
    ['O', PALABRA_VERBO],
    ['LLAVE', PALABRA_NOMBRE],
    ['FIN', PALABRA_VERBO],
    ['ACABAR', PALABRA_VERBO],
]

_coger = {
    TIPO_PALABRA: PALABRA_VERBO,
    SIGNIF_PALABRA: COGER,
}

_cuchillo = {
    TIPO_PALABRA: PALABRA_NOMBRE,
    SIGNIF_PALABRA: CUCHILLO,
}

palabras = {
    'COGER': _coger,
    'COGE': _coger,
    'CUCHILLO': _cuchillo,
    'NAVAJA': _cuchillo,
}

def es_direccion(verbo):
    return verbo in ['N', 'S', 'E', 'O']
