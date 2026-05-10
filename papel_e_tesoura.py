import random

opcoes = ["pedra", "tesoura", "papel"]


def jogo(escolha, computador):
    print(f"Computador escolheu: {computador}")

    if escolha not in opcoes:
        print("Opção inválida!")
    elif escolha == computador:
        print("Empate!")
    elif (
        (escolha == "pedra" and computador == "tesoura")
        or (escolha == "tesoura" and computador == "papel")
        or (escolha == "papel" and computador == "pedra")
    ):
        print("Você ganhou!")
    else:
        print("Você perdeu!")


while True:
    computador = random.choice(opcoes)
    escolha = input("\nEscolha (pedra/tesoura/papel): ").lower()
    jogo(escolha, computador)

    continuar = input("Jogar novamente? (S/N): ").upper()
    if continuar == "N":
        break
