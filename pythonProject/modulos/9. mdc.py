def mdc(valor1, valor2):
    mdc = 1

    if valor1 == 0 or valor2 == 0:
        return 0

    if valor1 > valor2:
        aux = valor2
    else:
        aux = valor1

    for i in range(1, aux + 1):
        if valor1 % i == 0 and valor2 % i == 0:
            mdc = i
    return mdc

if __name__ == "__main__":
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))

    print(f"O mdc entre {num1} e {num2} é igual a {mdc(num1, num2)}")