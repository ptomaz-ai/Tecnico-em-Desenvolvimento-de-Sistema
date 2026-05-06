matriz = [
[5 , 8 , 2] ,
[7 , 3 , 10] ,
[6 , 1 , 4]
]

resultado = 0

for i in range (3) :
    for j in range (3) :
        if i == j :
            resultado += matriz [ i ][ j ]
        elif matriz [ i ][ j ] % 2 == 0:
            resultado += matriz [ i ][ j ] // 2
        else :
         resultado -= matriz [ i ][ j ]

        if resultado % 3 == 0:
            resultado += 2
        else :
            resultado -= 1

print ( resultado )