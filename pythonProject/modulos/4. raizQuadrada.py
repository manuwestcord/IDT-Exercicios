def raizQuadrada (valor):
    raiz = valor ** 0.5

    return raiz

if __name__ == "__main__":
    continuar = True

    while continuar:
        numero = int(input("Digite um valor para saber a sua raiz quadrada(digite 0 para parar): "))
        if numero == 0:
            continuar = False
        else:
            print(f"A raiz quadrada de {numero} é igual a {raizQuadrada(numero):.2f}")