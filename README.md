# volunTEArea


## Projeto
Nós somos o grupo volunTEArea e vamos explicar o código que construimos para o Projeto!

### bd.py:
Inicialmente, temos o arquivo "bd.py" que funciona como um banco de dados que contém as informações das pessoas da gestão, dos voluntários e dos responsáveis. Essas informações são armazenadas em 3 listas de dicionários diferentes, sendo, os responsáveis da gestão na “lista_gestao”, os voluntários na “lista_voluntario” e os responsáveis das crianças na “lista_responsavel”.

***
### login.py:
Em seguida, temos o arquivo “login.py” que realiza a verificação do e-mail que ocorre na função "busca_email" que recebe os parâmetros da lista de dicionários do arquivo “bd.py” e o e-mail digitado pelo usuário. Com isso, ele verifica na lista de dicionários se o e-mail está presente, se sim a função retorna a posição do cadastro, se não retorna nada. Em seguida, temos a confirmação da senha onde ocorre na função “autenticacao_login” que recebe a posição onde se encontra o e-mail digitado pelo usuário e verifica se a senha está correta ou não. Caso o usuário digite um e-mail não existente o programa apresentará uma mensagem de erro pedindo para ele se cadastrar.

***
### gestao.py:
Prosseguindo, temos o arquivo “gestao.py” que contém as funcionalidades, separadas em funções, presentes no programa. Apresenta um while que dentro tem um input perguntando qual funcionalidade deseja acessar e condicionais chamando a função da funcionalidade escolhida do usuário. Ao fim, pergunta se o usuário deseja voltar para a escolha da funcionalidade (Back) ou encerrar o programa (End).

***
### voluntario.py:
Nesse viés, temos o arquivo “voluntario.py” que contém as funcionalidades, separadas em funções, presentes no site. Igual ao arquivo de gestão, apresenta um while que dentro tem um input perguntando qual funcionalidade deseja acessar e condicionais chamando a função da funcionalidade escolhida do usuário. Ao fim, pergunta se o usuário deseja voltar para a escolha da funcionalidade (Back) ou encerrar o programa (End).

***
### cadastro.py:
Seguidamente, temos o arquivo “cadastro.py” que consiste em duas partes. A primeira é uma função em que o cadastro é voltado para os voluntários onde é perguntado seu nome, CPF, data de nascimento, telefone, e-mail e senha. Ao fim, essas informações são adicionadas por um append na lista de dicionários do banco de dados (bd.py). A segunda é outra função em que o cadastro é voltado para os responsáveis onde é perguntado o nome do responsável, nome(s) da(s) criança(s), CPF do responsável, data de nascimento do responsável, telefone do responsável, e-mail do responsável e a senha. Ao fim, as informações também são adicionadas por um append mas em outra lista de dicionários do banco de dados.

***
### main.py:
Por fim, temos o arquivo “main.py” que contém os import's de todos os arquivos citados anteriormente. Ele inicia com um input perguntando se o usuário deseja fazer login ou cadastro. Escolhendo Login, o programa pede pra ele escolher entre o setor de Gestão ou de Voluntário. Se o usuário escolher o setor de Gestão, o programa vai pedir seu e-mail e senha e realizar a verificação do arquivo de "login.py", caso for aprovado ele entrará nas funcionalidades do setor de gestão do arquivo "gestao.py", caso não ele apresentará o erro que o usuário fez. Se o usuário escolher o setor de Voluntário, o programa fará o mesmo passo a passo citado anteriormente. Caso o usuário não tenha escolhido a opção de Login e escolheu a parte de Cadastro, o programa irá pedir que tipo de cadastro o usuário vai querer fazer. Se o usuário escolher se cadastrar como Voluntário, o programa puxará a função cadastro_voluntario do arquivo "cadastro.py". Se o usuário escolher se cadastrar como Responsável, o programa puxará a função cadastro_responsavel.

***
