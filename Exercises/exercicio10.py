#===========================Exercicio 10-A==============================
import time
for n in range(10, -1, -1):
    time.sleep(1)
    print(n)

#===========================Exercicio 10-B==============================
for i in range(2, 51, 2):
    print(i)

#===========================Exercicio 10-C==============================
s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        s = s + i
        c = c + 1
print(s, "numeros: ", c)

#===========================Exercicio 10-D==============================
num = int(input("Digite um número para ver sua tabuada: "))
print("=" * 15)
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i:2} = {resultado}")
print("=" * 15)

#===========================Exercicio 10-E==============================
s = 0
c = 0
for i in range(1, 7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        s += num
        c += 1
print(f"Você informou {c} números PARES e a soma dos valores pares é {s}")

#===========================Exercicio 10-F==============================
p = int(input("Digite o número que vc deseja iniciar: "))
r = int(input("Digite o valor da raazão que você deseja: "))
f = int(input("Digite o numero onde vc quer que pare: "))
for i in range(p, f, r):
    print(i)

#===========================Exercicio 10-G==============================
num = int(input("Digite um número: "))
tot = 0
for i in range(1, num+1):
    if num % i == 0:
        print("\033[32m", end='')
        tot += 1
    else:
        print("\033[31m", end='')
    print(i, end=' ')
print(" ")
if tot == 2:
    print("\033[34mEle é um numero primo!")
else:
    print("\033[31mEle não é um número primo!")

#===========================Exercicio 10-H==============================
frase = input("Digite uma frase: ").strip().upper()
separar = frase.split()
juntar = "".join(separar)
inverso = ''
for i in range(len(juntar) -1, -1, -1):
    inverso += juntar[i]

print(f"Você escreveu {juntar} e a palavra final é {inverso}")

if inverso == juntar:
    print("Isso é um plindromo")
else:
    print("Isso não é um palindromo")

#===========================Exercicio 10-I==============================
s = 0
s1 = 0
for i in range(7):
    ano = int(input(f"Em que ano a {i+1}ª pessoa nasceu? "))
    if 2026 - ano > 18:
        s += 1
    elif 2026 - ano < 18:
        s1 += 1

print(f"Ao todo tivemos {s} pessoas maior de idade")
print(f"E tambem tivemos {s1} pessoas menor de idade")

#===========================Exercicio 10-J==============================
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f"Digite o peso da {p}ª pessoa: "))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f"O maior peso lido é o de {maior}Kg")
print(f"O menor peso lido é o de {menor}Kg")

#===========================Exercicio 10-K==============================
it = 0
nomevelho = ""
maioridadehomem = 0
mulhernova = 0
for p in range(1, 5):
    print("-" * 15, f"{p}ª PESSOA", "-" * 15)
    n = str(input("Nome: ")).title()
    i = int(input("Idade: "))
    s = input("Sexo [M/F]: ").upper()

    if p == 1 and s == "M":
        maioridadehomem = i
        nomevelho = n
    elif s == "M" and i > maioridadehomem:
        maioridadehomem = i
        nomevelho = n

    if s == "F" and i < 20:
        mulhernova += 1
    
        it += i
print("-" * 41)
print("A média de idade do grupo é", it / 4)
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")
print(f"Nesse grupo existem {mulhernova} mulher(es) com menos de 20 anos de idade")