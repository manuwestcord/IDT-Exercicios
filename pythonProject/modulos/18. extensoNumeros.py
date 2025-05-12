def numero_por_extenso(n):
    if n == 0:
        return "zero"

    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos",
                "oitocentos", "novecentos"]

    def numero_menor_que_mil(n):
        extenso = ""

        if n >= 100:
            if n == 100:
                extenso += "cem"
            else:
                extenso += centenas[n // 100]
            n %= 100
            if n > 0:
                extenso += " e "

        if n >= 20:
            extenso += dezenas[n // 10]
            n %= 10
            if n > 0:
                extenso += " e "

        if 10 <= n < 20:
            extenso += especiais[n - 10]
        elif n < 10:
            extenso += unidades[n]

        return extenso

    grupos = ["", "mil", "milhão", "bilhão"]
    partes = []
    grupo_index = 0

    while n > 0:
        parte = n % 1000
        if parte > 0:
            if grupo_index == 1 and parte == 1:
                partes.append("mil")
            else:
                partes.append(numero_menor_que_mil(parte) + (" " + grupos[grupo_index] if grupos[grupo_index] else ""))
        n //= 1000
        grupo_index += 1

    return " e ".join(reversed(partes))
if __name__ == "__main__":
    numero = int(input("Digite um número de até 12 casas para saber sua escrita por extenso: "))
    print(numero_por_extenso(numero))
