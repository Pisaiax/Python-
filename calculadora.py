while True:
    escolha = input('Deseja continuar?: S or N')
    if escolha.upper() == 'S':
        num1 = input()
        operador = input()
        num2 = input()
    else: 
        break

    def calcular(num1, operador, num2):
        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            return num1 / num2
        elif operador == '%':
            return num1 * num2 / 100
        else:
            print('error..')

    resultado = calcular(float(num1), operador, float(num2))
    print(f'Resultado é: {resultado}')