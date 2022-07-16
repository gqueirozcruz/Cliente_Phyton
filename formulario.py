# View - o que vai para o usuário 

import validacao

def formulario_login():
    usuario_digitado = input("informe  o seu usuario")
    senha_digitado = input("informe sua senha")
    validacao.validar_login(usuario_digitado, senha_digitado)

