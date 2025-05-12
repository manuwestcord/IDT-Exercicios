matriz = [["" for _ in range(5)]for _ in range(5)]
somaImpar = 0
somaLinhas = 0

for i in range(5):
    for j in range(5):
        matriz [i][j] = int(input(f"Digite o valor para [{i}, {j}]: "))

#for i in range(5):
    #print( matriz [i])

for i in range(5):
    for j in range(5):
        if matriz[i][j] % 2 != 0:
            somaImpar += matriz[i][j]
print(f"\nA soma dos números ímpares desta matriz é de: {somaImpar}\n")

for j in range(5):
    somaColunas = 0
    for i in range(5):
        somaColunas += matriz[i][j]
    print(f"A soma da coluna {j} é de {somaColunas}")

for i in range(5):
    somaLinhas = 0
    for j in range(5):
        somaLinhas += matriz[i][j]
    print(f"A soma da linha {i} é de {somaLinhas}")