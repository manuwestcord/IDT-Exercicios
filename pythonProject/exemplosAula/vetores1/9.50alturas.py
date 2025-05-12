alturas = [0.0 for _ in range(5)]
somaAltura = 0
contRepetid = 0
somaQuadrados = 0
quant = int(input("Digite a quantidade de alturas que deseja colocar: "))

for i in range(quant):
    alturas[i] = float(input(f"Digite a {i + 1}° altura: "))
    somaAltura += alturas[i]
    somaQuadrados += alturas[i] ** 2

mediaAltura = somaAltura/quant
variancia = (somaQuadrados/ quant) - mediaAltura ** 2
desvioPadrao = variancia ** 0.5

moda = None
maxFreq = 1
for i in range(quant):
    frequenciaAtual = 1

    for j in range(i + 1, quant):
        if alturas[i] == alturas[j]:
            frequenciaAtual += 1

    if frequenciaAtual > maxFreq:
        maxFreq = frequenciaAtual
        moda = alturas[i]

for i in range(quant):
    for j in range(i,quant):
        if alturas[i] > alturas[j]:
            aux = alturas[j]
            alturas[j] = alturas[i]
            alturas[i] = aux



if(quant % 2 == 0):
    mediana = (alturas[int(quant/2) - 1] + alturas[int(quant/2)]) / 2

else:
    mediana = alturas[int(quant/2)]

print(f"\nA altura média é de: {mediaAltura:.2f}")
print(f"\nO desvio padrão é de: {desvioPadrao:.2f}")
print(f"\n A moda é de: {moda}")
print(f"\n A mediana é de: {mediana:.2f}")