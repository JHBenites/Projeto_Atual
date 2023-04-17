from entidades.aluno import inserir_aluno, Aluno, get_alunos
def cadastrar_alunos():
    inserir_aluno(Aluno(nome='Ana julia', ano_nascimento=1995, sexo='F', estado_civil='solteiro', estrangeiro=False))
    inserir_aluno(Aluno('Joaquim', 1990, 'M', 'casado', True))
    inserir_aluno(Aluno('Ana Ligia', 1998, 'F', 'solteiro', False))
    inserir_aluno(Aluno('Mateus', 1991, 'M', 'solteiro', False))
    inserir_aluno(Aluno('Livia', 1985, 'F', 'casado', True))
    inserir_aluno(Aluno('Roberto', 1990, 'M', 'casado', False))
    inserir_aluno(Aluno('Ana Maria', 1991, 'F', 'solteiro', False))
    inserir_aluno(Aluno('Sandro', 1992, 'X', 'solteiro', True))

def imprimir_objetos(cabeçalho, objetos, filtros = None):
    if filtros == None: print('\n' + cabeçalho)
    else: print('\n' + cabeçalho + filtros)
    for indice, objeto in enumerate(objetos): print(str(indice + 1)+ ' - ' + str(objeto))

if __name__ == '__main__':
    cadastrar_alunos()
    imprimir_objetos('Alunos Cadastros', get_alunos())