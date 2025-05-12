nome1 = input("Digite o nome do país 1: ")
ouro1 = int(input(f"Digite o número de medalhas de ouro para {nome1}: "))
prata1 = int(input(f"Digite o número de medalhas de prata para {nome1}: "))
bronze1 = int(input(f"Digite o número de medalhas de bronze para {nome1}: "))
pontos1 = ouro1 * 3 + prata1 * 2 + bronze1 * 1

nome2 = input("Digite o nome do país 2: ")
ouro2 = int(input(f"Digite o número de medalhas de ouro para {nome2}: "))
prata2 = int(input(f"Digite o número de medalhas de prata para {nome2}: "))
bronze2 = int(input(f"Digite o número de medalhas de bronze para {nome2}: "))
pontos2 = ouro2 * 3 + prata2 * 2 + bronze2 * 1

nome3 = input("Digite o nome do país 3: ")
ouro3 = int(input(f"Digite o número de medalhas de ouro para {nome3}: "))
prata3 = int(input(f"Digite o número de medalhas de prata para {nome3}: "))
bronze3 = int(input(f"Digite o número de medalhas de bronze para {nome3}: "))
pontos3 = ouro3 * 3 + prata3 * 2 + bronze3 * 1

if pontos1 >= pontos2 and pontos1 >= pontos3:
    print(f"1º lugar: {nome1} - {pontos1} pontos")
    if pontos2 >= pontos3:
        print(f"2º lugar: {nome2} - {pontos2} pontos")
        print(f"3º lugar: {nome3} - {pontos3} pontos")
    else:
        print(f"2º lugar: {nome3} - {pontos3} pontos")
        print(f"3º lugar: {nome2} - {pontos2} pontos")
elif pontos2 >= pontos1 and pontos2 >= pontos3:
    print(f"1º lugar: {nome2} - {pontos2} pontos")
    if pontos1 >= pontos3:
        print(f"2º lugar: {nome1} - {pontos1} pontos")
        print(f"3º lugar: {nome3} - {pontos3} pontos")
    else:
        print(f"2º lugar: {nome3} - {pontos3} pontos")
        print(f"3º lugar: {nome1} - {pontos1} pontos")
else:
    print(f"1º lugar: {nome3} - {pontos3} pontos")
    if pontos1 >= pontos2:
        print(f"2º lugar: {nome1} - {pontos1} pontos")
        print(f"3º lugar: {nome2} - {pontos2} pontos")
    else:
        print(f"2º lugar: {nome2} - {pontos2} pontos")
        print(f"3º lugar: {nome1} - {pontos1} pontos")

