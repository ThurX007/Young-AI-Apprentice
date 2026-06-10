#===========================Exercicio 7-A==============================
nome = input("What is your full name? ").strip()
print(f"Seu nome maiusculo é {nome.upper()}")
print(f"Seu nome minusculo é {nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(" ")} letras")
separar = nome.split()
print(f"Seu primeiro nome tem {len(separar[0])} letras")

#===========================Exercicio 7-B==============================
'''Como eu fiz'''
city = input("Digite o nome da sua cidade: ").strip().lower()
separar = city.split()
if separar[0] == "santo":
    print("True")
else:
    print("False")

'''Como ele fez'''
city = input("Digite o nome da sua cidade: ").strip()
print(city[:5].upper() == "SANTO")

#===========================Exercicio 7-C==============================
nome = input("Enter your full name: ").strip().lower()
print("silva" in nome)

#===========================Exercicio 7-D==============================
frase = input("Enter a sentence: ").strip().upper()
print(f"A letra 'A' aparece {frase.count("A")} vezes")
print(f"A primeira letra 'A' aparece na posição {frase.find("A") + 1}")
print(f"O ultimo 'A' aparece na posição {frase.rfind("A") + 1}")

#===========================Exercicio 7-E==============================
nome = input("Qual é o seu nome? ").title().strip()
nome1 = nome.split()
print(f"Prazer em te conhecer, {nome}!")
print(f"Seu primeiro nome é {nome1[0]}")
print(f"Seu ultimo nome é {nome1[-1]}")