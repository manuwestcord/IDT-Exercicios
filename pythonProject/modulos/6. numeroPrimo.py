def numeroPrimo(valor):
    div = 0
    for i in range(1, valor + 1):
        if valor % i == 0:
            div += 1
    if div == 2:
        return True
    else:
        return False

if __name__ == "__main__":
    print("VERIFICADOR DE NÚMEROS PRIMOS:")
    sair = False
    while sair == False:
        numero = int(input("Digite um número para saber se é primo ou não(caso queira sair, digite 0): "))
        if numero == 0:
            sair = True
        else:
            if numeroPrimo(numero):
                print(f"O número {numero} é primo!")
            else:
                print(f"O número {numero} não é número primo")
