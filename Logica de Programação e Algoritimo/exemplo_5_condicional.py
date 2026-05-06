idade = int(input("Digite sua idade: "))
carteira = input("você tem CNH?")

if(idade >= 18 and carteira == "sim"):
    print("voce pode dirigir!")
elif(idade >= 18 and carteira == "Não"):
    print("você nao pode dirigir!") 
elif(idade < 18 ):
    print("você não pode tirar sua CNH")
else:
    print("ERRO!")           