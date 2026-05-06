# solicite um texto para o usuario
texto = input("digite um texto qualquer: ")

# Exibir letra por letra do texto 
# para cada letra no texto
for letra in texto:
    print(letra)

# contar quantidade de caraquiteres != ''
qtd_caracteres = 0

for letra in texto:
    if(letra != " "):
        qtd_caracteres+=1
print("A quantidade de caraquiteras é: ", qtd_caracteres)

# contas as quantidades de vogais
vogais = "aeiouAEIOUáàãâÁÀÃÂéèêÉÈÊíìîÌÍÎóòõôÒÓÔÕÚÙÛúÙû"

qtd_vogais = 0 

for vogal in vogais:
    for letra in texto:
     if(letra == vogal):
        qtd_vogais+=1
print("a quntidade de vogais é:", qtd_caracteres)  

# palindromo
texto_invertido = ""

for i in range(len(texto)-1,-1,-1):
   texto_invertido = texto_invertido + texto[i]

if(texto == texto_invertido):
   print("É palindorme!")
else:
   print("Não é palindrome")