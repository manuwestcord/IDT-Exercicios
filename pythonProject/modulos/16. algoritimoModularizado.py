# a) Função para entrada de dados no vetor
def digitarValores():
    vetor = []
    for i in range(100):
        valor = int(input(f"Digite o valor {i+1}: "))
        vetor.append(valor)
    return vetor

# b) Função para somar os valores do vetor
def somatorio(vetor):
    soma = 0
    for valor in vetor:
        soma += valor
    return soma

# c) Função para calcular a média dos valores
def media(vetor):
    return somatorio(vetor) / len(vetor)

# d) Função para calcular o desvio-padrão (sem math.sqrt)
def desvioPadrao(vetor):
    med = media(vetor)
    somaVariancia = 0
    for x in vetor:
        somaVariancia += (x - med) ** 2
    variancia = somaVariancia / len(vetor)

    # Calcula a raiz quadrada manualmente usando o método de aproximação
    raizQuadrada = variancia
    for _ in range(20):  # Mais iterações aumentam a precisão
        raizQuadrada = (raizQuadrada + variancia / raizQuadrada) / 2
    return raizQuadrada

# e) Função para substituir valores negativos por zero de forma mais simples
def substituirNegativos(vetor):
    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor[i] = 0
    return vetor

# f) Função para substituir valores repetidos maiores que zero por zero de forma mais simples
def substituirRepetidos(vetor):
    for i in range(len(vetor)):
        for j in range(i + 1, len(vetor)):
            if vetor[i] == vetor[j] and vetor[i] > 0:
                vetor[j] = 0
    return vetor


if __name__ == "__main__":
    vetor = digitarValores(10)  # Alterado para 10 entradas para facilitar testes

    print(f"Somatório: {somatorio(vetor)}")
    print(f"Média: {media(vetor)}")
    print(f"Desvio-padrão: {desvioPadrao(vetor)}")

    vetorSemNegativos = substituirNegativos(vetor)
    print(f"Vetor com valores negativos substituídos por zero: {vetorSemNegativos}")

    vetorSemRepetidos = substituirRepetidos(vetorSemNegativos)
    print(f"Vetor com valores repetidos (maiores que zero) substituídos por zero: {vetorSemRepetidos}")

