montadoras = {}

def get_montadoras(): return montadoras

def inserir_montadora(montadora):   #<----------------
    nome_montadora = montadora.nome
    if nome_montadora not in montadoras.keys():
        montadoras[nome_montadora] = montadora
        return True
    else:
        print('Montadora ' + nome_montadora + ' já tem cadastro')
        return False

class Montadora:

    def __init__(self, nome, país_origem, sede_maior_fábrica_brasil):
        self.nome = nome
        self.país_origem = país_origem
        self.sede_maior_fábrica_brasil = sede_maior_fábrica_brasil
        self.veículos = {}                  #<-------------

    def __str__(self):
        formato = '{} {:<20} {} {:<14} {} {:<17} {}'
        montadora_formatada = formato.format('|', self.nome, '|', self.país_origem, '|', self.sede_maior_fábrica_brasil, '|')
        return montadora_formatada
    def inserir_veículo(self, veículo):
        marca_modelo_veículo = veículo.marca_modelo
        if marca_modelo_veículo not in self.veículos.keys(): self.veículos[marca_modelo_veículo] = veículo
        else:
            print('Veículo' + marca_modelo_veículo + ' já tem cadastro na Montadora')
