texto = input("digite um texto: ")


for letra in texto:
    print(letra)


qtd_caracteres = 0

for letra in texto:
    if(letra != " "):
        qtd_caracteres+=1
print("a quantidade de caracteres é: ", qtd_caracteres)


vogais = "aeiouAEIOUáàãâÁÀÃÂéèêÉÈÊíìîÍÌÎóòõôÓÒÕÔúùûÚÙÛ"
qtd_vogais = 0

for vogal in vogais:
    for letra in texto:
        if(letra == vogal):
            qtd_vogais+=1
print("a quantidade de vogais é: ", qtd_vogais)
