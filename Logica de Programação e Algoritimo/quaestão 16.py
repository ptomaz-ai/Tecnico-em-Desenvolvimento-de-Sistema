numeros = []


for i in range(6):
    num = float(input("Digite o  número: "))
    
    
    if num < 0:
        numeros.append(1)
    else:
        numeros.append(num)


print("Lista final (negativos substituídos por 1):")
print(numeros)