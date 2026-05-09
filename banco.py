saldo = 0.0
senha = ''


def depositar():
    global saldo
    valor = float(input('Quanto deseja depositar? '))
    saldo += valor
    print(f'Depositado! Saldo atual: R${saldo}')

def sacar():
    global saldo
    valor = float(input('Quanto quer sacar?'))
    if valor > saldo: 
        print('Saldo pouco, pobre!')
    else:
        saldo -= valor
        print(f'Saldo {saldo}')

def ver_saldo():
    print(f'R$: {saldo}')

while True:
    print('\n1 - Depositar')
    print('2 - Sacar')
    print('3 - Ver saldo')
    print('4 - Sair')

    escolha = input('Qual deseja?: ')

    if escolha == '1':
        depositar()
    elif escolha == '2':
        pergunta = input('Senha: ')
        if pergunta == senha:
            sacar()
    elif escolha == '3':
        ver_saldo()
    elif escolha == '4':
        break
    else: 
        print('Acapotemo o corsa')