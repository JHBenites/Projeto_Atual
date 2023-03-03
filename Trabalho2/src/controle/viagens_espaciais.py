from entidades.orbita_terrestre import inserir_orbita_terrestre, OrbitaTerrestre, \
    get_orbitas_terrestre, selecionar_orbita_terrestre

def inserir():
    inserir_orbita_terrestre(OrbitaTerrestre(empresa='Virgin Galactic', numero_de_orbitas=5,
                                             mobilidade_extraveicular=True))
    inserir_orbita_terrestre(OrbitaTerrestre('SpaceX', 6, True))
    inserir_orbita_terrestre(OrbitaTerrestre('SpaceX', 4, False))
    inserir_orbita_terrestre(OrbitaTerrestre('Blue Origin', 2, False))
    inserir_orbita_terrestre(OrbitaTerrestre('Virgin Galactic', 2, True))
    inserir_orbita_terrestre(OrbitaTerrestre('SpaceX', 2, True))
    inserir_orbita_terrestre(OrbitaTerrestre('Space Adventures', 3, False))

def imprimir_objetos(cabeçalho, objetos, filtros = None):
    if filtros == None: print('\n' + cabeçalho)
    else: print ('\n' + cabeçalho + filtros)
    for índice, objeto in enumerate(objetos): print(str(índice + 1) + ' - ' + str(objeto))

if __name__ == '__main__':
    inserir()
    imprimir_objetos('Órbitas ', get_orbitas_terrestre())
    filtros, orbitas_selecionadas = selecionar_orbita_terrestre()
    imprimir_objetos('Órbitas com ', orbitas_selecionadas, filtros)
    filtros, orbitas_selecionadas = selecionar_orbita_terrestre(empresa='SpaceX')
    imprimir_objetos('Órbitas com ', orbitas_selecionadas, filtros)
    filtros, orbitas_selecionadas = selecionar_orbita_terrestre('SpaceX', mobilidade_extraveicular=True)
    imprimir_objetos('Órbitas com ', orbitas_selecionadas, filtros)
    filtros, orbitas_selecionadas = selecionar_orbita_terrestre('SpaceX', True, numero_de_orbitas=2)
    imprimir_objetos('Órbitas com ', orbitas_selecionadas, filtros)


