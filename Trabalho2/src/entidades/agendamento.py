from entidades.cliente import get_cliente
from entidades.empresa import get_empresa
from entidades.orbita_terrestre import OrbitaTerrestre
from util.data import Data

agendamentos = []

def get_agendamentos(): return agendamentos

def inserir_agendamento(cpf_cliente, empresa_nome, data, orbita):
    cliente = get_cliente()[cpf_cliente]
    empresa = get_empresa()[empresa_nome]

    if cliente == None:
        print('Erro: Cliente não cadastrado')
        return
    if empresa == None:
        print('Erro: Empresa não cadastrada')
        return
    agendamento = Agendamento(cliente, empresa, data, orbita)
    if agendamento not in agendamentos: agendamentos.append(agendamento)
    else: print('Agendamento já cadastrado --- ' + str(agendamento))

def selecionar_agendamentos(sede_empresa = None, peso=None, mobilidade_extraveicular=None, data = None):
    filtros = 'Filtros: '
    if mobilidade_extraveicular == True :
        filtros += ' - com mobilidade extraveicular'
    elif mobilidade_extraveicular == False :
        filtros += ' - sem mobilidade extraveicular'
    if sede_empresa != None : filtros += ' sede em: ' + sede_empresa
    if peso != None: filtros += ' Peso: ' + str(peso)
    agendamentos_selecionados = []
    for agendamento in agendamentos:
        if peso != None and agendamento.cliente.peso > peso: continue
        if sede_empresa != None and agendamento.empresa.sede != sede_empresa: continue
        if data != None and agendamento.data.__lt__(data) : continue
        agendamentos_selecionados.append(agendamento)
    return filtros, agendamentos_selecionados


class Agendamento:
    def __init__(self, cliente, empresa, orbita_terrestre, data):
        self.cliente = cliente
        self.empresa = empresa
        self.data = data
        self.orbita_terrestre = orbita_terrestre
    def __str__(self):
        agendamento_str = 'Agendamento do cliente:: ' + str(self.cliente) + 'com a empresa: ' +\
            str(self.empresa) + ' em orbita terrestre ' + str(self.orbita_terrestre) + ' no dia: ' + str(self.data)
        return agendamento_str
