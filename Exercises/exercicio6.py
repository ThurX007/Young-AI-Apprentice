#===========================Exercicio 6-A==============================
#Jeito mais simples que só corta a parte decimal
import math

num = float(input("Digite um numero: "))

print(f"O numero digitado foi {num} e o numero inteiro é {math.trunc(num)}")

'''Jeito mais complexo que arredonda para o mais proximo inteiro'''

import math

num = float(input("Enter a decimal number to see it rounded to the nearest intenger: "))

print(f"You entered {num}, and the number rounded is {math.floor(num + 0.5)}")

#===========================Exercicio 6-B==============================
import math

ca = float(input("Enter the length of the adjacent side: "))
co = float(input("Enter the length of the opposite side: "))

hipo = math.hypot(ca, co)

print(f"{hipo:.2f}")

#===========================Exercicio 6-C==============================
import math

angle = int(input("Enter the angle you want to calculate in degrees: "))
transformar = math.radians(angle)
sen = math.sin(transformar)
cos = math.cos(transformar)
tan = math.tan(transformar)

print(f"The sine of {angle}° is {sen:.2f}\nThe cosine is {cos:.2f}\nAnd the tangent is {tan:.2f}")

#===========================Exercicio 6-D==============================
'''O jeito que eu fiz'''

import random

lista = []

for aluno in range(4):
    alunos = input("Enter the student name: ")
    lista.append(alunos)

print(f"The chosen student is {random.choice(lista)}")

'''Como era pra ter feito de acordo com o nivel'''

import random

a1 = input("Enter the name of the 1º student: ")
a2 = input("Enter the name of the 2º student: ")
a3 = input("Enter the name of the 3º student: ")
a4 = input("Enter the name of the 4º student: ")

alunos = [a1, a2, a3, a4]
choice = random.choice(alunos)

print(f"The chosen student is {choice}")

#===========================Exercicio 6-E==============================
'''Como eu quis fazer'''
import random

lista = []

for aluno in range(4):
    alunos = input("Enter the student name: ")
    lista.append(alunos)

choice1 = random.choice(lista)
print(f"The 1º chosen student to present the project is {choice1}")
lista.remove(choice1)
choice2 = random.choice(lista)
print(f"The 2º student chosen to present the project is {choice2}")
lista.remove(choice2)
choice3 = random.choice(lista)
print(f"The 3º chosen student to present the project is {choice3}")
lista.remove(choice3)
choice4 = random.choice(lista)
print(f"The last chosen student to present the project is {choice4}")
lista.remove(choice4)

'''Como eu poderia ter feito'''
import random

lista = []

for aluno in range(4):
    aluno = input("Enter the student name: ")
    lista.append(aluno)

shuffle = random.shuffle(lista)
print("A lista mostra a sequencia: ")
print(lista)
