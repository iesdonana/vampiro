from coleccion import Coleccion

class Item:
    def __init__(self, nombre, descripcion, sustantivo):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__sustantivo = sustantivo

    def sustantivo(self):
        return self.__sustantivo

class Contenedor(Item):
    def __init__(self, nombre, descripcion, sustantivo):
        super().__init__(nombre, descripcion, sustantivo)
        self.__contenido = Coleccion()

    def meter_item(self, item):
        self.__contenido.set_elemento(item.sustantivo(), item)

    def sacar_item(self, sustantivo):
        self.__contenido.del_elemento(sustantivo)
