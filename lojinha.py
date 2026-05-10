opcoes = [
    {"nome": "tenis", "valor": 100.00},
    {"nome": "cordao", "valor": 100.00},
]

saldo = 300.00


def comprar(escolher):
    global saldo
    for item in opcoes:
        if item["nome"] == escolher:
            if saldo >= item["valor"]:
                saldo -= item["valor"]
                print(f"Comprado! Saldo restante: R$ {saldo:.2f}")
            else:
                print("Saldo insuficiente!")
            return
    print("Produto inválido!")


while True:
    print("\n--- Produtos ---")
    for item in opcoes:
        print(f'{item["nome"]} - R$ {item["valor"]:.2f}')
    print(f"Saldo: R$ {saldo:.2f}")

    escolher = input("Digite o produto: ").lower()
    comprar(escolher)

    continuar = input("Deseja continuar? (S/N): ").upper()
    if continuar == "N":
        break

print("Obrigado pela compra!")
