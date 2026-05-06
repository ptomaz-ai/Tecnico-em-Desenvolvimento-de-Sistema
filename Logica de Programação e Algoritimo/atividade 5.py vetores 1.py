numero_digitado = []
vetor = []


for i in range(8):
    num = int(input("Digite uma vetor: "))
    vetor.append(num)

numero_digitado = int(input("Digite um numero para procurar no vetor: "))

for i in range(8):
    if(vetor[i] == numero_digitado):
        print("encontrou")