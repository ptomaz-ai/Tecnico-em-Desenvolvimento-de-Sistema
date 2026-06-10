#Sistema de cadastro de usuario e produtos
#o sistema devera permirtir 
#cadastrar 
#lista
#detetar

#criação das lista
usuarios = []
produtos = []

#-----------------------------------------------
# ----- função menu usuarios -----
def menu_usuarios():
    opcao_menu_usuario = 0

    while(opcao_menu_usuario != 4):
        print()
        print(" ----- menu Usuario -----")
        print("1 - cadastro de usuario")
        print("2 - lista de usuario")
        print("3 - deletar usuario")
        print("4 - voltar")

        opcao_menu_usuario = int(input("escolha uma opção "))

        match opcao_menu_usuario:
            # cadastro Usuario
            case 1:
                Nome = input("digite o nome: ")
                telefone = input("digite o telefone: ")
                email = input("digite o email: ")

                #criação de json de usuário (cahve: vertor)
                usuario = {
                    "nome": Nome,
                    "telefone": telefone,
                    "email": email
                }

                # adicionar o json no array
                usuarios.append(usuario)
                print(f"usuario {usuario['nome']}cadstro com sucesso!")
            # lista usuario
            case 2:
                print("\n lista de Usuário: ")
                if(len(usuarios) == 0 ):
                    print("nenhum usuário cadastrado!")
                else:
                    for usu in usuarios:
                        print("--------")
                        print("nome: ", usu["nome"])
                        print("telefone: ", usu["telefone"])
                        print("email: ", usu["email"])
            #deletar usuario
            case 3:
                nome_deletar = input("digite o nome do usuario que deseja deletar: ")
                encontrado = False

                for usu in usuario:
                    if(usu["nome"] == nome_deletar):
                        usuarios.remove(usu)
                        encotrado = True
                        print("usuario removido com sucesso!")

                if(encontrado == False):
                    print("usuario removido com sucesso!")
            # volta ao menu principal
            case 4:
                print("voltar ao menu principal...")
                break
#-----------------------------------------------
# ----- função menu produtos -----
def menu_produtos():
    opcao_menu_produto = 0

    while(opcao_menu_usuario != 5):
        print()
        print(" ----- menu produtos -----")
        print("1 - cadastro de produto")
        print("2 - lista de produtos")
        print("3 - deletar produto")
        print("4 - calcular total")
        print("5 - voltar")

        opcao_menu_produto = int(input("escolha uma opção "))

        match opcao_menu_produto:
            # cadastro Usuario
            case 1:
                Nome = input("digite o nome: ")
                descricao = input("digite o descrição: ")
                quantidade = input("digite o quntidade: ")
                valor = float(input("digite o valor"))

                #criação de json de usuário (cahve: vertor)
                produto = {
                    "nome": Nome,
                    "descrição": descricao,
                    "quantidade": quantidade,
                    "valor": valor
                }

                # adicionar o json no array
                produtos.append(produto)
                print(f"uproduto {produto['nome']}cadstro com sucesso!")
            # lista produto
            case 2:
                print("\n lista de produtos: ")
                if(len(usuarios) == 0 ):
                    print("nenhum produto cadastrado!")
                else:
                    for pro in produtos:
                        print("--------")
                        print("nome: ", pro["nome"])
                        print("descrição: ", pro["descrição"])
                        print("quantidade: ", pro["quantidade"])
                        print("valor: ", pro["valor"])
            #deletar usuario
            case 3:
                nome_deletar = input("digite o nome do produto que deseja deletar: ")
                encontrado = False

                for pro in produto:
                    if(pro["nome"] == nome_deletar):
                        usuarios.remove(pro)
                        encotrado = True
                        print("produto removido com sucesso!")

                if(encontrado == False):
                    print("produto removido com sucesso!")
            # volta ao menu principal
            case 5:
                print("voltar ao menu principal...")
                break



#-----------------------------------------------
# ----- menu principal -----
opcao_menu = 0
while(opcao_menu != 3):
    print("----- menu - sistema de cadastro -----")
    print("Opções: ")
    print("1 - Usuarios")
    print("2 - produtos")
    print("3 - Sair")
    opcao_menu = int(input("Escolha uma opção "))

    match opcao_menu:
        # menu usuario
        case 1:
            menu_usuarios()
        #menu produtos
        case 2:
            menu_produtos()
        case 3:
            print("até logo")
        case _:
            print("opção invalida")
