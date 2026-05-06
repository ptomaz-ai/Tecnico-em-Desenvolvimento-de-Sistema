# Criando uma variavel numerica

numero = 10 

#criado uma variavel texto

nome = "gabriel"

#usuario inserir um texto

nome_completo = int(input("digite seu nome"))

#usuario inserir um numero inteiro

idade = int(input("digite um numero"))

#usuario inserir um numero decimal

salario = float(input("digite seu salario"))

#estruturas condicionais

if (salario >1500 and idade >= 18 ):
    print("voçê pode tirar carta")
elif (salario <1500 or idade <18 ):
    print("voçê não pode tirar carta")
else:
    print("invalido")

#estrutura condicionais exemplo 2

turno = input("digite seu turno (M/V/n):")

if( turno == "M"):#utilizar dois iguais para comparar
    print("Bom dia!")
elif( turno == "V" ):
    print("boa tarde ")
elif( turno == "N!" ):
    print("boa noite")

#estrutura da repetição
# 0 -> 10

for i in range(11):#sempre coloque um
    print(i)

for i in range(1,16):
    print(i)

#5 ->65 (aumento de 5 em 5)

for i in range(5,66,+5):
    print(i)

for i in range(122<-1,-2):
    print(i)

#usuario escolhe inisio e fim 

inicio = int(input("inicio"))
fim = int(input("fim"))

for i in range(inicio,fim,-1):
    print(i)

#vetor

nomes = []

for i in range(5):
    nomes.append(input("digite um nome"))

for nome in nomes:
    print("nome")