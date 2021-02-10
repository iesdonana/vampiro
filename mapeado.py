from localidad import Localidad
from coleccion import Coleccion
from conexion import Conexion

vestibulo = Localidad('VESTÍBULO', 'Estás en el vestíbulo del castillo.')
pasillo = Localidad('PASILLO', 'Te encuentras en el pasillo...')

al_pasillo = Conexion('NORTE', pasillo)
al_vestibulo = Conexion('SUR', vestibulo)

cs1 = Coleccion()
cs1.set_elemento(al_pasillo)

cs2 = Coleccion()
cs2.set_elemento(al_vestibulo)

vestibulo.set_conexiones(cs1)
pasillo.set_conexiones(cs2)
