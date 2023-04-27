n = int (input("Digite sequencia de numeros: "))
n2 = n
contaNumeroPositivo = 0
contaNumeroNegativo = 0

while n>0:
    sequencia = int (input("Digite o numero da sequencia"))
    n = n -1
    if sequencia>0:
        contaNumeroPositivo = contaNumeroPositivo +1

    else:
        contaNumeroNegativo = contaNumeroNegativo +1

print ("Numeros positivos: "+  str (contaNumeroPositivo))
print ("Numeros negativos: " + str (contaNumeroNegativo))


