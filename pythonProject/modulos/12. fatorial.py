def fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

if __name__ == "__main__":
    valor = int(input("Digite um número para saber o seu fatorial: "))
    print(f"O fatorial de {valor} é igual a {fatorial(valor)}")