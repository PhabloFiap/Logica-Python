def ePrimo(num):
    if num == 1:
        return False
    
    div = 2
    while num % div != 0:
        div = div + 1

    if div == num:
        return True
    else:
        return False

n = 2
conta_primo = 0

while conta_primo < 10000:
    resp = ePrimo(n)
    if resp == True:
        print(n)
        conta_primo = conta_primo + 1
    n = n + 1

