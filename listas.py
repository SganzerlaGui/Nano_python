from arquivo import *
#usuarios = {}
#
#print(usuarios)
#
#usuarios = {
#        "Guilherme" : ["Guilherme Sganzerla", "20/03/2026", "Programador"],
#        "Tatiany" : ["Tatiany Sganzerla", "20/03/2026", "Fisioterapeuta"]
#}
#
#print(usuarios)
#
#usuarios ["Florinda"] = ["Florinda da Silva", "09/04/2025", "Juiza"] 
#
#print(usuarios)


usuarios = {}

opcao = perguntar()
            
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L" or opcao == "S":
    
    if opcao == "I":
        inserir(usuarios)
        # Este é um exemplo de código que utiliza um dicionário para armazenar informações de usuários.
        # O dicionário 'usuarios' é usado para armazenar as informações de cada usuário, onde a chave é o nome do usuário e o valor é uma lista contendo o nome completo, a data de nascimento e a função do usuário.
        # A função 'inserir' é responsável por adicionar um novo usuário ao dicionário 'usuarios', solicitando ao usuário as informações necessárias.
        # O código também permite a visualização das informações de cada usuário, a remoção de um usuário específico e a impressão das informações de todos os usuários.
        # O arquivo 'arquivo.py' contém a implementação das funções 'inserir', 'remover' e 'imprimir', enquanto o arquivo 'listas.py' contém o código principal que interage com o usuário.
    
    opcao = perguntar()

