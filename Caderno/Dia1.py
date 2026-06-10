r1 = int(input("Digite o valor da 1° reta: "))
r2 = int(input("Digite o valor da 2° reta: "))
r3 = int(input("Digite o valor da 3° reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Podem formar um triangulo")
else:
    print("Não podem formar um triangulo")