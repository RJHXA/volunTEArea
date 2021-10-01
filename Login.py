opcao = str
login = str
loginConfirmada = ["rjhxa@cesar.school", "pecc@cesar.school", "masd@cesar.school", "lkaan@cesar.school", "vsdg@cesar.school", "mmbc@cesar.school", "lsb4@cesar.school", "jaa2@cesar.school", "bps@cesar.school"]
senha = int
senhaConfirmada = 123
x = 0
achou = False
contadorTentativas = 0

# Primeira Escolha do Usuário
print("Escolha uma das opções: \nLogin | Cadastro")
opcao = input("")

# Se ele escolher para Logar
if(opcao == 'Login' or opcao == 'login'):
    print("Login (e-mail): ")
    login = input("")
    # Verificação de E-mail, porém só conseguir com 1 Tentativa só
    while(login != loginConfirmada[x]):
        for i in loginConfirmada:
            if(login == loginConfirmada[x]):
                achou = True
                break
            x += 1
        if(achou == True):
            break
        else:
            break
    # Se a Verificação do E-mail der certo vai para o aplicativo
    if(x <= 8):
        print("Senha: ")
        senha = int (input(""))

        # Verificação da senha do Usuário
        while(senha != senhaConfirmada):
            contadorTentativas = contadorTentativas + 1
            print("Senha Errada. Tente novamente!")
            print("Você tem ", 3-contadorTentativas, " tentativas restantes!")
            senha = int (input(""))
        # Se o Usuário errar a senha 3 vezes, Fim do programa           
            if(contadorTentativas>=3):
                break
        # Se o Usuário conseguir acertar a senha em menos de 3 tentativas, segue o app
        if(contadorTentativas<3):
            print("Bem Vindo ao Aplicativo volunTEArea!")
            print("Você faz parte da Área de Gestão ou dos Voluntários?")
            # Escolha se é da área de Gestão ou Voluntários
            escolha = str (input(""))
            # GESTÃO
            # Escolha de qual Funcionalidade o Usuário quer usar
            if(escolha == 'Gestão'):
                print("Que Funcionalidade você deseja acessar da Gestão? \nFeedBack | Sugestões Anônimas | Relatório dos Voluntários | Voluntários Cadastrados | Calendário")
                funcionalidades = str (input(""))

                if(funcionalidades == 'FeedBack' or funcionalidades == 'Feedback'):
                    print("Setor do FeedBack")
                    print("- Melhor Aplicativo =)")

                elif(funcionalidades == 'Sugestões Anônimas'):
                    print("Setor das Sugestões Anônimas")
                    print("- Nada a melhorar")

                elif(funcionalidades == 'Relatório dos Voluntários'):
                    print("Setor do Relatório dos Voluntários")
                    print("- Rafael destinada a criança 01, 21/03 às 13:00")

                elif(funcionalidades == 'Voluntários Cadastrados'):
                    print("Setor do Voluntários Cadastrados")
                    print("- Rafael\n- Patrick\n- Marcela\n- Leonardo\n- Vinicius\n- Mariana\n- Luiza\n- Jamile\n- Brunna")

                else:
                    print("Setor do Calendário")
                    print("30/07/2021 - Atividade")
            else:
            # VOLUNTÁRIOS
            # Escolha de qual Funcionalidade o Usuário quer usar
                print("Que Funcionalidade você deseja acessar dos Voluntários? \nAgendamento | Criança Responsável | Sugestão Anônimo | Relatório | Calendário | Devolutiva dos Pais")
                funcionalidades = str (input(""))

                if(funcionalidades == 'Agendamento'):
                    print("Setor do Agendamento")
                    print("Que dia você deseja agendar com a criança?")
                    agendamento = input("")
                    print("Aguarde a Confirmação dos Responsáveis!")
                elif(funcionalidades == 'Criança Responsável'):
                    print("Setor da Criança Responsável")
                    print("Que Criança você foi destinada?")
                    crianca = str(input(""))
                elif(funcionalidades == 'Sugestão Anônimo'):
                    print("Setor Sugestão Anônimo")
                    print("Deposite uma Sugestão aqui: ")
                    sugestao = str(input(""))
                    print("Obrigado pela sugestão!")
                elif(funcionalidades == 'Relatório'):
                    print("Setor do Relatório Diário")
                    print("Coloque seu Relatório do dia aqui:")
                    relatorio = str(input(""))
                elif(funcionalidades == 'Calendário'):
                    print("Setor do Calendário")
                    print("30/07/2021 -> Atividade")
                else:
                    print("Setor da Devolutiva dos Pais")
                    print("Digite aqui:")
                    devolutiva = str(input(""))
    
        else:
# Se o Usuário Errar a senha 3 Vezes. Fim do Programa
            print("Você errou 3 Tentativas. Tente Novamente mais tarde!")
    else:
    # Se o Usuário Errar o E-mail. Fim do Programa
        print("E-mail não Encontrado. Por Favor ir para a Área de Cadastro!")

else: 
# Escolha do Cadastro de Voluntário ou da Criança  
    print("Escolha uma das opções: \nVoluntário | Responsável")
    opcao2 = str(input(""))

    if(opcao2 == 'Voluntário' or opcao2 == 'voluntário'):
    # Informações Pessoais Sobre o Voluntário
        print("Digite seu nome completo: ")
        nome = str(input(""))
        print("Qual sua Data de Nascimento?")
        idade = input("")
        print("Você já se voluntariou alguma vez na sua vida?")
        resposta = str(input(""))
        print("Digite seu Cpf:")
        cpf = int (input(""))
        print("Digite seu número de contato:")
        numero = int(input(""))
        print("Digite seu E-mail:")
        email= input("")

        print("Aguarde a Confirmação do seu Cadastro!")

    else:
    # Informações Pessoais Sobre o Responsável e da Criança
        print("Digite o nome completo do Responsável: ")
        nome = str(input(""))
        print("Digite o nome completo da Criança: ")
        nomeCrianca = str(input(""))
        print("Qual a Data de Nascimento do Responsável?")
        idadeResponsavel = input("")
        print("Qual a Data de Nascimento da Criança?")
        idade = input("")
        print("Digite o Cpf do Responsável:")
        cpf = int (input(""))
        print("Digite o número de contato do Responsável:")
        numero = int(input(""))
        print("Digite o E-mail do Responsável:")
        email= input("")

        print("Aguarde a Confirmação do Cadastro da Criança!")


