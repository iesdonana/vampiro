from localidad import Localidad

vestibulo = Localidad('VESTÍBULO', 'Estás en el vestíbulo del castillo.')
pasillo = Localidad('PASILLO', 'Te encuentras en el pasillo...')
cocina = Localidad('COCINA', 'Estás en la cocina...')
biblioteca = Localidad('BIBLIOTECA', 'La biblioteca del castillo...')

vestibulo.set_conexiones({
    'NORTE': pasillo
})

pasillo.set_conexiones({
    'SUR': vestibulo,
    'ESTE': biblioteca,
    'OESTE': cocina
})

cocina.set_conexiones({
    'ESTE': pasillo
})

biblioteca.set_conexiones({
    'OESTE': pasillo
})
