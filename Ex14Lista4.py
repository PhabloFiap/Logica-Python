num = int (input("Digite um numero "))

soma =0
div =1

while div<num:
    if num % div ==0:
        soma = soma + div
    div = div +1
    
if soma == num:
    print (num, "é perfeito")
else:
    print (num, "Não é perfeito")
