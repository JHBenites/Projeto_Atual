from entidades.cliente import clientes
from entidades.empresa import empresas

agendamentos = []

def get_agendamentos(): return agendamentos

def inserir_agendamento(cpf_cliente, empresa, data):
    cliente =