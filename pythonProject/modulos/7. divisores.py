def encontrarDivisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

if __name__ == "__main__":

    continuar = True
    valor = int(input("Digite um valor para saber os seus divisores(escreva 0 para parar): "))

    while valor == 0:
        continuar = False
    print(f"Os números divisores de {valor} são {encontrarDivisores(valor)}")