from NANO_PYTHON_FIAP.arquivo import *

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
        chave = input("Digite o nome do usuario: ").upper()
        nome = input("Digite o nome do usuario: ").upper()
        nascimento = input("Digite a data de nascimento do usuario (Use: d/m/a): ")
        usuarios[chave] = [nome], [nascimento]
    
    opcao = perguntar()

