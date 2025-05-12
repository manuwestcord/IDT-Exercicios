def numeroAbsoluto(valor):
    if valor < 0:
        return -valor
    else:
        return valor

if __name__ == "__main__":
    valor = int(input("Digite um número para saber o seu absoluto: "))
    print(f"O valor absoluto de {valor} é igual a {numeroAbsoluto(valor)}")