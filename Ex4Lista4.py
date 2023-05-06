n =int (input("Digite a sequencia de um numero: "))
n2 = n
i =0
contaNegativo = 0
contaPositivo = 0

while n>i:
    num = int (input("digite um numero"))
    if num <0:
        contaNegativo =+1
        
    else:
        contaPositivo =+1
    i+=1
print ("numeros negativos: " + str (num))
print("numeros positivos: " +str (num))