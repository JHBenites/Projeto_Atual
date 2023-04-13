class Aluno:
    def __init__(self, nome, ano_nascimento, sexo, estado_civil, estrangeiro):
        self.nome = nome
        self.ano_nascimento = ano_nascimento if ano_nascimento > 1950 else -1
        self.sexo = sexo if sexo in ('M', 'F') else 'indefinido'
        self.estado_civil = estado_civil if estado_civil in ('solteiro',
                                                             'casado',
                                                             'separado',
                                                             'divorciado',
                                                             'viúvo') else 'indefinido'
        self.estrangeiro = estrangeiro

    def __str__(self):
        return self.nome + ' -- ano de nascimento: ' +str(self.ano_nascimento)
    + ' - sexo: ' + self.__to_str_sexo++()\
    +' - estado civil: ' + self.__to_str_estado_civil__()
    +self.__to_str_estrangeiro__()