def fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

def arranjo(n, p):
    if p > n:
        return "Erro: p não pode ser maior que n."
    return fatorial(n) // fatorial(n - p)

if __name__ == "__main__":
    n = int(input("Digite o valor de n (total de elementos): "))
    p = int(input("Digite o valor de p (elementos por arranjo): "))

    print(f"O arranjo de {n} elementos, {p} a {p}, é {arranjo(n, p)}")