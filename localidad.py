class Localidad:
    def __init__(self, corta, larga):
        self.set_corta(corta)
        self.set_larga(larga)

    def corta(self):
        return self.__corta

    def set_corta(self, corta):
        self.__corta = corta

    def larga(self):
        return self.__larga

    def set_larga(self, larga):
        self.__larga = larga

    def conexiones(self):
        return self.__conexiones

    def set_conexiones(self, conexiones):
        self.__conexiones = conexiones
