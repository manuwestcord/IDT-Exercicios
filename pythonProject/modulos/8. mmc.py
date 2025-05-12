def mmc(valor1, valor2):
    if valor1 == 0 or valor2 == 0:
        return 0

    if valor1 > valor2:
        mmc = valor1

    else:
        mmc = valor2

    while mmc % valor1 != 0 or mmc % valor2 != 0:
        mmc += 1
    return mmc

if __name__ == "__main__":
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))

    print(f"O mmc entre {num1} e {num2} é igual a {mmc(num1, num2)}")