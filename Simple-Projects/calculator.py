while True:
    operacao = input("Qual é a operação que você deseja fazer? (x, +, -, /) ")
    num1 = float(input("Digite um numero "))
    num2 = float(input("Digite outro numero "))

    if operacao == "x":
        print(num1 * num2)
    elif operacao == "+":
        print(num1 + num2)
    elif operacao == "-":
        print(num1 - num2)
    elif operacao == "/":
        print(num1 / num2)
    else:
        print("Operação invalida! (tente sem acentos)")

    continuar = input("Deseja continuar? (sim ou nao) ")
    if continuar == "sim":
        continue
    else:
        print("Obrigado por usar a calculadora!")
    break

