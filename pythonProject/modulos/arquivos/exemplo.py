def lerArquivo(nome):
    arquivo = open(nome, "r")
    conteudo = arquivo.read()
    arquivo.close()
    return conteudo

def gravarArquivo(nome, adicionar):
    conteudo = lerArquivo(nome)
    arquivo = open(nome, "w")
    print(conteudo)
    conteudo = conteudo + adicionar
    arquivo.write(conteudo)
    arquivo.close()

if __name__ == "__main__":
    conteudo = lerArquivo("arquivo.txt")
    print(conteudo)

    conteudoNovo = "\nSamuel insuportável"
    gravarArquivo("arquivo.txt", conteudoNovo)