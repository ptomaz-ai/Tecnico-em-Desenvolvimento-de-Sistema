idade = int(input("digite sua idade"))

if(idade >=0 and idade <=12):
    print("você é uma criança")
elif(idade >=13 and idade <=17):
    print("você é um adolecente")
elif(idade >=18 and idade <=59):
    print("você é um adulto")
elif(idade > 60 ):
    print("idoso")
else:
    print("erro")    