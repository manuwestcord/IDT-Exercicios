dataAniversario = str(input("Digite a data do seu aniversário (dd/mm/aaaa): "))
dataAtual = str(input("Digite a data do dia atual (dd/mm/aaaa): "))

diaAniversario, mesAniversario, anoAniversario = map(int, dataAniversario.split("/"))
diaAtual, mesAtual, anoAtual = map(int, dataAtual.split("/"))

anos = anoAtual - anoAniversario
meses = mesAtual - mesAniversario
dias = diaAtual - diaAniversario

if dias < 0:
    meses -= 1
    dias += 30

if meses < 0:
    anos -= 1
    meses += 12

print(f"Você tem {anos} anos, {meses} meses e {dias} dias.")