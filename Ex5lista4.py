n = int(input("Digite um numero que deseja contar os divisores"))
divisor = 0
i=0
while n>0:
    if i%n ==0:
        i +=1
    
    n-=1

print (i)