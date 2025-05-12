# Um dado comerciante malico cobra 10% de acréscimo para cada prestação em atraso e depois da um desconto de 10% sobre
# esse valor. Faça um algoritimo que solicite o valor da prestação em atraso e apresente o valor final a pagar, assim
# como o prejuízo do comerciante na operação.

valorPrestacao = float(input("Digite o valor da prestação em atraso: "))

acrescimo = valorPrestacao * 0.1
valorAumento = valorPrestacao + acrescimo
desconto = valorAumento * 0.1
valorFinal = valorAumento - desconto
prejuizo = valorPrestacao - valorFinal

print(f"O valor final da prestação será de R$ {valorFinal:.2f} e o prejuízo levado pelo comerciante é de R$ {prejuizo:.2f}")