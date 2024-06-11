agências_publicidade = {}

def get_agências_publicidade(): return agências_publicidade

def inserir_agência_publicidade(agência_publidade):
    nome_agência_publicidade = agência_publidade.nome
    if nome_agência_publicidade not in agências_publicidade.keys():
        agências_publicidade[nome_agência_publicidade] = agência_publidade
        return True
    else:
        print('Agência de Publicidade '+ nome_agência_publicidade + ' já tem cadastro')
        return False
class AgênciaPublicidade:
    def __init__(self, nome, país_origem, ranking_avaliação):
        self.nome = nome
        self.país_origem = país_origem
        self.ranking_avaliação = ranking_avaliação

    def __str__(self):
        formato = '{}{:<10}{}{:<14}{}{:<1}{}'
        agência_publicidade_formatada = formato.format('|', self.nome, '|', self.país_origem, '|', str(self.ranking_avaliação), '|')
        return agência_publicidade_formatada

# def selecionar_agências_publicidade(ranking_máximo_avaliação=None, país_origem=None, prefixo_nome=None):
#     filtros = '\nFiltros --'
#     if ranking_máximo_avaliação is not None: filtros += 'ranking máximo de avaliação' + str(ranking_máximo_avaliação)
#     if país_origem is not None: filtros += ' - país de origem: ' + str(país_origem)
#     if prefixo_nome is not None: filtros += ' - prefixo do nome: ' + prefixo_nome
#     agências_publicidade_selecionadas = []
#     for agência_publicidade in agências_publicidade:
#         if ranking_máximo_avaliação is not None and agência_publicidade.ranking_avaliação > ranking_máximo_avaliação: continue
#         if país_origem is not None and agência_publicidade.país_origem != país_origem: continue
#         if prefixo_nome is not None and not agência_publicidade.nome.startswith(prefixo_nome): continue
#         agências_publicidade_selecionadas.append(agência_publicidade)
#     return filtros, agências_publicidade_selecionadas