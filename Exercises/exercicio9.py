#===========================Exercicio 9-A==============================
casa = int(input("Qual é o valor da casa? "))
sal = int(input("Qual é o seu salario? "))
temp = int(input("Em quantos anos você vai pagar a casa? "))
per_sal = sal * 0.30
prestacao = casa / (temp * 12)
if prestacao > per_sal:
    print("O emprestimo foi NEGADO!")
else: 
    print(f"O emprestimo foi APROVADO! Você pagará {prestacao:.2f} por mês")

#===========================Exercicio 9-B==============================
num = int(input("Digite um numero inteiro: "))
print("""Escolha uma das bases para a conversão: 
[ 1 ] converter para BINÁRIO 
[ 2 ] converter para OCTAL 
[ 3 ] converter para HEXADECIMAL""")
opcao = int(input("Sua opção: "))
if opcao == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}")
elif opcao == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opcao == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print(f"A opçao {opcao} não existe")

#===========================Exercicio 9-C==============================
num1 = int(input("Digite o 1° numero: "))
num2 = int(input("Digite o 2° numero: "))

if num2 > num1:
    print(f"O numero {num2} é o maior valor e o menor é o {num1}")
elif num1 > num2:
    print(f"O numero {num1} é o maior valor e o menor é o {num2}")
elif num1 == num2:
    print(f"Os numeros {num1} e {num2} tem o mesmo valor")

#===========================Exercicio 9-D==============================
idade = int(input("Digite a sua idade: "))
alistamento = 18

if idade < alistamento:
    print("Você ainda não precisa de alistar")
    print(f"Ainda te restam {alistamento - idade} anos para o alistamento")
elif idade == alistamento:
    print("Você precisa se alistar agora")
else:
    print("Você perdeu o prazo do alistamento")
    print(F"O prazo foi excedido por {idade - alistamento} anos")

#===========================Exercicio 9-E==============================
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
if media <= 5:
    print(f"Reprovado com média {media}")
elif media < 7:
    print(f"Está de recuperação com média {media}")
elif media <= 10:
    print(f"Aprovado com média {media}")
else:
    print(f"O valor da média, {media}, não se encaixa no sistema")

#===========================Exercicio 9-F==============================
ano = int(input("Digite o seu ano de nascimento: "))
if 2026 - ano <= 9:
    print("Você está na categoria MIRIM!")
elif 2026 - ano <= 14:
    print("Você está na categoria INFANTIL!")
elif 2026 - ano <= 19:
    print("Você está na categoria JUNIOR!")
elif 2026 - ano == 20:
    print("Você está na categoria SÊNIOR!")
else:
    print("Você está na categoria MASTER!")

#===========================Exercicio 9-G==============================
peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))
imc = peso / (altura * altura)
if imc <= 18.5:
    print("Você está abaixo do peso")
elif imc <= 25:
    print("Você está no peso ideal")
elif imc <= 30:
    print("Você está com sobrepeso")
elif imc <= 40:
    print("Você está com obesidade")
else:
    print("Você está com obesidade morbida")

#===========================Exercicio 9-H==============================
import random

lista = ["pedra", "papel", "tesoura"]
print(" ")
print("Vamos jogar pedra, papel ou tesoura!")
print(" ")
escolha = input("Escolha entre pedra, papel ou tesoura: ")
pc = random.choice(lista)
print(f"Eu escolhi {pc} e você escolheu {escolha}, então")
print("-=-" * 15)
if escolha == pc:
    print("\033[1;33mEMPATE!\033[m")
elif escolha == "papel" and pc == "pedra":
    print("\033[1;32mVOCÊ GANHOU!!\033[m")
elif escolha == "pedra" and pc == "papel":
    print("\033[1;31mVOCÊ PERDEU!!\033[m")
elif escolha == "tesoura" and pc == "papel":
    print("\033[1;32mVOCÊ GANHOU!!\033[m")
elif escolha == "papel" and pc == "tesoura":
    print("\033[1;31mVOCÊ PERDEU!!\033[m")
elif escolha == "pedra" and pc == "tesoura":
    print("\033[1;32mVOCÊ GANHOU!!\033[m")
elif escolha == "tesoura" and pc == "pedra":
    print("\033[1;31mVOCÊ PERDEU!!\033[m")

print("-=-" * 15)