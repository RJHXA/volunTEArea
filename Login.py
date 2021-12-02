def busca_email(lista_emails, email):
    for i in lista_emails:
        if(i["email"] == email):
            return i
    return None

def autenticacao_login(lista_emails, email, senha):
    verficacao_login = busca_email(lista_emails, email)
    if (verficacao_login != None):
        if verficacao_login["senha"] == senha:
            return 1
        else:
            return 2
    else:
        return 3