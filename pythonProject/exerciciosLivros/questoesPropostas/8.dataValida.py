data = (input("Digite uma data dd/mm/aaaa: "))
dia, mes, ano = map(int, data.split("/"))
dataValida = True

if mes < 1 or mes > 12:
    print("Data incorreta!")
    dataValida = False

if ano < 1:
    print("Data incorreta!")
    dataValida = False

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia < 1 or dia > 31:
        print("Data incorreta!")
        dataValida = False

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia < 1 or dia > 30:
        print("Data incorreta!")
        dataValida = False

elif mes == 2:
    if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)):
        if dia < 1 or dia > 29:
            print("Data incorreta!")
            dataValida = False

    else:
        if dia < 1 or dia > 28:
            print("Data incorreta!")
            dataValida = False

if dataValida:
    print("Essa é uma data válida")

