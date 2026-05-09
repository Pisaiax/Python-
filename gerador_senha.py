import random
import string

def gerar_senha(tamanho):
    cr = string.ascii_letters + string.digits
    password = ''

    for i in range(tamanho):
        password += random.choice(cr)

    return password

while True:
    tamanho = int(input('Digite um tamanho: '))
    print(f'Senha é {gerar_senha(tamanho)}')

    next = input('S or N?').upper()
    if next.startswith('N'):
        break