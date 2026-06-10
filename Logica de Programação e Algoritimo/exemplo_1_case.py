print("----- Menu de Opção -----")
print("1 - Círculo")
print("2 - Trinângulo")
print("3 - Quadrado")
opcao = int(input("Digite uma opção: "))

match opcao:
    case 1:
        print("🏐")
    case 2 :
        print("🔼")
    case 3 :
        print("⏹️")
    case _ :
        print("❌ Opção Inválida")
