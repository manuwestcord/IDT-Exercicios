caractere = ["" for _ in range(10)]
consoantes = ["" for _ in range(10)]
contadorConsoantes = 0

for i in range(10):
    caractere = input("Digite um caractere: ").lower()

if caractere[i].isalpha() and caractere not in 'aeiou':
    consoantes[contadorConsoantes] = caractere[i]
    contadorConsoantes += 1

parar = False
i = 0
while not parar:
    if consoantes[i] == "":
        ultPosicao = i
        parar = True
    i += 1
print(ultPosicao)
print(consoantes[ultPosicao])

print(f"\nForam lidos {contadorConsoantes} consoantes.")

print("As consoantes são: ", end = "")
for i in range(ultPosicao):
    if i == ultPosicao - 1:
        print(consoantes[i], end = "")
    else:
        print(consoantes[i], end = ", "
                                   "")