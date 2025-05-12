numeros = [0 for _ in range(20)]
listaPar = [0 for _ in range(20)]
listaImpar = [0 for _ in range(20)]

contadorPar = 0
contadorImpar = 0

for i in range(20):
    numeros[i] = int(input(f"Digite o {i + 1}° número: "))

    if numeros[i] % 2 == 0:
        listaPar[contadorPar] = numeros[i]
        contadorPar += 1
    else:
        listaImpar[contadorImpar] = numeros[i]
        contadorImpar += 1

listaPar = listaPar[:contadorPar]
listaImpar = listaImpar[:contadorImpar]

print("\nVetor de todos os números")
print(numeros)

print("\nVetor de todos os números impares")
print(listaImpar)

print("\nVetor de todos os números pares")
print(listaPar)

print(f"A lista impar é de {listaImpar}\n"f"A lista par é de: {listaPar}")