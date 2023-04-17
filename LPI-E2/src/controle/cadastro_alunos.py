from entidades.aluno import inserir_aluno, Aluno, get_alunos
def cadastra_alunos():
    inserir_aluno(Aluno(nome='Ana julia', ano_nascimento=1995, sexo='F', estado_civil='solteiro', estrangeiro=False))
    inserir_aluno(Aluno('Joaquim', 1990, 'M', 'casado', True))
    inserir_aluno(Aluno('Ana Ligia', 1998, 'F', 'solteiro', False))
    inserir_aluno(Aluno('Mateus', 1991, 'M', 'solteiro', False))
    inserir_aluno(Aluno('Livia', 1985, 'F', 'casado', True))
    inserir_aluno(Aluno('Roberto', 1990, 'M', 'casado', False))
    inserir_aluno(Aluno('Ana Maria', 1991, 'F', 'solteiro', False))
    inserir_aluno(Aluno('Sandro', 1992, 'X', 'solteiro', True))

