#revisão matriz 1
#solicitar a qunatidade de linhas
#solicitar a quantidades de colunas
#preencher matriz
#calcular a soma de todos os numeros
#--------------------------------------------------------

#passo 1(variaveis)
linhas = int(input("digite a quatidades de linhas: "))
colunas = int(input("digite as quantidades de colunas"))
matriz = []
soma = 0

#passo 2(preencher matriz)
#sempre repitir quando preencher a matriz

linha = []
for j in range(colunas):
    linha.apped(int(input("digite um numero")))
matriz.append(linhas)

#passo 39percorrer a matriz  a coluna soma
#senpre repitir quando for percorre a matriz
for i in range(linhas):
    for j in range(colunas):
        soma=soma+matriz[i][j]
print("a soma é:", soma)