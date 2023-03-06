from entidades.cliente import inserir_cliente, Cliente, get_cliente
from entidades.endereço import Endereço
from util.data import Data
from entidades.empresa import inserir_empresa, Empresa, get_empresa
from entidades.agendamento import inserir_agendamento, get_agendamentos, selecionar_agendamentos
def cadastrar_cliente():
    inserir_cliente(Cliente(nome = 'John Carter', peso = 65, cpf = '212.234.571-32',
                            data_nascimento = Data(dia=8, mês=7, ano=1998), sexo = 'M',
                            endereço = Endereço(logradouro = 'Rua Arco Verde', número = '171',
                                                complemento = 'Bloco M Ap 6', bairro = 'Jardim Paulista',
                                                cidade = 'Dourados', cep = '79810-015')))
    inserir_cliente(Cliente('Ana Ligia Silveira', 55, '312.434.775-30', Data(8 , 8, 1982), 'F',
                            Endereço('Rua Chapéu Velho', 303, 'Ap G', 'Rouxinol', 'Glória de Dourados', '79820-017')))
    inserir_cliente(Cliente('Julia Lefevre', 53, '531.331.740-71', Data(30, 4, 1993), 'F',
                            Endereço('Rua Sino da Mata', 589, None, 'Brejão', 'Caarapó', '73100-000')))
    inserir_cliente(Cliente('Viktor Pritchenko', 63, '631.431.740-81', Data(1, 4, 1980), 'M',
                            Endereço('Rua Mata Cuba', 153, None, 'Ipês', 'Monte Alto', '77500-000')))
    inserir_cliente(Cliente('Jorge Lucas', 73, '641.211.720-81', Data(7, 12, 1978), 'M',
                            Endereço('Rua Presidente Vargas', 192, 'Casa B', 'Jeremias de Paula Eduardo',
                                     'Monte Alto', '75520-020')))
def cadastrar_empresas() :
    inserir_empresa(Empresa(nome = 'Virgin Galactic', nacionalidade = 'California'))
    inserir_empresa(Empresa('SpaceX', 'California'))
    inserir_empresa(Empresa('Blue Origin', 'Washington'))
    inserir_empresa(Empresa('Orion Span', 'California'))
    inserir_empresa(Empresa('Space Adventures', 'Virgínia'))
    inserir_empresa(Empresa('Zero 2 Infinity', 'Barcelona'))

def cadastrar_agendamentos():
    inserir_agendamento(cpf_cliente = '212.234.571-32', empresa_nome = 'SpaceX',
                        mobilidade_extraveicular = True, data=Data(dia=15,mês=4,ano=2023), vaga=2, numero_orbitas=1)
    inserir_agendamento('312.434.775-30', 'Orion Span', False, Data(6,3,2023), 1, 3)
    inserir_agendamento('531.331.740-71', 'SpaceX', True, Data(6,7,2023), 4, 2)
    inserir_agendamento('631.431.740-81', 'Blue Origin',True, Data(7,9,2024), 5, 2)
    inserir_agendamento('641.211.720-81', 'Zero 2 Infinity', True, Data(6,3,2023), 1, 1)

def imprimir_objetos(cabeçalho, objetos, filtros = None):
    if filtros == None: print('\n' + cabeçalho)
    else: print ('\n' + cabeçalho + filtros)
    for índice, objeto in enumerate(objetos): print(str(índice + 1) + ' - ' + str(objeto))

if __name__ == '__main__':
    cadastrar_cliente()
    imprimir_objetos('--- Clientes cadastrados', get_cliente().values())
    cadastrar_empresas()
    imprimir_objetos('--- Empresas cadastradas', get_empresa().values())
    cadastrar_agendamentos()
    imprimir_objetos('--- Agendamentos cadastrados', get_agendamentos())
    # filtros, agendamentos_selecionados = selecionar_agendamentos()
    # imprimir_objetos('Agendamento cadastrados', get_agendamentos())
    # filtros, agendamentos_selecionados = selecionar_agendamentos()
    # imprimir_objetos('Agendamentos selecionados com ', agendamentos_selecionados, filtros)
    # filtros, agendamentos_selecionados = selecionar_agendamentos(mobilidade_extraveicular = True )
    # imprimir_objetos('Agendamentos selecionados com ', agendamentos_selecionados, filtros)
    # filtros, agendamentos_selecionados = selecionar_agendamentos(True, nacionalidade_empresa = 'California')
    # imprimir_objetos('Agendamentos selecionados com ', agendamentos_selecionados, filtros)
    # filtros, agendamentos_selecionados = selecionar_agendamentos(True, 'California', sexo = 'F')
    # imprimir_objetos('Agendamentos selecionados com ', agendamentos_selecionados, filtros)
    # filtros, agendamentos_selecionados = selecionar_agendamentos(True,'California', 'F', peso= 65)



