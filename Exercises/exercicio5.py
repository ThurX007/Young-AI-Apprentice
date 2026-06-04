#===========================Exercicio 5-A==============================
num = int(input("Digite um numero para ver seu antecessor e sucessor: "))
print(f"O antecessor de {num} é {num - 1} e o sucessor é {num + 1}")

#===========================Exercicio 5-B==============================
num = int(input("Digite um numero para ver seu dobro, triplo e raiz quadrada: "))
print(f"O dobro de {num} é {num * 2}, o triplo é {num * 3} e a raiz quadrada é {num ** 0.5}")

#===========================Exercicio 5-C==============================
nota1 = float(input("Digite a nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print(f"A media do aluno é {media}")

#===========================Exercicio 5-D==============================
m = float(input("Digite uma distancia (EM METROS): "))
cm = m * 100
mm = m * 1000
print(f"{m}m em centimetros é {cm}cm e em milimetros é {mm}mm")

#===========================Exercicio 5-E==============================
num = int(input("Digite um numero para ver a sua tabuada: "))
print(f"Tabuada do {num}: ")
print("=" * 15)
for i in range(1, 11):
    print(f"{num} x {i:2} = {num * i:3}")

print("=" * 15)

#===========================Exercicio 5-F==============================
real = float(input("Digite quanto você tem em reais: "))
dolar = 5.07
print(f"Com R${real} você pode comprar US${real / dolar:.2f}")

#===========================Exercicio 5-G==============================
largura = float(input("Qual é a largura da parede? "))
altura = float(input("Qual é a altura da parede? "))
area = largura * altura
print(f"A area da parede é {area}m²")
tinta = area / 2
print(f"Para pintar a parede, você precisará de {tinta}L de tinta")

#===========================Exercicio 5-H==============================
print("AQUI TODOS OS PRODUTOS GANHAM DESCONTOOOO!!!!")
produto = float(input("Digite o preço do produto: R$"))
desconto = produto - (produto * 0.05)

print(f"Você ganhou 5% de desconto nesse produto! O preço com desconto é R${desconto:.2f}")

#===========================Exercicio 5-I==============================
print("Promoção de salarios!")
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}. Nós te daremos um aumento de 15% no seu salario!")
sem_aumento = float(input("Qual é o seu salario atual? R$"))
aumento = sem_aumento + (sem_aumento * 0.15)
print(f"Parabens, {nome}! Seu novo salario é R${aumento:.2f}")

#===========================Exercicio 5-J==============================
c = int(input("Qual é a temperatura em graus celsius? "))
f = 9 * c / 5 + 32
print(f"A temperatura {c}ºC em ºF é {f}ºF")

#===========================Exercicio 5-K==============================
d = int(input("Por quantos dias você alugou o carro? "))
km = float(input("Quantos km você percorreu com este carro? "))
valor = d * 60 + km * 0.15
print(f"Você terá que pagar R${valor:.2f} por este carro")