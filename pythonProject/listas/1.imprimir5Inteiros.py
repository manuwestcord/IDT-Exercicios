if __name__ == "__main__":
    numeros = []

    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)

    print(f"Os números digitados foram: {numeros}")
