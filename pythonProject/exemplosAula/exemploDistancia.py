def entradaDados():
    mat = [[0 for _ in range(4)]for _ in range(4)]
    for i in range(4):
        for j in range(4):
            mat [i][j] = input(f"Digite a valor da distância da posição {i,j}: ")

    vet = ["" for _ in range(4)]
    for i in range(4):
        vet[i] = input(f"Digite o nome da cidade da posição [{i}]").upper()

    return mat, vet

def entradaCidades(cidadesAtendidas):
    cidade1 = ""
    cidade2 = ""
    repetir = True

    while repetir == True:
        cidade1 =  input("Digite o nome da cidade de origem: ").upper()
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
    cidade1, cidade2 = entradaCidades(vet)
    posicao1 = buscaPosicaoVetor(vet, cidade1)
    posicao2 = buscaPosicaoVetor(vet, cidade2)

    print(f"A distância entre a cidade {cidade1} e a {cidade2} é de {mat[posicao1][posicao2]}", end= "KM")

