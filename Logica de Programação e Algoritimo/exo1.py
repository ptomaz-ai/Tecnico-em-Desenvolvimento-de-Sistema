#  importar as bibliotecas
import pandas as pd
import os

dados = {
    "Nome":   [],
    "Diciplina":  [],
    "Nota": []
}
deseja_continuar = ""

while(deseja_continuar != "n"):
    print("\n Digite os dados: ")
    Nome = input("Nome: ")
    Diciplina = int(input("Diciplina: "))
    Nota = input("Nota: ")
    

    dados["Nome"].append(Nome)
    dados["Diciplina"].append("Diciplina")
    dados["Nota"].append("nota")

    deseja_continuar = input("deseja_continuar? (s/n)").strip().lower()
    #istrip()-> tirar espassos em branco
    #lower()-> transformar em minúsculo

df = pd.DataFrame(dados)
print(df)


escolha_arquivo = input("Digite o numero do formato desejado: ")
os.chdir("C:\\Users\\50365627801\\Documents\\leitura_manipulacao_exo1\\")

df.to_csv("dados.txt", sep="\t", index=False)
print("dados salvos em 'dados.txt'!")
try:
    df_lido = pd.read_csv("dados.txt", sep="\t")
    print(df_lido)
except FileNotFoundError:
        print("\n arquivo não encontrado!")




