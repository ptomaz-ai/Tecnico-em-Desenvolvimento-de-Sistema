#revisão vetores -1
#preencher o vetor
#percorrer o vetor e calcular a soma dos numeros
#
#
# ------------------------------------------------
vetor = []
soma = 0 
qdt = int(input("digite a quantidade de numeros"))

#passo 2(preencher o vetor)
for i in range(qdt):
    vetor.append(int(input("digite um numero")))

#passo 3(preenchero vetor)
for num in vetor:
    soma = soma + num 

print("a soma é ", soma)