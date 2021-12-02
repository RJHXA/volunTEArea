def setor_feedback():
    print("| Setor do FeedBack |")
    print("- Trabalho do Voluntário Rafael foi excelente, só precia melhorar na questão do horário e chegar em ponto!")

def setor_anonimas():
    print("| Setor das Sugestões Anônimas |")
    print("- Nada a melhorar")

def setor_relatorio():
    print("| Setor do Relatório dos Voluntários |")
    print("- Rafael destinada a criança 01, 21/03 às 13:00")

def setor_cadastrados(lista):
    for i in range(len(lista)):
        print("- ", lista[i])
    print("Deseja adicionar um Novo Voluntário?")
    print("1 - Sim | 2 - Não")
    resposta = int(input(""))
    if(resposta == 1):
        print("Digite o nome do novo Voluntário:")
        lista.append(input(""))
    else:
        return lista

def setor_calendario():
    print("| Setor do Calendário |")
    print("30/07/2021 - Atividade")

# GESTÃO
# opcao de qual Funcionalidade o Usuário quer usar
def user_func():
    repeticao = ""
    cadastrados = ["Rafael", "Patrick", "Marcela", "Leonardo", "Vinícius", "Mariana", "Luiza", "Jamile", "Brunna"]
    while(repeticao != 2):
        print("\nQue Funcionalidade você deseja acessar da Gestão? \n1-FeedBack | 2- Sugestões Anônimas | 3- Relatório dos Voluntários | 4- Voluntários Cadastrados | 5- Calendário")
        funcionalidade = int(input())

        if (funcionalidade == 1):
            setor_feedback()
        elif(funcionalidade == 2):
            setor_anonimas()
        elif(funcionalidade == 3):
            setor_relatorio()
        elif(funcionalidade == 4):
            setor_cadastrados(cadastrados)
        elif(funcionalidade == 5):
            setor_calendario()
        else:
            print("Opção Inválida!")
        print("1 - Back | 2 - End")
        repeticao = int(input(""))