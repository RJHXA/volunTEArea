def setor_agendamento():
    print("| Setor do Agendamento |")
    print("Que dia você deseja agendar com a criança?")
    agendamento = input("")
    print("Aguarde a Confirmação dos Responsáveis!")

def setor_crianca_responsal():
    print("| Setor da Criança Responsável |")
    print("Que Criança você foi destinada?")
    crianca = str(input(""))

def setor_anonimo():
    print("| Setor Sugestão Anônimo |")
    print("Deposite uma Sugestão aqui: ")
    sugestao = str(input(""))
    print("Obrigado pela sugestão!")

def setor_relatorio():
    print("| Setor do Relatório Diário |")
    print("Coloque seu Relatório do dia aqui:")
    relatorio = str(input(""))

def setor_calendario():
    print("| Setor do Calendário |")
    print("30/07/2021 -> Atividade")

def setor_devolutiva():
    print("| Setor da Devolutiva dos Pais |")
    print("Digite aqui:")
    devolutiva = str(input(""))

# VOLUNTÁRIOS
# Escolha de qual Funcionalidade o Usuário quer usar
def user_voluntario():
    repetição = ""
    while(repetição != 2):
        print("\nQue Funcionalidade você deseja acessar dos Voluntários? \n1- Agendamento | 2- Criança Responsável | 3- Sugestão Anônimo | 4- Relatório | 5- Calendário | 6- Devolutiva dos Pais")
        funcionalidades = int (input(""))

        if(funcionalidades == 1):
            setor_agendamento()
        elif(funcionalidades == 2):
            setor_crianca_responsal()
        elif(funcionalidades == 3):
            setor_anonimo()
        elif(funcionalidades == 4):
            setor_relatorio()
        elif(funcionalidades == 5):
            setor_calendario()
        elif(funcionalidades == 6):
            setor_devolutiva()
        else:
            print("Opção Inválida!")
        print("\n1 - Back | 2 - End")
        repetição = int(input(""))