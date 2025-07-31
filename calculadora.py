# Calculadora simples

# Solicita o primeiro número
num1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número
num2 = float(input("Digite o segundo número: "))

# Solicita a operação
operador = input("Digite a operação (+, -, *, /): ")

# Verifica a operação e faz o cálculo
if operador == "+":
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro: divisão por zero.")
else:
    print("Operador inválido.")
