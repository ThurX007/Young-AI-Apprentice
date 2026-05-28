name = input("Qual é o seu Nome? ")
idade = int(input("Qual é a sua idade? "))
nasceu_m = int(input("Em qual mes você nasceu? Em numero "))

ano = int(2026)
mes = int(5)

nascimento_y = ano - idade
nascimento_m = mes - nasceu_m


print ("Seu nome é " + name)
print ("Você tem", idade, "anos")
if nasceu_m <= mes:
    print(nascimento_y)
else :
    print("Você nasceu em", nascimento_y - 1)

    print("Você tem", nascimento_m, "meses")