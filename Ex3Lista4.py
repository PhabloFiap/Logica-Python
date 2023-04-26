num1 = int (input("Digite quantos numero voce quer escrever"))
numtemp = int(0)
numpos = int (0)
numneg = int (0)

while num1 != 0:
    numtemp = int (input("Insira o numero: "))
    if numtemp>0:
        numpos = numpos +1
    else:
        numneg = numneg +1  
    num1= num1 - 1

   
print(numpos)
print(numneg)