import interprete
import jugador

jugador.describe_localidad_actual()

while True:
    orden = input('> ')
    interprete.interpretar(orden)
    if interprete.hay_error_sintactico():
        print('No entiendo lo que quieres decirme.')
    elif interprete.verbo_es_direccion():
        if not jugador.intentar_mover(interprete.verbo()):
            print('No hay salida en esa dirección.')
    elif interprete.verbo() in ['FIN', 'ACABAR']:
        if interprete.nombre() is None:
            print('Hasta luego, Lucas.')
            break
        else:
            print('No entiendo lo que quieres decirme')
    else:
        print('Verbo:', interprete.verbo())
        print('Nombre:', interprete.nombre())
