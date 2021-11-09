def cadastro_voluntario(lista_voluntario):
    usuario = {}
    usuario["nome"] = input("Digite seu nome: ")
    usuario["cpf"] = input("Digite seu cpf: ")
    usuario["nascimento"] = input("Digite a sua data de nascimento: ")
    usuario["telefone"] = input("Digite seu telefone: ")
    usuario["email"] = input("Digite seu e-mail: ")
    usuario["senha"] = input("Digite sua senha: ")

    lista_voluntario.append(usuario)
    return "Cadastro Efetuado!"

def cadastro_responsavel(lista_responsavel):
    usuario = {}
    usuario["nome"] = input("Digite seu nome: ")
    usuario["crianca"] = input("Digite o(s) nome(s) da criança(s): ").split(" ")
    usuario["cpf"] = input("Digite seu cpf: ")
    usuario["nascimento"] = input("Digite a sua data de nascimento: ")
    usuario["telefone"] = input("Digite seu telefone: ")
    usuario["email"] = input("Digite seu e-mail: ")
    usuario["senha"] = input("Digite sua senha: ")

    lista_responsavel.append(usuario)
    return "Cadastro Efetuado!"