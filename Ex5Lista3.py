n = int (input("Digite um numero: "))
n2 = n
divisor =0
primo =0

while n>0:

    if n2%n ==0:
        divisor += 1

    

    n-=1
if divisor==2 or n ==1:
        print(str (n2) +" é primo")

print (divisor)
print (primo)
