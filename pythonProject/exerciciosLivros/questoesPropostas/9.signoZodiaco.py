data = str(input("Digite o dia e mês de seu nascimento (dd/mm): "))

dia, mes = map(int, data.split("/"))

if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    print("O signo do zodíaco é: Aquário")
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    print("O signo do zodíaco é: Peixes")
elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    print("O signo do zodíaco é: Áries")
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    print("O signo do zodíaco é: Touro")
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    print("O signo do zodíaco é: Gêmeos")
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    print("O signo do zodíaco é: Câncer")
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    print("O signo do zodíaco é: Leão")
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    print("O signo do zodíaco é: Virgem")
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    print("O signo do zodíaco é: Libra")
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    print("O signo do zodíaco é: Escorpião")
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    print("O signo do zodíaco é: Sagitário")
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
    print("O signo do zodíaco é: Capricórnio")

