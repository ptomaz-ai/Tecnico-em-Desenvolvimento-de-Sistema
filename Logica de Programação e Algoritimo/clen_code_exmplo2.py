notas = []

for i in range(4):
    #Tenta solicitar as notas
    try:
        nota = float(input(f"Digite a {i+1}ªnota: "))

        if(nota < 0 or nota > 10):
            print("Notas invalidas. Digite um numero de 1 a 10")
            exit()
        else:
            notas.append(nota)
#Se tiver algum erro (excesso)de valor, retorna uma mensagem
    except ValueError:
        print("erro:Insira um numero valido!")

#se a pessoa apenas digitou o texto
if not notas:
    print("Erro: Nenhuma nota foi inserida!")
else:
    media = sum(notas)/len(notas)

if(media >= 7):
    print(f"Média = {media} - Aprovado!")
elif(media >= 5):
    print(f"Média = {media} - Recuperaçao!")
else:
    print(f"Média = {media} - reprovado")
