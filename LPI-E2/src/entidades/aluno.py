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
        return self.nome + ' -- ano de nascimento: ' + str(self.ano_nascimento)\
    + ' - sexo: ' + self.__to_str_sexo__()\
    + ' - estado civil: ' + self.__to_str_estado_civil__() \
    + self.__to_str_estrangeiro__()

    def __to_str_sexo__(self):
        if self.sexo == 'M': return 'masculino'
        elif self.sexo == 'F': return 'feminino'
        else: return 'indefinido'

    def __to_str_estado_civil__(self):
        if self.sexo == 'M': return self.estado_civil
        elif self.sexo == 'F':
            if self.estado_civil != 'indefinido': return self.estado_civil[:-1] + 'a'
            else: return 'indefinido'
        else: return self.estado_civil + '/a'

    def __to_str_estrangeiro__(self):
        if not self.estrangeiro: return ''
        else:
            if self.sexo == 'M': return ' - estrangeiro'
            elif self.sexo == 'F': return ' - estrangeira'
            else: return ' - estrangeiro/a'

alunos = []

def get_alunos(): return alunos

def inserir_aluno(aluno): alunos.append(aluno)