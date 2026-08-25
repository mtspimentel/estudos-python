aluno = {}
aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input('A media foi de: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'  #Adiciona à aluno a situação
elif 5 >= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 30)

for k, v in aluno.items():
    print(f'- {k} é igual a {v}') #Mostra o keys e values (nome, média, situação) -> (nome e media q digitado e a situação)
