numeros = []

for i in range(5):
    #Tenta solicitar as notas
    try:
        numero = float(input(f"Digite a {i+1}ªnumero: "))

        if(numero < 0 or numero > 9999999999999999999999999999999999):
            print("Notas invalidas. Digite um numero de 1 a 10")
            exit()
        else:
            numeros.append(numero)
    except ValueError:
        print("erro:Insira um numero valido!")
if not numero:
    print("Erro: Nenhuma nota foi inserida!")
else:
    media = sum(numero)/len(numero)