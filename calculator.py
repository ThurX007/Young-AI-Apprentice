while True:
    operacao = input("Qual é a operação que você deseja fazer? multiplicacao, subtracao, soma ou divisao? ")
    num1 = float(input("Digite um numero "))
    num2 = float(input("Digite outro numero "))

    if operacao == "multiplicacao":
        print(num1 * num2)
    elif operacao == "soma":
        print(num1 + num2)
    elif operacao == "subtracao":
        print(num1 - num2)
    elif operacao == "divisao":
        print(num1 / num2)
    else:
        print("Operação invalida! (tente sem acentos)")

    continuar = input("Deseja continuar? (sim ou nao) ")
    if continuar == "sim":
        continue
    else:
        print("Obrigado por usar a calculadora!")
    break

