def somaFibonacci(n):
    fib1, fib2 = 1, 1
    soma = 0

    for i in range(n):
        soma += fib1
        fib_atual = fib1 + fib2
        fib1 = fib2
        fib2 = fib_atual

    return soma

if __name__ == "__main__":
    n = int(input(f"Digite o valor de n: "))
    print(f"A soma dos {n} primeiros termos da série de Fibonacci é: {somaFibonacci(n)}")