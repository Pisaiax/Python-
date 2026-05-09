import random

opcoes = ['pedra', 'tesoura', 'papel']
computador = random.choice(opcoes)
escolha = input('Escolha: ')


def jogo(escolha, computador):
    if escolha == 'pedra' and computador == 'tesoura':
        print('Você ganhou')
    elif escolha == 'papel' and computador == 'tesoura':
        print('Você perdeu')
    elif escolha == 'pedra' and computador == 'papel':
        print('Você perdeu')
    elif escolha == computador:
        print('Empate')

jogo(escolha, computador)