numeros = []
media = 0
soma = 0

for i in range(4):
    num = int(input("Digite uma numero: "))
    numeros.append(num)

for numero in numeros:
    soma = soma + numeros

media = soma /4
print("A media é ",media)

if(media < 4):
    print("reprovado! ")

elif(media > 4 and media < 7):
    print("recuperação! ")

else:
    print("reprovado! ")