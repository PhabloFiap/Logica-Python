def contadivisores (n):
    contagem = 0
    div =1
    while div<= n:
        if n % div == 0:
            contagem = contagem + 1
        
        div= div + 1
    
    return contagem    

def ehprimo(n):
    if contadivisores(n)==2
        return True
    else:
        return False

print(contadivisores(8))
print (contadivisores(139))

