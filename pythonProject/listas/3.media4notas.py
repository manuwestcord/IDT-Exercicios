notas = []
somaNotas = 0
for i in range(4):
    nota = float(input(f"Digite a {i + 1}° nota: "))
    notas.append(nota)
    somaNotas += nota

media = somaNotas/4
print(f"As notas são {notas}")
print(f"A média da soma das 4 notas entregues é de: {media:.2f}")