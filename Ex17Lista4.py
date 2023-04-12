num = int(input("Informe n: "))

raiz = 0.001
incremento = 0.001

while raiz * raiz < num:
    raiz = raiz + incremento

print(f"A raiz quadrada de {num} é {raiz}")

