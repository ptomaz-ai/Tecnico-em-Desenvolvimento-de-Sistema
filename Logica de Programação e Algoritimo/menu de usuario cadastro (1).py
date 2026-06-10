#cdastro 
#listar
#deletar

usuarios = []
cortes = []

#----------------------------------------------------------------------------------
#------função menu usuarios-----

def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 4):
        print()
        print("------Menu Usuario------")
        print("1- Cadastrar usuário")
        print("2- Listar usuários")
        print("3- Deletar Usuários")
        print("4- Voltar")

        opcao_menu_usuario = int(input("Escolha uma opção: "))

        match opcao_menu_usuario:

            case 1:
                nome = input("Digite o nome: ")
                telefone = input("Digite o telefone: ")
                email = input("Digite o email: ")

                #criação do Json de usuario
                usuario = {
                    'nome':nome,
                    'telefone':telefone,
                    'email':email
                }
                
                usuarios.append(usuario)
                print(f"usuarios{usuario['nome']} cadstro com sucesso!")

                #listar usuarios

            case 2:
                print("\n Listar de usuarios : ")

                if(len(usuarios) == 0):
                    print("nenhum usuario cadastrado!")

                else:
                    for usu in usuarios:
                        print("---------------------------------------------")
                        print("nome :", usu["nome"])
                        print("telefone:", usu["telefone"])
                        print("email: ", usu["email"])

            case 3 :
                nome_deletar = input("Digite o nome do usuário que deseja deletar: ")
                encontrado = False

                for usu in usuarios:
                    if(usu['nome'] == nome_deletar):
                        usuarios.remove(usu)
                        encontrado = True
                        print("Usuario removido com sucesso!!!")

                if(encontrado == False):
                    print("Usuário não encontrado! ")

                        #voltar ao menu principal

            case 4:
                print("Voltando ao menu principal...")
                break

#----------------------------------------------------------------------------------
#------função menu usuarios-----

def menu_cortes():
    opcao_menu_corte = 0

    while(opcao_menu_corte != 5):
        print()
        print("------Menu dos cortes de cabelo------")
        print("1- Cadastrar um corte ou penteado")
        print("2- Listar cortes/penteados ")
        print("3- Deletar cortes/penteados")
        print("4- Voltar")

        opcao_menu_cortes = int(input("Escolha uma opção: "))

        match opcao_menu_cortes:

            case 1:
                nome = input("Digite o nome: ")
                descricao = input("Digite a descrição: ")
                tempo = float(input("Digite o tempo do corte: "))
                valor = float(input("Digite o valor: "))

                #criação do Json de produto
                corte = {

                    'nome':nome,
                    'descricao':descricao,
                    'tempo':tempo,
                    'valor': valor
                }
                
                cortes.append(corte)
                print(f"produto{corte['nome']} cadstro com sucesso!")

                #listar produtos

            case 2:
                print("\n Listar de produtos : ")

                if(len(cortes) == 0):
                    print("nenhum produto cadastrado!")

                else:
                    for cor in cortes :
                        print("---------------------------")
                        print("nome :", cor["nome"])
                        print("Descrição :", cor["descricao"])
                        print("Tempo : ", cor["tempo"])
                        print("valor : ", cor["valor"])

            case 3 :
                nome_deletar = input("Digite o nome do corte/penteado que deseja deletar: ")
                encontrado = False

                for cor in cortes:
                    if(cor['nome'] == nome_deletar):
                        cortes.remove(cor)
                        encontrado = True
                        print("Tipo de corte removido com sucesso!!!")

                if(encontrado == False):
                    print("Este corte não  foi encontrado! ")

                        #voltar ao menu principal
#----------------------------------------------------------------------------------------terminar

            case 4:
                print("Voltando ao menu principal...")
                break


#----------------------------------------------------------------------------------
#-----menu principal-----

opcao_menu = 0
while(opcao_menu != 3):

    print("----- Menu - Sistema de cadatro -----")
    print("Oções:")
    print("1-Usuário")
    print("2-cortes")
    print("3-Sair")
    opcao_menu = int(input("Escolha uma opção: "))

    match opcao_menu:
        case 1:
            menu_usuarios()
            #menu do produto
        case 2:
            menu_cortes()
        case 3:
            print("Ate logo!")
        case _:
            print("❌")

