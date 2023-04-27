def substitui(frase, letra):
    resp = ""
    for c in frase:
        if c == letra:
            resp = resp + '*'
        else:
            resp = resp + c
    
    return resp
    

def sub(frase, letra):
    resp = ""
    i = 0
    while i < len(frase):
        c = frase[i]
        if c == letra:
            resp = resp + '*'
        else:
            resp = resp + c
        i = i + 1
    return resp        

troca = substitui("camiseta", "a")    
print(troca)
