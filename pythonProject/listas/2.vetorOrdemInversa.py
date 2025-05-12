if __name__ == "__main__":
  numeros = [0 for _ in range(10)]

  for i in range(10):
    numeros[i] = float(input(f"Digite o {i + 1}° número: "))

  print("Os números na ordem inversa são: ")
  print("[", end ="")

  for i in range(9, -1, -1):
    if i > 0:
      print(numeros[i], end= ", ")
    else:
      print(numeros[i], end="")
  print("]")