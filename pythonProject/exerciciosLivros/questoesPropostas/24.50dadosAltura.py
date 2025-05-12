maiorAltura = 0
menorAltura = float('inf')
somaAlturaMulheres = 0
somaAlturaHomens = 0
quantidadeMulheres = 0
quantidadeHomens = 0
quantidadeAlunos = int(input("Digite a quantidade de alunos: "))
maiorNome = ""
menorNome = None

for i in range(quantidadeAlunos):
    print(f"Pessoa {i + 1}:")

    nome = input("Digite o nome do aluno: ")

    if menorNome is None or len(nome) < len(menorNome):
        menorNome = nome
    if len(nome) > len(maiorNome):
        maiorNome = nome

    altura = float(input("Digite a altura (em metros): "))

    sexo = input("Digite o sexo (M para masculino, F para feminino): ").upper()

    if altura > maiorAltura:
        maiorAltura = altura
    if altura < menorAltura:
        menorAltura = altura

    if sexo == 'F':
        somaAlturaMulheres += altura
        quantidadeMulheres += 1
    elif sexo == 'M':
        somaAlturaHomens += altura
        quantidadeHomens += 1

if quantidadeMulheres > 0:
    mediaAlturaMulheres = somaAlturaMulheres / quantidadeMulheres
else:
    mediaAlturaMulheres = 0

if quantidadeHomens > 0:
    mediaAlturaHomens = somaAlturaHomens / quantidadeHomens
else:
    mediaAlturaHomens = 0

totalPessoas = quantidadeHomens + quantidadeMulheres

if totalPessoas > 0:
    percentualHomens = (quantidadeHomens / totalPessoas) * 100
    percentualMulheres = 100 - percentualHomens

else:
    percentualHomens = 0
    percentualMulheres = 0

print(f"A maior altura do grupo é: {maiorAltura:.2f} metros")
print(f"A menor altura do grupo é: {menorAltura:.2f} metros")
print(f"A média de altura das mulheres é: {mediaAlturaMulheres:.2f} metros")
print(f"A média de altura dos homens é: {mediaAlturaHomens:.2f} metros")
print(f"O número de homens é: {quantidadeHomens}")
print(f"O número de mulheres é: {quantidadeMulheres}")
print(f"A diferença percentual entre homens e mulheres é: {abs(percentualHomens - percentualMulheres):.2f}%")
print(f"O menor nome é: {menorNome}")
print(f"O maior nome é: {maiorNome}")

