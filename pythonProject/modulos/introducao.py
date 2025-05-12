def olaMundo():
    print("Olá mundo!")

def olaUDESC():
    print("Olá UDESC!")

def soma(var1, var2):
    somatorio = var1 + var2
    print(f"A soma do valor {var1} + {var2} = {somatorio}")
    res = var1 + var2
    return res

def entradaDados():
    valores = [0 for _ in range(2)]
    valores[0] = int(input("Digite o primeiro valor: "))
    valores[1] = int(input("Digite o segundo valor: "))
    return valores

def saidaDados(var1, var2, somatorio):
    print(f"A soma do valor {var1} + {var2} = {somatorio}")

if __name__ == "__main__":
    #olaMundo()
    #olaUDESC()
    print("SOMA")
    valores = entradaDados()
    somatorio = soma(valores[0], valores[1])
    saidaDados(valores[0], valores[1], somatorio)