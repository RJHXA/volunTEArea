# GESTÃO
# opcao de qual Funcionalidade o Usuário quer usar
def user_func():
    repeticao = ""
    cadastrados = ["Rafael", "Patrick", "Marcela", "Leonardo", "Vinícius", "Mariana", "Luiza", "Jamile", "Brunna"]
    funcionalidades={1:('| Setor do FeedBack |','\n- Trabalho do Voluntário Rafael foi excelente, só precia melhorar na questão do horário e chegar em ponto!'), 
                 2: ('| Setor das Sugestões Anônimas |','- Nada a melhorar'),
                 3:('| Setor do Relatório dos Voluntários |','- Rafael destinada a criança 01, 21/03 às 13:00'),
                 4:'| Setor do Voluntários Cadastrados |'}
    while(repeticao != "End"):
        print("\nQue Funcionalidade você deseja acessar da Gestão? \n1-FeedBack | 2- Sugestões Anônimas | 3- Relatório dos Voluntários | 4- Voluntários Cadastrados | 5- Calendário")
        funcionalidade = int(input())

        if funcionalidade in funcionalidades:
            print('{}'.format(funcionalidades[funcionalidade]))

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
        print("Você quer continuar? Caso queira finalizar, digite 'End'.")
        repeticao = str(input(""))