class Token:
    __tokens = {}

    def __init__(self, lexemas):
        self.__ident = lexemas[0]
        for lexema in lexemas:
            Token.__tokens[lexema] = self

    def __repr__(self):
        return self.__ident

class Verbo(Token):
    pass

class Direccion(Verbo):
    pass

class Nombre(Token):
    pass

"""
class Vocabulario:
    palabras = {}

    def __init__(self, dic):
        self.__voc = {}
        for token, palabras in dic.items():
            for palabra in palabras:
                self.__voc[palabra] = token

    def token(self, palabra):
        return self.__voc.get(palabra)

    @staticmethod
    def es_direccion(palabra: Token):
        return isinstance(palabra, Direccion)
"""

COGER = Verbo(['COGER', 'COGE', 'TOMAR', 'TOMA'])
DEJAR = Verbo(['DEJAR', 'DEJA'])
NORTE = Direccion(['NORTE', 'N'])
SUR = Direccion(['SUR', 'S'])
ESTE = Direccion(['ESTE', 'E'])
OESTE = Direccion(['OESTE', 'O'])
ARRIBA = Direccion(['ARRIBA', 'SUBIR'])
ACABAR = Verbo(['ACABAR', 'TERMINAR', 'FIN'])
TRAJE = Nombre(['TRAJE'])
CUCHILLO = Nombre(['CUCHILLO'])

"""
verbos = Vocabulario({
    COGER: ['COGER', 'COGE', 'TOMAR', 'TOMA'],
    DEJAR: ['DEJAR', 'DEJA'],
    NORTE: ['NORTE', 'N'],
    SUR: ['SUR', 'S'],
    ESTE: ['ESTE', 'E'],
    OESTE: ['OESTE', 'O'],
    ACABAR: ['ACABAR', 'FIN', 'TERMINAR'],
})

nombres = Vocabulario({
    TRAJE: ['TRAJE'],
    CUCHILLO: ['CUCHILLO', 'NAVAJA'],
})
"""
