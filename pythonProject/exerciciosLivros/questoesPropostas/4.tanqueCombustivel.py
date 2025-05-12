capacidadeTanque = float(input("Informe a capacidade total do tanque (em litros): "))
litrosAbastecidos = float(input("Informe a quantidade de litros abastecidos: "))
quilometragemPercorrida = float(input("Informe a quilometragem percorrida desde o último abastecimento: "))

consumoMedio = quilometragemPercorrida / litrosAbastecidos

autonomiaRestante = (capacidadeTanque - litrosAbastecidos) * consumoMedio

print(f"O consumo médio foi de {consumoMedio:.2f} km/l.")
print(f"A autonomia que o carro ainda teria antes do abastecimento era de {autonomiaRestante:.2f} km.")
