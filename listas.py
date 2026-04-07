from arquivo import *
import os


#usuarios = {}

#print(usuarios)

#usuarios = {
#        "Guilherme" : ["Guilherme Sganzerla", "20/03/2026", "Programador"],
#        "Tatiany" : ["Tatiany Sganzerla", "20/03/2026", "Fisioterapeuta"]
#}

#print(usuarios)

#usuarios ["Florinda"] = ["Florinda da Silva", "09/04/2025", "Juiza"] 

#print(usuarios)


#usuarios = {}

#opcao = perguntar()
#while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L" or opcao == "S":    
#    if opcao == "I":
#        inserir(usuarios)
#        #----- Este é um exemplo de código que utiliza um dicionário para armazenar informações de usuários.
#        # ------O dicionário 'usuarios' é usado para armazenar as informações de cada usuário, onde a chave é o nome do usuário e o valor é uma lista contendo o nome completo, a data de nascimento e a função do usuário.
#        # -------A função 'inserir' é responsável por adicionar um novo usuário ao dicionário 'usuarios', solicitando ao usuário as informações necessárias.
#        # -------O código também permite a visualização das informações de cada usuário, a remoção de um usuário específico e a impressão das informações de todos os usuários.
#        # --------O arquivo 'arquivo.py' contém a implementação das funções 'inserir', 'remover' e 'imprimir', enquanto o arquivo 'listas.py' contém o código principal que interage com o usuário.    
#    opcao = perguntar()

#---Lista = []
#---dicionnario {}
#---tupla()    
#------Tupla para retornar mais de 1 valor de 1 metodo
#--------enumerate vai voltar enumerado: 11,2,3,4,5,6,7......
#l-------list concatena a numeração e os gmails em uma tupla

for chave in range(0, len(tupla)):    
    #print(f"Email:", tupla[chave][1])
    novo_email = input("Digite o seu email: ")
    usuario = input("Digite o seu usuario: ")
    nome = input("Digite o seu nome: ")
    nivel = input("Digite o seu nivel: ")
    usuarios[tupla[chave][1]] = [nome, nivel, usuario]
if novo_email in emails:
    print("Esse email já está cadastrado!!")
else:
    emails.append(novo_email)

clean()

for chave, dado in usuarios.items():
   
    print(f"- Usuario......", {usuarios[chave][2]})
    print(f"- Email......", {novo_email})
    print(f"- Nome.....", {nome})
    print(f"- Nivel......", {nivel})

print(emails)

# ------[chave] -> Escolhe qual usuário da lista estamos acessando (o 1º, o 2º, etc.)

# ---------[1] -> Pega o e-mail que está guardado dentro da tupla do enumerate

# ---------[0] -> Pega a primeira informação da lista (o Nome)

# --------[1] -> Pega a segunda informação da lista (o Nível)




from captura import *

usuarios = {}

def menu():
    print("1 - Inserir usuario\n" +
          "2 - Pesquisar usuario\n" +
          "3 - Excluir usuario\n" +
          "4 - Listar usuarios\n" +
          "5 - Sair\n")
    
    # Chamando a função que está no captura.py
    return pegar_opcao()

# --- Execução (que volta ao menu após concuido)---

while True:
    clean()
    opcao = menu()

    if opcao == "1":
        inserir(usuarios)
        print(usuarios)
    
    elif opcao == "2":
        pesquisar(usuarios)
    
    elif opcao == "3":
        excluir(usuarios)
    
    elif opcao == "4":
        listar(usuarios)
    
    elif opcao == "5":
        sair()
        #break # Quebra o loop e fecha o programa
    
    else:
        print("Opção inválida!")

    # Pausa para o usuário conseguir ler o que aconteceu antes de limpar a tela
    input("\nPressione ENTER para voltar ao menu...")
    break

clean()

nome_da_pessoa = inserir(usuarios) 

print(f"Acabamos de cadastrar o {nome_da_pessoa}!")
