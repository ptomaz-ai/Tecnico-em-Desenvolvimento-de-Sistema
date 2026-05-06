valorCompra = float(input("digite o valor da compra:"))
copomDescomto = input("possui cupom de descomto? ")

if(valorCompra >= 200 or copomDescomto == "sim"):
    print("vocé ganhou descomto de 15%! ")
else:
    print("você não tem direito a desconto no momento!")    