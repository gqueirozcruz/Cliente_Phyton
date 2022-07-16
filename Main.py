
# View - o que vai para o usuário 
def view ():
    usuario_digitado = input("informe  o seu usuario")
    senha_digitado = input("informe sua senha")
    controller(usuario_digitado, senha_digitado)





# Model - O que vem do banck de dados (BD)
def model_usuario():
    usuario_BD = 'joao'
    return usuario_BD


def model_senha():
    senha_BD = '123'
    return senha_BD 




# Constrolller - a validação 
def controller(usuario_digitado, senha_digitado):
    usuario_BD = model_usuario()
    senha_BD = model_senha()

    if usuario_digitado == usuario_BD and senha_digitado == senha_BD:
        print("pode entrar")
    else: 
        print("usuário ou senha inválido")






view()