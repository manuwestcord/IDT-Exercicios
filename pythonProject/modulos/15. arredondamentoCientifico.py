def arredondamento_cientifico(valor, precisao):
    if valor == 0:
        return 0
    else:
        # Converte o valor para string em notação científica e arredonda com a precisão desejada
        valor_arredondado = f"{valor:.{precisao}g}"
        return float(valor_arredondado)


if __name__ == "__main__":
    valor = float(input("Digite o valor fracionário: "))
    precisao = int(input("Digite o número de dígitos significativos: "))

    resultado = arredondamento_cientifico(valor, precisao)
    print(f"O valor {valor} arredondado cientificamente com {precisao} dígitos significativos é: {resultado}")