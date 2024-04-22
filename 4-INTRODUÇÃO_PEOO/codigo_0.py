nome = input('Insira seu nome: ')
matricula = input('Insira sua matrícula: ')
ano = matricula[0:4]
semestre = matricula[5]
curso = matricula[6:10]
contador = matricula[11:14]
print(f'Nome: {nome}')
print(f'Matrícula: {matricula}')
print(f'Ano de Ingresso no IFRN: {ano}')