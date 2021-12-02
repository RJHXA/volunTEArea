from cadastro import *
from login import *
from bd import *
from gestao import *
from voluntario import *
armazenmento = []

print("Escolha uma das opções: \n1 - Login | 2 - Cadastro")
opcao = int(input("Escolha 1 ou 2: "))

if(opcao == 1):
    print("Escolha um setor 1 - Gestão | 2 - Voluntário")
    resposta = int(input())
    if(resposta == 1):
        # Gestão
        email = input("Digite seu email: ")
        senha = int(input("Digite sua senha: "))
        verificacao = autenticacao_login(lista_gestao, email, senha)
        if(verificacao == 1):
            # Verificação Aprovada
            print("Bem vindo o Setor de Gestão!")
            user_func()
        elif(verificacao == 2):
            print("Senha Errada! Tente Novamente mais Tarde!")
        else:
            print("E-mail não Cadastrado! Por Favor se dirigir ao Setor de Cadastro")

    elif(resposta == 2):
        # Voluntário
        email = input("Digite seu email: ")
        senha = int(input("Digite sua senha: "))
        verificacao = autenticacao_login(lista_voluntario, email, senha)
        if(verificacao == 1):
            print("Bem vindo o Setor de Voluntário!")
            user_voluntario()
        elif(verificacao == 2):
            print("Senha Errada! Tente Novamente mais Tarde!")
        else:
            print("E-mail não Cadastrado! Por Favor se dirigir ao Setor de Cadastro")

    # elif(resposta == 3):
    #     # Responsável
    #     email = input("Digite seu email: ")
    #     senha = int(input("Digite sua senha: "))
    #     verificacao = autenticacao_login(lista_responsavel, email, senha)
    #     if(verificacao == 1):
    #         print("Bem vindo o Setor de Responsável!")
    #     elif(verificacao == 2):
    #         print("Senha Errada! Tente Novamente mais Tarde!")
    #     else:
    #         print("E-mail não Cadastrado! Por Favor se dirigir ao Setor de Cadastro")

elif(opcao == 2):
    print("Escolha uma das opções: \n1 - Voluntário | 2 - Responsável")
    opcao2 = int(input(""))
    while(opcao2 != 1 and opcao2 != 2):
        opcao2 = int(input("Erro! Digite 1 ou 2\n"))
    if(opcao2 == 1):
        cadastro_voluntario(armazenmento)
    else:
        cadastro_responsavel(armazenmento)