num1 = int(input("Digite um número: "))
num2 = int(imput("Digite outro número: "))
operacao = input("Digite a operação (+,-,*,/): ")

if(operacao == "+"):
    resultado = num1+num2
elif(operacao == "-"):
    resultado = num1-num2
elif(operacao == "*"):
    resultado = num1*num2
 elif(operacao == "/"):
    resultado = num1/num2 
else:
    resultado = "ERRO"   
print("O resultado é: ,resultado")               