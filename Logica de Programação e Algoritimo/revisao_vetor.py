saltos = []

for i in range(7):
    saltos.append(int(input("digite o valor do salto")))

#todos os saltos na ordem em que foram realizados

print(saltos)

# Maior
maior = saltos[0]

for salto in saltos:
    if(salto > maior):
        maior = salto

print("o maior salto é: ", maior)

# Menor
menor = saltos[0]

for salto in saltos:
    if(salto < menor):
        menor = salto

print("o menor salto é: ", menor)

# média sem maior e menor
soma = 0 

for salto in saltos:
    if(salto != maior and saltos != menor):
        soma = soma = saltos
media = soma / 5 
print(" A média sem maior e menor é: ", media)

# media geral 
soma = 0 

for salto in saltos:
    soma = soma + saltos
media_geral = soma / 7 
print("A média geral é: " , media_geral)