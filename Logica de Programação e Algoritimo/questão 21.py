soma_pares = 0

for i in range(8):
    num = int(input("Digite um número: "))
    if(num %2 == 0):
        soma_pares += num

print("O valor da soma dor numeros pares são: ",soma_pares)