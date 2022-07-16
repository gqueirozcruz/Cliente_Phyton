
# View - o que vai para o usuário 
usuario = input("informe  o seu usuario")
senha_digitado = input("informe sua senha")

# Model - O que vem do banck de dados (BD)
usuario_BD = 'joao'
senha_BD = '123'

# Constrolller - a validação 

if usuario == usuario_BD and senha_digitado == senha_BD:
    print("pode entrar")
else: 
    print("usuário ou senha inválido")

