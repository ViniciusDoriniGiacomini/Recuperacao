num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")
sinal = input("Digite o operador(+, -, *, /): ")

if sinal == "+":
    result = float(num1) + float(num2)
    print("Resultado: ", result)
elif sinal == "-":
    result = float(num1) - float(num2)
    print("Resultado: ", result)
elif sinal == "*":
    result = float(num1) * float(num2)
    print("Resultado: ", result)
elif sinal == "/":
    result = float(num1) / float(num2)
    print("Resultado: ", result)
