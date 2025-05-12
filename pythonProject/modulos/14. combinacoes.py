def fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial


def combinacao(n, p):
    if p > n:
        return "p não pode ser maior que n."
    return fatorial(n) // (fatorial(p) * fatorial(n - p))


if __name__ == "__main__":
    n = int(input("Digite o valor de n (total de elementos): "))
    p = int(input("Digite o valor de p (elementos por combinação): "))

    print(f"A combinação de {n} elementos, {p} a {p}, é: {combinacao(n, p)}")