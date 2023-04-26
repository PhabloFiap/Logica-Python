def contadigitos (n,d):
    conta = 0 
    
    while n !=0:
        resto = n % 10
        if resto == d:
            conta = conta + 1
        n = n // 10

    return conta

qtd = contadigitos(1224237, 3)
print (qtd)