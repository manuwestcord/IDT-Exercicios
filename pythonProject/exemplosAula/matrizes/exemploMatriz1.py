matriz1 = [["" for _ in range(3)] for _ in range (3)]
matriz2 = [["" for _ in range(3)] for _ in range(3)]
matriz3 = [["" for _ in range(3)] for _ in range(3)]

for i in range (3):
    for j in range (3):
        matriz1[i][j] = int(input(f"Digite um valor para a matriz1 [{i}, {j}]: "))

for i in range(3):
    for j in range(3):
        matriz2[i][j] = int(input(f"Digite um valor para a matriz2 [{i}, {j}]: "))

for i in range(3):
    for j in range(3):
        matriz3[i][j] = matriz1[i][j] + matriz2[i][j]

for i in range(3):
    print(matriz3[i])

