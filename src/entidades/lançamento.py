from entidades.agência_publicidade import get_agências_publicidade
from entidades.montadora import get_montadoras

lançamentos = []

def get_lançamentos(): return lançamentos

def criar_lançamento(nome_montadora, marca_modelo_veículo, nome_agência_publicidade, data):
    montadora = get_montadoras()[nome_montadora]
    if montadora is None:
        print('Montadora' + nome_montadora + ' não cadastrada')
        return
    veículo = montadora.veículos[marca_modelo_veículo]
    if veículo is None:
        print('Veículo '+ marca_modelo_veículo + ' não cadastrado na montadora' + nome_montadora)
        return
    agência_publicidade = get_agências_publicidade()[nome_agência_publicidade]
    if agência_publicidade is None:
        print('Agência de Publicidade ' + nome_agência_publicidade + ' não cadastrada')
        return
    lançamento = Lançamento(montadora, veículo, agência_publicidade, data)
    if lançamento not in lançamentos: lançamentos.append(lançamento)
    else: print('Lançamento de Veículo já tem cadastro ---' + str(lançamento))

def selecionar_lançamentos(data_mínima_lançamento = None, potência_mínima_veículo = None, ranking_máximo_avaliação_agência_publicidade = None, país_origem_montadora = None):
    filtros = '\nFiltros -- '
    if data_mínima_lançamento is not None: filtros += 'data mínima de lançamento: ' + str(data_mínima_lançamento)
    if potência_mínima_veículo is not None: filtros += ' - potência mínima do veículo: ' + str(potência_mínima_veículo)
    if ranking_máximo_avaliação_agência_publicidade is not None:
        filtros += ('\n - ranking máximo de avaliação da agência de publicidade: ' + str(ranking_máximo_avaliação_agência_publicidade))
    if país_origem_montadora is not None: filtros += (' - país de origem da montadora: ' + país_origem_montadora)
    lançamentos_selecionados = []
    for lançamento in lançamentos:
        if data_mínima_lançamento is not None and lançamento.data < data_mínima_lançamento: continue
        if potência_mínima_veículo is not None and lançamento.veículo.potência < potência_mínima_veículo: continue
        if (ranking_máximo_avaliação_agência_publicidade is not None and lançamento.agência_publicidade.ranking_avaliação > ranking_máximo_avaliação_agência_publicidade): continue
        if país_origem_montadora is not None and lançamento.montadora.país_origem != país_origem_montadora: continue
        lançamentos_selecionados.append(lançamento)
    return filtros, lançamentos_selecionados

class Lançamento:
    def __init__(self, montadora, veículo, agência_publicidade, data):
        self.montadora = montadora
        self.veículo = veículo
        self.agência_publicidade = agência_publicidade
        self.data = data

    def __str__(self):
        formato = '{}{:<20}{}{:<19}{}{:<10}{}{:<10}{}'
        lançamento_formatado = formato.format('|', self.montadora.nome, '|', self.veículo.marca_modelo, '|', self.agência_publicidade.nome, '|', str(self.data), '|')
        return lançamento_formatado

    def str_filtro(self):
        formato = '{:>2} {} {:>14} {} {:<3} {}'
        filtro_formatado = formato.format(str(self.agência_publicidade.ranking_avaliação), '|', self.montadora.país_origem,'|', f'{self.veículo.potência:3d}' + ' cv', '|')
        return self.__str__() + filtro_formatado