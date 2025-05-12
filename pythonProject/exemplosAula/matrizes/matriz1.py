matriz = [["" for _ in range(5)] for _ in range (4)]

for i in range (4): #Linhas
    for j in range (5): #colunas
        matriz[i][j] = int(input(f"Digite um valor para [{i}, {j}]: "))
print(matriz)#toda matriz em uma linha

for i in range(4): #matriz em linhas individuais
    print(matriz [i])

for i in range(4): #linhas
    for j in range(5): #colunas
        print(matriz[i][j])

