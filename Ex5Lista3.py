n = int (input("Digite um numero: "))
n2 = n
divisor =0

while n>0:
    if n2%n ==0:
        divisor += 1
    n-=1
print (divisor)
