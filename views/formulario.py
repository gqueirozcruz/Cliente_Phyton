import controllers.controllerAplicacao as controllerAplicacao
# View - o que vai para o usuário
def formulario_login():
    usuario_digitado = input("Informe o seu usuário: ")
    senha_digitado = input("Informe sua senha: ")
    usuario_completo = [usuario_digitado, senha_digitado]
    return usuario_completo

def exibir_mensagem(texto):
        print("\n\n\n")
        print("================")
        print(texto)
        print("================")
        print("\n\n\n")

def menu():
    print("1 - Para cadastrar novo cliente")
    print("2 - Para listar toos os cliente")
    print("3 - para sair")
    opcao = input("Digite a opção")
    return opcao

def cadastro_clente():
    nome = input("Informe o nome:")
    telefone = input(" Informe o telefone: ")
    cliente=[nome,telefone]
    return cliente