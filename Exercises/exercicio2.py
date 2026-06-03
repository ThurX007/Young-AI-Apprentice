#============Exercicio 2-A============

print("Criar Usuario")
usuario = input("Nome de usuário: ")
senha = input("Senha: ")

print("Login")
usuario_login = input("Nome de usuário: ")
senha_login = input("Senha: ")

if usuario_login == usuario and senha_login == senha:
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
