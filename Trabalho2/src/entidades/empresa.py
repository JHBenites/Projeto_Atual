empresas = {}

def get_empresa(): return empresas
def inserir_empresa(empresa):
    nome_empresa = empresa.nome
    if nome_empresa not in empresas.keys(): empresas[nome_empresa] = empresa
    else: print('Empresa já cadastrada')

class Empresa:
    def __init__(self, nome, nacionalidade):
        self.nome = nome if nome in ('Virgin Galactic', 'SpaceX', 'Blue Origin', 'Orion Span',
                                              'Space Adventures', 'Zero 2 Infinity') else -1
        self.nacionalidade = nacionalidade
    def __str__(self):
        empresa_str = str(self.nome) + ' de ' + str(self.nacionalidade)
        return empresa_str


