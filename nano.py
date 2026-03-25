#nome = input("Digite um funcionário: ")
#
#empresa = input("Digite a instituição: ")
#
#qtde_funcionarios = int(input("Digite a qtde de funcionários: "))
#
#mediaMensalidade = float(input("Digite a média da mensalidade: "))
#
#print(nome + " trabalha na empresa " + empresa)
#
#print("Possui: ", qtde_funcionarios, " funcionarios.")
#
#print("A média da mensalidade é de: " + str(mediaMensalidade))
#
#print("==============Verifique os tipos de dados abaixo:==============")
#
#print("O tipo de dado da variavel [nome] é: ", type(nome))
#
#print("O tipo de dado da variavel [empresa] é: ", type(empresa))
#
#print("O tipo de dado da variavel [qtde_funcionarios] é: ", type(qtde_funcionarios))
#
#print("O tipo de dado da variavel [mediaMensalidade] é: ", type(mediaMensalidade))

# APRENDENDO (DECISÃO) IF, ELIF E ELSE ------------------------------------------------------------------------

#nome = input("Digite o seu nome: ")
#idade = int(input("Digite a sua idade: "))
#if idade >= 65:
#    print("Paciente", nome, "POSSUI atendimento prioritario.")
#else:
#    print("Paciente", nome, "NÃO possui atendimento prioritario.")

# APRENDENDO LAÇOS DE REPETIÇÃO (WHILE E FOR) ------------------------------------------------------------------------

#numero = int(input("Digite um numero: "))
#while numero < 100:
#    print(str(numero))
#    numero = numero + 1 
#print("Laço encerrado")

#tabuada = int(input("Digite um numero para ver sua tabuada: "))
#print("Tabuada do", tabuada)
#for valor in range(1,11,1):
#    print(str(tabuada) + "X" + str(valor) + "=" + str((tabuada*valor)) )

#O range(valor, limite, passo) gera uma sequência de números. Os parâmetros são:
#valor: o primeiro número da sequência (por padrão, 0).
#limite: o número que determina quando a iteração do loop deve parar. Os números gerados são menores que o limite.
#passo: a quantidade que o contador é incrementado (ou decrementado, se for negativo) a cada iteração do loop. Por padrão, é 1.
#Por exemplo, range(1, 11, 1) gera uma sequência de números de 1 a 10. range(5, 16, 2) gera uma sequência de números de 5 a 15 com um passo de 2.

# LISTAS E VARIAVEIS --------------------------------------------------------------------------------------------

#O append agrega o item que foi respondido no input no - invetario[] -

inventario = []
resposta = "S"
while resposta  == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("numero serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print(elemento)
