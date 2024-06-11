#1 etapa
#veículos = {}

#def get_veículos(): return veículos

#def inserir_veículo(veículo): veículos.append(veículo)
#-----------------------------------------------------------------------
class Veículo:
    def __init__(self, marca_modelo, alimentação, potência, importado):
        self.marca_modelo = marca_modelo
        self.alimentação = alimentação if alimentação in ('flex', 'diesel', 'elétrico') else 'indefinida'
        self.potência = potência
        self.importado = importado

    def __str__(self):
        if self.importado: importado_str = 'importado |'
        else: importado_str = ''
        formato = '{}{:<19}{}{:<8}{}{:<6}{}{}'
        veículo_formatado = formato.format('|', self.marca_modelo, '|', self.alimentação, '|', f'{self.potência:3d}' + ' cv', '|',
                                           importado_str)
        return veículo_formatado

# def selecionar_veículos(importado=None, alimentação=None, potência_máxima=None):
#     filtros = '\nFiltros --'
#     if importado: filtros += 'importado'
#     elif importado == False: filtros += 'nacional'
#     if alimentação is not None: filtros += ' - alimentação: ' + alimentação
#     if potência_máxima is not None: filtros += ' - potência máxima:' + str(potência_máxima)
#     veículos_selecionados = []
#     for veículo in veículos:
#         if importado in (True, False) and veículo.importado != importado: continue
#         if alimentação is not None and veículo.alimentação != alimentação: continue
#         if potência_máxima is not None and veículo.potência > potência_máxima: continue
#         veículos_selecionados.append(veículo)
#     return filtros, veículos_selecionados