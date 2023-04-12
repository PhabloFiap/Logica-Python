num = int (input ("Informe um numer: "))
num_copia = num
invertido = ""



while num!= 0:
    digito = num % 10
    invertido = invertido + str (digito)
    num = num //10


print(invertido)
if int(invertido) == num_copia:
    print("É palindrome")
else:
    print("Não é palindrome")
    