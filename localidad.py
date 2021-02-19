from coleccion import Coleccion
from conexion import Conexion

class Localidad:
    def __init__(self, corta, larga):
        self.set_corta(corta)
        self.set_larga(larga)
        self.__conexiones = Coleccion()

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
        for direccion, destino in conexiones.items():
            con = Conexion(direccion, destino)
            self.__conexiones.set_elemento(direccion, con)

    def describir(self):
        print(self.corta())
        print(self.larga())

    def salida_hacia(self, verbo):
        try:
            return self.__conexiones.elemento(verbo)
        except KeyError:
            return None
