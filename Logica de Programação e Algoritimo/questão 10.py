numeros = []

for i in range(6):
    numeros.append(int(input("digite um numero")))

for num in numeros:
    if(num %2 == 0):
        print(num)