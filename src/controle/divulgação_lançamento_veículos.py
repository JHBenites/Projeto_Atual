from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from util.data import Data
from entidades.agência_publicidade import inserir_agência_publicidade, AgênciaPublicidade, get_agências_publicidade
from entidades.veículo import Veículo
from entidades.montadora import inserir_montadora, Montadora, get_montadoras
from entidades.lançamento import criar_lançamento, get_lançamentos, selecionar_lançamentos
def cadastrar_agências_publicidade():
    inserir_agência_publicidade(AgênciaPublicidade(nome='BETC Havas', país_origem='França', ranking_avaliação=1))
    inserir_agência_publicidade(AgênciaPublicidade('Galeria', 'Brasil', 2))
    inserir_agência_publicidade(AgênciaPublicidade('Artplan', 'Brasil', 3))
    inserir_agência_publicidade(AgênciaPublicidade('McCann', 'Estados Unidos', 4))
    inserir_agência_publicidade(AgênciaPublicidade('Africa', 'Estados Unidos', 5))

#etapa 1
#------------------------------------------------------------------------------------------------------------
# def cadastrar_veículos():
#     inserir_veículo(Veículo(marca_modelo='Hyundai HB20', alimentação='flex', potência=80, importado=False))
#     inserir_veículo(Veículo('Chevrolet Onix Plus', 'flex', 116, False))
#     inserir_veículo(Veículo('Fiat Strada', 'diesel', 130, False))
#     inserir_veículo(Veículo('Fiat Toro', 'diesel', 185, False))
#     inserir_veículo(Veículo('BYD Dolphin', 'elétrico', 95, True))
#     inserir_veículo(Veículo('Volvo XC40', 'elétrico', 231, True))
#     inserir_veículo(Veículo('Volvo FH 540', 'diesel', 540, False))
#     inserir_veículo(Veículo('VW Delivery 11180', 'diesel', 175, False))
#     inserir_veículo(Veículo('DAF XF 530', 'diesel', 530, False))
#     inserir_veículo(Veículo('Volvo FH 460', 'diesel', 460, False))
#------------------------------------------------------------------------------------------------------------

def cadastrar_montadoras():
    montadora = Montadora(nome='Hyundai', país_origem='Coréia do Sul', sede_maior_fábrica_brasil='Piracicaba - SP')
    inserir_montadora(montadora)
    montadora.inserir_veículo(Veículo(marca_modelo='Hyundai HB20', alimentação='flex', potência=80, importado=False))
    montadora = Montadora('GM', 'Estados Unidos', 'São Caetano - SP')
    inserir_montadora(montadora)
    montadora.inserir_veículo(Veículo('Chevrolet Onix Plus', 'flex', 116, False))
    montadora = Montadora('Fiat', 'Itália', 'Betim - MG')
    inserir_montadora(montadora)
    montadora.inserir_veículo(Veículo('Fiat Strada', 'diesel', 130, False))
    montadora.inserir_veículo(Veículo('Fiat Toro', 'diesel', 185, False))
    montadora = Montadora('BYD', 'China', 'Camaçari - BA')
    inserir_montadora(montadora)
    montadora.inserir_veículo(Veículo('BYD Dolphin', 'elétrico', 95, True))
    montadora = Montadora('Volvo', 'Suécia', 'exterior')
    inserir_montadora(montadora)
    montadora.inserir_veículo(Veículo('Volvo XC40', 'elétrico', 231, True))
    montadora = Montadora('Volvo Caminhões', 'Suécia', 'Curitiba - PR')
    inserir_montadora(montadora)
    montadora.inserir_veículo(Veículo('Volvo FH 540', 'diesel', 540, False))
    montadora.inserir_veículo(Veículo('Volvo FH 460', 'diesel', 460, False))
    montadora = Montadora('Volkswagen Caminhões', 'Alemanha', 'Resende - RJ')
    inserir_montadora(montadora)
    montadora.inserir_veículo(Veículo('VW Delivery 11180', 'diesel', 175, False))
    montadora = Montadora('DAF', 'Holanda', 'Ponta Grossa - PR')
    inserir_montadora(montadora)
    montadora.inserir_veículo(Veículo('DAF XF 530', 'diesel', 530, False))

