from entidades.cliente import clientes
from entidades.empresa import empresas

agendamentos = []

def get_agendamentos(): return agendamentos

def inserir_agendamento(cpf_cliente, empresa_nome, mobilidade_extraveicular, data, vaga, numero_orbitas):
    cliente = clientes[cpf_cliente]
    empresa = empresas[empresa_nome]
    if cliente == None:
        print('Erro: Cliente não cadastrado')
        return
    if empresa == None:
        print('Erro: Empresa não cadastrada')
        return
    agendamento = Agendamento(cliente, empresa, mobilidade_extraveicular, data, vaga, numero_orbitas)
    if agendamento not in agendamentos: agendamentos.append(agendamento)
    else: print('Agendamento já cadastrado --- ' + str(agendamento))

def selecionar_agendamentos(mobilidade_extraveicular = None, peso=None,
                            nacionalidade_empresa = None, vagas = None):
    filtros = 'Filtros: '
    if vagas != None: filtros += 'Vagas: ' + vagas
    if mobilidade_extraveicular == True :
        filtros += ' - com mobilidade extraveicular'
    elif mobilidade_extraveicular == False :
        filtros += ' - sem mobilidade extraveicular'
    if nacionalidade_empresa != None : filtros += ' sede em: ' + nacionalidade_empresa
    if peso != None: filtros += 'Peso: ' + peso
    agendamentos_selecionados = []
    for agendamento in agendamentos:
        if peso != None and agendamento.cliente.peso != peso: continue
        if mobilidade_extraveicular != None and agendamento.mobilidade_extraveicular != mobilidade_extraveicular:\
            continue
        if nacionalidade_empresa != None and agendamento.empresa.nacionalidade != nacionalidade_empresa: continue
        if vagas != None and agendamento.vagas != vagas: continue
        agendamentos_selecionados.append(agendamento)
    return filtros, agendamentos_selecionados


class Agendamento:
    def __init__(self, cliente, empresa, mobilidade_extraveicular, data, vagas, numero_orbitas):
        self.cliente = cliente
        self.empresa = empresa
        self.mobilidade_extraveicular = mobilidade_extraveicular
        self.data = data
        self.vagas = vagas
        self.numero_orbitas = numero_orbitas
    def __str__(self):
        agendamento_str = 'Agendamento do cliente:: ' + str(self.cliente) + 'com a empresa: ' +\
            str(self.empresa) + ' em ' + str(self.vagas) + ' vagas ' + ' no dia: ' + str(self.data) +\
            ' N° de orbitas: ' + str(self.numero_orbitas)+\
            self.__to_str_mobilidade_extraveicular__()
        return agendamento_str

    def __to_str_mobilidade_extraveicular__(self):
        if not self.mobilidade_extraveicular:
            return ''
        else:
            if self.mobilidade_extraveicular == True:
                return ' -com Mobilidade Extraveicular'