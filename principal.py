import interprete
import localidades

localidad = localidades.localidades[localidades.actual]
print(localidad[1])
print(localidad[0])

while True:
    orden = input('> ')
    interprete.interpretar(orden)
    if interprete.hay_error_sintactico():
        print('No entiendo lo que quieres decirme.')
    elif interprete.verbo in ['N', 'S', 'E', 'O']:
        se_ha_movido = False
        for c in localidades.conexiones:
            if c[0] == localidades.actual and c[1] == interprete.verbo:
                se_ha_movido = True
                localidades.actual = c[2]
                localidad = localidades.localidades[localidades.actual]
                print(localidad[1])
                print(localidad[0])
                break
        if not se_ha_movido:
            print('No hay salida en esa dirección.')
    elif interprete.verbo == 'FIN':
        if interprete.nombre is None:
            print('Hasta luego, Lucas.')
            break
        else:
            print('No entiendo lo que quieres decirme')
    elif interprete.verbo == 'N':
        pass
    else:
        print('Verbo:', interprete.verbo)
        print('Nombre:', interprete.nombre)
