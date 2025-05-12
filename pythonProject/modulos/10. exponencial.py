def exponencial(base, exponente):
    resultado = base ** exponente

    return resultado

if __name__ == "__main__":
    base = int(input("Digite um valor para a base: "))
    expoente = int(input("Digite um valor para o expoente: "))

    print(f"A exponenciação entre {base} elevado na {expoente} é igual a {exponencial(base, expoente)}")