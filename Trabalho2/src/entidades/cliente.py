clientes = {}
def get_cliente(): return clientes

def inserir_cliente(cliente):
    cpf_cliente = cliente.cpf
    if cpf_cliente not in clientes.keys(): clientes[cpf_cliente] = cliente
    else: print('Cliente já cadastrado')

class Cliente:
    def __init__(self, nome, peso, cpf, data_nascimento, sexo, endereço):
        self.nome = nome
        self.peso = peso
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.endereço = endereço

    def __str__(self):
        return self.nome + ' - Peso:' + str(self.peso) + ' - CPF:' + self.cpf + ' - nascimento:'\
            +str(self.data_nascimento) + ' - sexo:' + self.__to_str_sexo__()\
            +'\n         - residente em:: ' + str(self.endereço)

    def __to_str_sexo__(self):
        if self.sexo == 'M': return 'masculino'
        elif self.sexo == 'F': return 'feminino'
        else: return 'indefinido'
