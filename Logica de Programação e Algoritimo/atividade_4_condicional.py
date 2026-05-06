lado1 = float(input("digite o primeiro lado"))
lado2 = float(input("digite o segundo lado"))
lado3 = float(input("digite o terceiro lado"))

if((lado1+lado2) > lado3 and (lado1+lado3) > (lado2+lado3) > lado1):
    if(lado1 == lado2 and lado2 == lado3 and lado3v== lado1):
        print("equilátero")

    elif(lado1 != lado2 and lado2 != lado3 and lado3 != lado1):
        print("escaleno")

    else:
        print("isosceles")

        print("o triângulo não existe!")