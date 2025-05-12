def divisivel6(numero):
    if numero % 6 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    continuar = True
    while continuar:
        num = int(input("Digite um número para saber se é divisível por 6 (digite 0 se quiser parar): "))
        if num == 0:
            continuar = False
        else:
            divisivel = divisivel6(num)
            if divisivel:
                print(f"O número {num} é divisível por 6")

            else:
                print(f"O número {num} não é divisível por 6")
