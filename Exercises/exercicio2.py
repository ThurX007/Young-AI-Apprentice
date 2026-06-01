#============Exercicio 2-A============

usuario = input("Nome de usuário: ")
senha = input("Senha: ")

USUARIO_CORRETO = "ThurX"
SENHA_CORRETA = "1331"

if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
    print("Acesso Liberado!")
else:
    print("Acesso Negado!")

#============Exercicio 2-B============

age = int(input("Qual é a sua idade? "))

if age <= 12:
    print("Você é uma criança.")
elif 13 <= age <= 18:
    print("Você é um adolescente.")
elif 19 <= age <= 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
