quantEntrada = int(input("Digite a quantidade de alunos: "))
alunos = ["" for _ in range(quantEntrada)]
idade = [0 for _ in range(quantEntrada)]
altura = [0.0 for _ in range(quantEntrada)]

#entrada
for i in range(quantEntrada):
    alunos[i] = str(input(f"Digite o nome do aluno {i+1}: "))
    idade [i] = int (input(f"Digite a idade do aluno {i+1}: "))
    altura [i] = float(input(f"Digite a altura do aluno {i+1}: "))


maiorAltura = altura[0]
menorAltura = altura[0]
maiorNome = alunos[0]
menorNome = alunos[0]
maiorIdade = idade[0]
menorIdade = idade[0]
somaAltura = 0
somaIdade = 0
#processamento
for i in range (quantEntrada):
    somaAltura += altura[i]
    somaIdade += idade[i]

    if altura[i] > maiorAltura:
        maiorAltura = altura[i]


    if altura[i] < menorAltura:
        menorAltura = altura[i]

    if len(alunos[i]) > len(maiorNome):
        maiorNome = alunos[i]

    if len(alunos[i]) < len(menorNome):
        menorNome = alunos[i]

    if idade[i] > maiorIdade:
        maiorIdade = idade[i]

    if idade[i] < menorIdade:
        menorIdade = idade[i]

mediaAltura = somaAltura / len(altura)
mediaIdade = somaIdade / len(idade)
#saida
for i in range (quantEntrada):
    print(f"O aluno {alunos[i]} tem a idade {idade[i]} e a altura {altura[i]}")

print (f"A maior altura é {maiorAltura}")
print(f"A menor altura é {menorAltura}")
print(f"O maior nome é {maiorNome}")
print(f"O menor nome é {menorNome}")
print(f"A maior idade é {maiorIdade}")
print(f"A menor idade é {menorIdade}")
print(f"A média das idades é de {mediaIdade}")
print(f"A média das alturas é de {mediaAltura}")