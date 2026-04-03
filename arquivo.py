def clean():
    import os
    os.system("cls")



def perguntar():
# O return:é usada para retornar um valor de uma função. Quando uma função é chamada, ela executa um bloco de código e, em seguida, retorna um valor
    return input("Oque você deseja realizar?: \n" +
              "<I> - para cadastrar usuario\n" +
              "<P> - para Pesquisar usuario\n" +
              "<E> - para Excluir usuario\n" +
              "<L> - para Listar usuario\n" +
              "<S> - para Sair\n").upper()

def inserir(dicionario):
    chave = input("Digite o nome do usuario: ").upper()
    nome = input("Digite o seu nome: ").upper()
    nascimento = input("Digite a data de nascimento do usuario (Use: d/m/a): ")

