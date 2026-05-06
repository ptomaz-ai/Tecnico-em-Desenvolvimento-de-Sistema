notas = []

for i in range(4):
    notas.append(int(input(f"Digite a {i+1}ªnota: ")))

media = sum(notas)/len(notas)

print("Sua média é:",media)
    