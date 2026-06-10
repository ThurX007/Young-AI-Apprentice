#===========================Exercicio 8-A==============================
import random
from time import sleep
num1 = random.randint(1, 5)
num2 = int(input("Adivinhe o numero que eu estou pensando! Ele vai de 1 até 5: "))
print("Processando...")
sleep(3)
if num2 == num1:
    print(f"Parabens! Você acertou, o numero era {num1}")
else:
    print(f"Você errou! O numero era {num1}, tente novamente")

#===========================Exercicio 8-B==============================
speed = int(input("A quantos KM/h você estava? "))
if speed > 80:
    print("Você foi multado!")
    multa = (speed - 80) * 7
    print(f"Você precisará pagar uma multa de R${multa} por ultrapassar a velocidade máxima")
else:
    print("Tudo certo, prossiga!")

#===========================Exercicio 8-C==============================





#===========================Exercicio 8-D==============================
d = int(input("Qual é a distancia da viagem? "))
if d <= 200:
    valor1 = d * 0.50
    print(f"Você pagará por esta viagem o valor de R${valor1}")
else:
    valor2 = d * 0.45
    print(f"Você pagará por esta viagem o valor de R${valor2}")

#===========================Exercicio 8-E==============================





#===========================Exercicio 8-F==============================







#===========================Exercicio 8-G==============================
sal = float(input("Qual é o seu salario? "))
if sal <= 1250:
    print("Você ganhou um aumento de 15%, agora seu salario é ", sal + (sal * 0.15))
else: 
    print("Você ganhou um aumento de 10%, agora seu salario é ", sal + (sal * 0.10))