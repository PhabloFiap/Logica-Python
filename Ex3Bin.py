bin = int (input("Informe o numero binario: "))
soma =0
pot2 =1

while bin>0:
    digito = bin % 10
    soma = soma + digito *pot2
    bin = bin //10
    pot2 = pot2* 2

print(soma)