def cadastrar_lançamentos():
    criar_lançamento(nome_montadora='Hyundai', marca_modelo_veículo='Hyundai HB20', nome_agência_publicidade='Africa', data = Data(dia=1, mês=9, ano=2012))
    criar_lançamento('GM', 'Chevrolet Onix Plus', 'McCann', Data(12,9,2019))
    criar_lançamento('Fiat', 'Fiat Strada', 'Galeria', Data(1, 9, 1998))
    criar_lançamento('Fiat', 'Fiat Toro', 'Galeria', Data(1, 9, 2016))
    criar_lançamento('BYD', 'BYD Dolphin', 'Artplan', Data(28, 6, 2023))
    criar_lançamento('Volvo', 'Volvo XC40', 'BETC Havas', Data(15, 4, 2018))
    criar_lançamento('Volvo Caminhões', 'Volvo FH 540', 'BETC Havas', Data(1, 3, 2014))
    criar_lançamento('Volkswagen Caminhões', 'VW Delivery 11180', 'Artplan', Data(23, 1, 2018))
    criar_lançamento('DAF', 'DAF XF 530', 'Artplan', Data(18, 8, 2020))
    criar_lançamento('Volvo Caminhões', 'Volvo FH 460', 'BETC Havas', Data(17, 4, 2014))

def imprimir_somente_para_alinhar_formatação():
    print('\nMontadoras : nome - país de origem - sede da maior fábrica no Brasil')
    for índice, montadora in enumerate(get_montadoras().values()) : print(montadora)
    print('\nVeículos : marca modelo - alimentação - potência - importado')
    for montadora in get_montadoras().values() :
        for veículo in montadora.veículos.values() : print(veículo)


if __name__ == '__main__':
    cadastrar_agências_publicidade()
    #------------------------------------------------------------------------------------------------------------
    #etapa1
    # cabeçalho = 'Agências de Publicidades : nome - país de origem - ranking de avaliação'
    # imprimir_objetos(cabeçalho='\n' + cabeçalho, objetos=get_agências_publicidade())
    # filtros, agência_publicidades_selecionadas = selecionar_agências_publicidade()
    # imprimir_objetos(cabeçalho, agência_publicidades_selecionadas, filtros)
    # filtros, agência_publicidades_selecionadas = selecionar_agências_publicidade(ranking_máximo_avaliação=3)
    # filtros, agência_publicidades_selecionadas = selecionar_agências_publicidade(ranking_máximo_avaliação=3)
    # filtros, agência_publicidades_selecionadas = selecionar_agências_publicidade(3, país_origem='Brasil', )
    #------------------------------------------------------------------------------------------------------------
    imprimir_objetos(cabeçalho='\nAgências de Publicidades : nome - país de origem - ranking de avaliação',
                     objetos = get_agências_publicidade().values())

    cadastrar_montadoras()
    imprimir_somente_para_alinhar_formatação()
    print('\nMontadoras : nome - país de origem - sede da maior fábrica no Brasil')
    for índice, montadora in enumerate(get_montadoras().values()) :
        imprimir_objeto(índice=índice, objeto_str=str(montadora))
        imprimir_objetos_internos(montadora.veículos.values())
    cadastrar_lançamentos()
    cabeçalho_lançamento = ('Lançamentos : nome da montadora - marca modelo do veículo - nome da agência de publicidade' + ' - data do lançamento')
    imprimir_objetos('\n' + cabeçalho_lançamento, get_lançamentos())
    filtros, lançamentos_selecionados = selecionar_lançamentos()
    cabeçalho_lançamento_filtros = (cabeçalho_lançamento + '\n -- ranking de avaliação da agência de publicidade - país de origem da montadora - potência do veículo')
    imprimir_objetos_associação_filtros(cabeçalho_lançamento_filtros, lançamentos_selecionados, filtros)
    filtros, lançamentos_selecionados = selecionar_lançamentos(data_mínima_lançamento=Data(dia=1, mês=1, ano=2012))
    imprimir_objetos_associação_filtros(cabeçalho_lançamento_filtros, lançamentos_selecionados, filtros)
    filtros, lançamentos_selecionados = selecionar_lançamentos(Data(1, 1, 2012), potência_mínima_veículo=150)
    imprimir_objetos_associação_filtros(cabeçalho_lançamento_filtros, lançamentos_selecionados, filtros)
    filtros, lançamentos_selecionados = selecionar_lançamentos(Data(1, 1, 2012), 150, ranking_máximo_avaliação_agência_publicidade=2)
    imprimir_objetos_associação_filtros(cabeçalho_lançamento_filtros, lançamentos_selecionados, filtros)
    filtros, lançamentos_selecionados = selecionar_lançamentos(Data(1, 1, 2012), 150, 2, país_origem_montadora='Suécia')
    imprimir_objetos_associação_filtros(cabeçalho_lançamento_filtros, lançamentos_selecionados, filtros)

