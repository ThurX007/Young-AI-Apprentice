#===========================Exercicio 11-A==============================
while True:
    s = input("Digite seu sexo (M/F): ").upper()
    if s == "M" or s == "F":
        break
    else:
        print("Este sexo não existe!")

#===========================Exercicio 11-B==============================
import random
tentativas = 0
while True: 
    pc = random.randint(0, 10)
    pessoa = int(input("Tente acertar o numero que eu estou pensando de 0 a 10: "))
    tentativas += 1
    if pessoa == pc:
        print(f"\033[32mParabens, você acertou!!\033[m \033[33mMas precisou de {tentativas}\033[m")
        print(f"O numero que eu pensei era {pc} e oque você disse tambem era {pessoa}")
        break
    else:
        print("\033[31mVocê errou, tenta denovo!\033[m")

#===========================Exercicio 11-C==============================
import time

num1 = int(input("Digite um numero inteiro: "))
num2 = int(input("Digite um numero inteiro: "))

while True:
    print('''[1] Somar 
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Saior do programa''')
    menu = int(input('''Escolha um para prosseguir: '''))
    if menu == 1:
        print("\033[32mA Soma dos números é", f"\033[32m{num1 + num2}\033[m")

    elif menu == 2:
        print("\033[32mO produto dos números é\033[m", f"\033[32m{num1 * num2}\033[m")

    elif menu == 3:
        if num1 == num2:
            print("\033[32mOs números são iguais\033[m")
        elif num1 > num2:
            print(f"\033[32mO maior número entre {num1} e {num2} é {num1}\033[m")
        elif num2 > num1:
            print(f"O maior número entre {num1} e {num2} é {num2}")

    elif menu == 4:
        print("Retornando...")
        time.sleep(1)
        num1 = int(input("Digite um numero inteiro: "))
        num2 = int(input("Digite um numero inteiro: "))

    elif menu == 5:
        print("Obrigado por nós escolher :)")
        break
    else:
        print("ERROR! Este numero não existe")
        num1 = int(input("Digite um numero inteiro: "))
        num2 = int(input("Digite um numero inteiro: "))

#===========================Exercicio 11-D==============================
num = int(input("Digite um número para ver o seu fatorial: "))
c = num
f = 1
print(f"O fatorial de {num} é: ")
while c > 0:
    print(c, end=" ")
    print("x" if c > 1 else "=", end=" ")
    f *= c
    c -= 1
print(f)
"'''''''''''''''''''''''''''''''"'''OU'''''''''''''''''"''''''''''''''''''"
num = int(input("Digite um número para ver o seu fatorial: "))
from math import factorial
print(f"O fatorial de {num} é", factorial(num))

#===========================Exercicio 11-E==============================
termo1 = int(input("Digite o primeiro termo da sua PA: "))
r = int(input("Digite a razão da sua PA: "))
termou = int(input("Digite o ultimo termo da sua PA: "))
c = termo1
print(termo1, "-->", end=" ")
while c <= termou - r:
    c += r
    print(c, end="")
    print(" --> " if c < termou - r else "", end="")

#===========================Exercicio 11-G==============================
s = 0
t = 0
n = 0
while n != 999:
    n = int(input("Digite um número. [999 para parar]: "))
    if n != 999:
        s += n
        t += 1
print(f"Você digitou {t} números e a soma entre eles é {s}")

#===========================Exercicio 11-H==============================
c = 0
t = 0
maior = 0
menor = 100000000000
while True:
    n = int(input("Digite um número: "))
    a = input("Quer continuar? [S/N] ").upper()
    c += 1
    t += n
    if menor > n:
        menor = n
    if n > maior:
        maior = n
    if a == "N":
        break
    elif a != "S":
        print("\033[33mNão consegui entender o seu comando, vou interpretar como se quisesse parar!\033[m")
        break
m = t / c
print(f"Você digitou {c} números e a média desses números foi {m}")
print(f"O maior valor entre eles é {maior} e o menor valor é {menor}")

