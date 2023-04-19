cpf = int (input("Informe cpf9: "))
guarda_cpf = cpf
soma =0
mult = 2

while cpf>0:
    digito = cpf% 10
    soma = soma + digito *mult
    cpf= cpf //10
    mult = mult +1

resto = soma % 11

if resto <2:
    digito_controle1 = 0

else:
    digito_controle1 = 11 - resto

print (guarda_cpf)
print(digito_controle1)

cpf = guarda_cpf *10 + digito_controle1

mult = 2
soma = 0

while cpf >0:
    digito = cpf %10
    soma = soma + digito* mult
    cpf = cpf//10
    mult = mult +1

resto = soma % 11
if resto<2:
    digito_controle2 =0

else:
    digito_controle2 = 11 - resto

print ("{}{}".format(digito_controle1, digito_controle2))
