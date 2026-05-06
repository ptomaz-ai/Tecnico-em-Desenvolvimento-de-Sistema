posicaoI = float (input("Qual a posição inicial: "))
posicaoF = float (input("Qual a posição final: "))
tempoI = float (input("Qual o tempo inicial: "))
tempoF = float (input("Qual o tempo final: "))

velocidademedia = (posicaoI-posicaoF)/(tempoI-tempoF)

print("A velocidade média é:", velocidademedia)