caractere = ""
consoantes = ""
contadorConsoantes = 0

for i in range(10):
    caractere = input("Digite um caractere: ").lower()

    if caractere not in 'aeiou':
        consoantes += caractere + ", "
        contadorConsoantes += 1

print(f"\nTotal de consoantes lidas: {contadorConsoantes}")
print("Consoantes:", consoantes)


