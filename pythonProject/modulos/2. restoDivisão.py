def restoDivisao(numero, divisor, quociente):
    for i in range(1, numero):
        if i * divisor <= numero:
            quociente = i
    total = divisor * quociente
    resto = numero - total
    return resto

if __name__ == "__main__":
    dividendo = int(input("Digite o valor do dividendo: "))
    divisor = int(input("Digite o valor do divisor: "))
    quociente = 0

    print(f"O resto de {dividendo} divido por {divisor} é igual a {restoDivisao(dividendo, divisor, quociente)}")