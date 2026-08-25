saldo = 1000
somadep = sacar = quant = 0
novsaldo = 0
saldonovo = ' '

while True:
    print('''
[1] Consultar saldo
[2] Depositar
[3] Sacar
[4] Sair''')
    menu = int(input('Digite um valor para acessar o menu:'))
    if menu == 1:
        if somadep < saldo:
            print(f'Voce tem R${saldo} reais de saldo')
            quant += 1
        if somadep > saldo:
            print(f'Seu novo saldo é de R${somadep} reais')
            quant += 1
    if menu == 2:
        dep = float(input('Quanto você quer depositar? '))
        somadep = dep + saldo
        quant += 1
        print(
            f'Voce depositou R${dep} reais e seu novo saldo é de R${somadep} reais')
    if menu == 3:
        sac = float(input('Quanto você quer sacar?'))
        if somadep > sac:
            novsaldo = somadep - sac
            quant += 1
            print(
                f'Seu saldo é R${somadep} reais e você sacou R${sac} reais. seu novo saldo é de R${novsaldo} reais')
            if sac > somadep:
                print('Saldo insuficiente')
