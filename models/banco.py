# Model - O que vem do banco de usuarios (BD)
def model_usuario():
    arquivo = open("models\\usuarios.txt","r+")
    conteudo = arquivo.readlines()
    for linha in conteudo:
        usuario_senha = linha.split(";")
    usuario_BD = usuario_senha[0]
    return usuario_BD

def model_senha():
    senha_BD = '123'
    return senha_BD
    for linha in conteudo:
        usuario_senha = linha.split(";")
    senha_BD = usuario_senha[1]
    return senha_BD

