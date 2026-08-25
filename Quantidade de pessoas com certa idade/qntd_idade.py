print('-'*30)
print('     Cadastre uma Pessoa')
print('-'*30)
maior18 = homem = mulhermenos20 = 0

while True:
    idade = int(input('Idade: '))
    if idade > 18:
        maior18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]:')).upper().strip()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continua == 'N':
        break
    
print(f'Foram cadastrados {maior18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homem} homens')
print(f'{mulhermenos20} mulheres tem menos de 20 anos')
