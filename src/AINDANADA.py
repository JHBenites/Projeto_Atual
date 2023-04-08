nome = 'JHONATAN'
print(' '*21, '_'*20)
print(f'Prazer em te conhecer {nome:=^20}!') #no espaço de 20 caracteres eu coloco = nos que não foram usados
print('Prazer em te conhecer {:=>20}'.format(nome)) #centralizado(títulos)
print(f'Prazer em te conhecer{nome:=<20}') #alinhado a direita
print(f'Prazer em te conhecer {nome:20}') #alinhado a esquerda
print(' '*20, '|', '_'*18,'|') #fechamento de quadro com espaços no lugar da frase
print('\n')
n = 1.3333333333333
print(n, end = '') #para não quebrar linha de um print para outro, ou seja retirar o '\n'
print(f'{n:.2f} sem quebra de linha e formatado pra real(float)')

