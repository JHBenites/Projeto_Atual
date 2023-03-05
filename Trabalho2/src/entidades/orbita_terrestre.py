class OrbitaTerrestre:
    def __init__(self, passageiros_maximo, numero_de_orbitas, mobilidade_extraveicular):
        self.numero_de_orbitas = numero_de_orbitas if 1 <= numero_de_orbitas <= 6 else -1
        self.passageiros_maximo = passageiros_maximo
        self.mobilidade_extraveicular = mobilidade_extraveicular

    def __str__(self):
        return 'Número máximo de passageiros: ' + self.passageiros_maximo + \
            ' - Número de Órbitas: ' + str(self.numero_de_orbitas) +\
            str(self.__to_str_mobilidade_extraveicular__())

    def __to_str_mobilidade_extraveicular__(self):
        if not self.mobilidade_extraveicular:
            return ''
        else:
            if self.mobilidade_extraveicular == True:
                return ' - Mobilidade Extraveicular'

orbitas = []

def get_orbitas_terrestre(): return orbitas

def inserir_orbita_terrestre(orbita): orbitas.append(orbita)

def selecionar_orbita_terrestre(empresa=None, mobilidade_extraveicular=None, numero_de_orbitas=None):
    filtros = 'Filtros: '
    if empresa != None: filtros += 'empresa: ' + empresa
    if mobilidade_extraveicular:
        filtros += ' - mobilidade_extraveicular'
    elif mobilidade_extraveicular == False:
        filtros += ' - sem mobilidade extraveicular'
    if numero_de_orbitas != None: filtros += ' - número de orbitas: ' \
                                             + str(numero_de_orbitas)
    orbitas_selecionados = []
    for orbita in orbitas:
        if empresa != None and orbita.empresa != empresa: continue
        if numero_de_orbitas != None and orbita.numero_de_orbitas != numero_de_orbitas: continue
        if mobilidade_extraveicular in (True, False) and orbita.mobilidade_extraveicular \
                != mobilidade_extraveicular: continue
        orbitas_selecionados.append(orbita)
    return filtros, orbitas_selecionados
