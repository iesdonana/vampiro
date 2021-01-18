import interprete

while True:
    orden = input('> ')
    interprete.interpretar(orden)
    if interprete.hay_error_sintactico():
        print('No entiendo lo que quieres decirme.')
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
