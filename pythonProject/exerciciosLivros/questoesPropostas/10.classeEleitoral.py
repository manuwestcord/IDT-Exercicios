idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("Não votante")
elif 16 <= idade <= 17 or idade > 70:
    print("Eleitor facultativo")
elif 18 <= idade <= 69:
    print("Eleitor obrigatório")
else:
    print("Idade inválida")