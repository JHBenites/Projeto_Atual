empresas = {}

def inserir_empresa(empresa):
    nome_empresa = empresa.nome
    if nome_empresa not in empresas.keys(): empresas[nome_empresa] = empresa
    else: print('Empresa já cadastrada')

class Empresa:
    def __init__(self, nome, nacionalidade, mobilidade_extraveicular):
        self.nome = nome if nome in ('Virgin Galactic', 'SpaceX', 'Blue Origin', 'Orion Span',
                                              'Space Adventures', 'Zero 2 Infinity') else -1
        self.nacionalidade = nacionalidade
        self.mobilidade_extraveicular = mobilidade_extraveicular
    def __str__(self):
        empresa_str = self.nome + ' de ' + self.nacionalidade +\
            str(self.__to_str_mobilidade_extraveicular__())
        return empresa_str


