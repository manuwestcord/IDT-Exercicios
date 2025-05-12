def entradaDados():
    mat = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mat[i][j] = int(input(f'Digite um valor para posição [{i}, {j}]: '))

    vet = ["" for _ in range(4)]
    for i in range(4):
        vet[i] = input(f"Digite a cidade da posição [{i}]: ")

    return mat, vet

def matriz_auxiliar():
    mat = [
          [0, 77, 129, 232],
          [77, 0, 52, 155],
          [129, 52, 0, 103],
          [232, 155, 103, 0]
          ]
    vet = ["IBI", "BLU", "ITA", "FLN"]
    return mat, vet

def entradaDadosCidadesBusca(cidadesAtendidas):
    cidade1 = ""
    cidade2 = ""
    repetir = True
    while repetir == True:
        cidade1 = input("Digite o nome da cidade de origem: ").upper()
        if cidade1 in cidadesAtendidas:
            repetir = False
        else:
            print(f"Escolha uma cidade dentro das possibilidades: {cidadesAtendidas}")

    repetir = True
    while repetir == True:
        cidade2 = input("Digite o nome da cidade de destino: ").upper()
        if cidade2 in cidadesAtendidas:
            repetir = False
        else:
            print(f"Escolha uma cidade dentro das possibilidades: {cidadesAtendidas}")
    return cidade1, cidade2

def buscaPosicaoVetor(cidadesAtendidas, cidade):
    for i in range(4):
        if cidadesAtendidas[i] == cidade:
            return i

if __name__ == "__main__":
    mat, vet = entradaDados()
    #mat, vet = matriz_auxiliar()
    cidade1, cidade2 = entradaDadosCidadesBusca(vet)
    posicao1 = buscaPosicaoVetor(vet, cidade1)
    posicao2 = buscaPosicaoVetor(vet, cidade2)

    print(f"A distância entre a cidade {cidade1} e a {cidade2} é de ", end="")
    print(mat[posicao1][posicao2], end=" KM")








