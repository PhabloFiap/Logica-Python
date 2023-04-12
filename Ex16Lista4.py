num = int(input("Informe parte do boleto: "))
soma = 0
mult = 2 

while num > 0:
    digito = num % 10
    prod = digito * mult
    if prod >= 10:
        soma = soma + prod % 10 + prod // 10
    else:
        soma = soma + prod    
    num = num // 10
    if mult == 2:
        mult = 1
    else:
        mult = 2

resto = soma % 10
if resto != 0:
    print("Digito de controle vale", 10 - resto)
else:
    print("Digito de controle vale 0")    
    