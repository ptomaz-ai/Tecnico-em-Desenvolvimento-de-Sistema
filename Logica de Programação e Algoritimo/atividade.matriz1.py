matriz1 = []
matriz2 = []
matriz_soma = []

#prencher matriz(repetir sempre que prenecher matriz)

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(F"M[{i}][{j}] = ")))
    matriz1.append(linha)

#prencher matriz(repetir sempre que prenecher matriz)

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(F"M[{i}][{j}] = ")))
    matriz2.append(linha)

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz1[i][j]+matriz2[i][j])
    matriz_soma.append(linha)
    matriz2.append(linha)

#prencher matriz(repetir sempre que prenecher matriz)
print("matriz soma:")
for linha in matriz_soma:
    print(linha)







