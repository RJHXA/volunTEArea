opcao = str
login = str
loginConfirmada = ["rjhxa@cesar.school", "pecc@cesar.school", "masd@cesar.school", "lkaan@cesar.school", "vsdg@cesar.school", "mmbc@cesar.school", "lsb4@cesar.school", "jaa2@cesar.school", "bps@cesar.school"]
cadastrados = ["Rafael", "Patrick", "Marcela", "Leonardo", "Vinícius", "Mariana", "Luiza", "Jamile", "Brunna"]
senha = int
senhaConfirmada = 123
contadorTentativas = 1
repetição = ""


# Se ele escolher para Logar
if(opcao == 'Login' or opcao == 'login'):
    print("E-mail: ")
    login = input("")
    # Verificação de E-mail, porém só conseguir com 1 Tentativa só
    if(login in loginConfirmada):
        print("Senha: ")
        senha = int (input(""))
        # Verificação da senha do Usuário
        while(senha != senhaConfirmada):
            contadorTentativas = contadorTentativas + 1
            print("Senha Errada. Tente novamente!")
            print("Você tem ", 4-contadorTentativas, " tentativas restantes!")
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
                while(repetição != "End"):
                    print("\nQue Funcionalidade você deseja acessar da Gestão? \n1-FeedBack | 2- Sugestões Anônimas | 3- Relatório dos Voluntários | 4- Voluntários Cadastrados | 5- Calendário")
                    funcionalidades = str (input(""))

                    if(funcionalidades == '1'):
                        print("| Setor do FeedBack |")
                        print("- Trabalho do Voluntário Rafael foi excelente, só precia melhorar na questão do horário e chegar em ponto!")

                    elif(funcionalidades == '2'):
                        print("| Setor das Sugestões Anônimas |")
                        print("- Nada a melhorar")

                    elif(funcionalidades == '3'):
                        print("| Setor do Relatório dos Voluntários |")
                        print("- Rafael destinada a criança 01, 21/03 às 13:00")

                    elif(funcionalidades == '4'):
                        print("| Setor do Voluntários Cadastrados |")
                        for i in range(len(cadastrados)):
                            print("- ", cadastrados[i])
                        print("Deseja adicionar um Novo Voluntário?")
                        print("Sim | Não")
                        resposta = str(input(""))
                        if(resposta == "Sim" or resposta == "sim"):
                            print("Digite o nome do novo Voluntário:")
                            cadastrados.append(input(""))
                    else:
                        print("| Setor do Calendário |")
                        print("30/07/2021 - Atividade")
                    print("\nBack | End")
                    repetição = str(input(""))
                    if(repetição == "End"):
                        break
            else:
            # VOLUNTÁRIOS
            # Escolha de qual Funcionalidade o Usuário quer usar
                while(escolha == "Voluntários"):
                    print("\nQue Funcionalidade você deseja acessar dos Voluntários? \n1- Agendamento | 2- Criança Responsável | 3- Sugestão Anônimo | 4- Relatório | 5- Calendário | 6- Devolutiva dos Pais")
                    funcionalidades = str (input(""))

                    if(funcionalidades == '1'):
                        print("| Setor do Agendamento |")
                        print("Que dia você deseja agendar com a criança?")
                        agendamento = input("")
                        print("Aguarde a Confirmação dos Responsáveis!")
                    elif(funcionalidades == '2'):
                        print("| Setor da Criança Responsável |")
                        print("Que Criança você foi destinada?")
                        crianca = str(input(""))
                    elif(funcionalidades == '3'):
                        print("| Setor Sugestão Anônimo |")
                        print("Deposite uma Sugestão aqui: ")
                        sugestao = str(input(""))
                        print("Obrigado pela sugestão!")
                    elif(funcionalidades == '4'):
                        print("| Setor do Relatório Diário |")
                        print("Coloque seu Relatório do dia aqui:")
                        relatorio = str(input(""))
                    elif(funcionalidades == '5'):
                        print("| Setor do Calendário |")
                        print("30/07/2021 -> Atividade")
                    else:
                        print("| Setor da Devolutiva dos Pais |")
                        print("Digite aqui:")
                        devolutiva = str(input(""))
                    print("\nBack | End")
                    repetição = str(input(""))
                    if(repetição == "End"):
                        break
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
        cpf = str (input(""))
        print("Digite seu número de contato:")
        numero = str(input(""))
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
        cpf = str (input(""))
        print("Digite o número de contato do Responsável:")
        numero = str(input(""))
        print("Digite o E-mail do Responsável:")
        email= input("")

        print("Aguarde a Confirmação do Cadastro da Criança!")