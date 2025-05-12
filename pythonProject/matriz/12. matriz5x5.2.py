matriz = [[""for _ in range(5)] for _ in range(5)]
trianguloSuperior = 0

for i in range(5):
    for j in range(5):
        matriz [i][j] = int(input(f"Digite o valor da posição ({i},{j}): "))

#for i in range(5):
    #print(matriz[i])
for i in range(5):
    print(f"A diagonal principal é composta por {matriz[i][i]} na posição {[i],[i]}")
print("\n")

for i in range(5):
    for j in range(5):
        if j > i:
            print(f"O triângulo superior da diagonal principal é composto por {matriz[i][j]} na posição {[i],[j]}")
print("\n")

for i in range(5):
    for j in range(5):
        if j < i:
            print(f"O triângulo inferior da diagonal principal é composto por {matriz[i][j]} na posição {[i],[j]}")
print("\n")

for i in range(5):
    for j in range(5):
        if i != j:
            print(f"A matriz sem a diagonal principal é composta por {matriz[i][j]} na posição {[i], [j]} ")
print("\n")

#for i in range(5):
 #   for j in range(5):
  #      if i + j == 4:
   #         print(f"A diagonal secundária é composta por {matriz [i][j]} na posição {[i],[j]}")
#print("\n")
contInver = len(matriz) -1
for i in range(len(matriz)):
    print(f"A diagonal secundária é composta por {matriz[i][contInver]}")
    contInver -= 1
print("\n")

for i in range(5):
    for j in range(5):
        if i + j < 4:
            print(f"O triângulo superior da diagonal secundária é composta por {matriz[i][j]} na posição {[i],[j]}")
print("\n")

for i in range(5):
    for j in range(5):
        if i + j > 4:
            print(f"O triângulo inferior da diagonal secundária é composta por {matriz[i][j]} na posição {[i],[j]}")
print("\n")

for i in range(5):
    for j in range(5):
        if i + j != 4:
            print(f"A matriz sem a diagonal secundária é composta por {matriz [i][j]} na posição {[i],[j]}")