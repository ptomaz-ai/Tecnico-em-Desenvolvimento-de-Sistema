matriz = [
    ["laranja","romã","maça-verde","limão","caqui"],
    ["beringela","bateta","pimentão","pimenta","pepino"]    
]
print(matriz[0]) # imprime a primeira linha (frutas)
print(matriz[1]) # imprime a srgunda linha (legumes)

print(matriz[0][2]) #imprime maça-verde
print(matriz[1][3]) #imprime pimenta

print("frutas: ")
print(matriz[0][0])
print(matriz[0][1])
print(matriz[0][2])
print(matriz[0][3])
print(matriz[0][4])

print("legumes: ")
print(matriz[1][0])
print(matriz[1][1])
print(matriz[1][2])
print(matriz[1][3])
print(matriz[1][4])

print("matriz completa:")
for i in range(2): #linhas
    for j in range(5): #colunas
        print(matriz[1][j])