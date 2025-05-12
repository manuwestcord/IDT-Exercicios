def divisao(dividendo, divisor):
    quociente = 0
    for i in range(1, dividendo):
        if i * divisor == dividendo:
            quociente = i
        elif i * divisor < dividendo:
            quociente = i

    return quociente

def restoDivisao(dividendo, divisor):
    quociente = 0
    for i in range(1, dividendo):
        if i * divisor <= dividendo:
            quociente = i
    total = divisor * quociente
    resto = dividendo - total
    return resto

if __name__ == "__main__":
    continuar = True

    while continuar:
        dividendo = int(input("Digite o valor do dividendo(digite 0 para parar): "))
        if dividendo == 0:
            continuar = False
        else:
            divisor = int(input("Digite o valor do divisor: "))

            print(f"O quociente da divisão de {dividendo} por {divisor} é igual a "
                  f"{divisao(dividendo, divisor)} e o resto é {restoDivisao(dividendo, divisor)}")
