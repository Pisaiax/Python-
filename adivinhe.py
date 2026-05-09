import random

numero = random.randint(1, 10)

while True:
    escolha = input('Adivinhe o número (1 a 10): ')

    if int(escolha) == numero:
        print('Acertou')
        break
    else:
        print('Não acertou')