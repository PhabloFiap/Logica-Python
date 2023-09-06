def organiza (lista,i):
    aux = lista [i]
    while i>0 and lista [i-1]> aux:
        lista [i] = lista [i-1]
        i= i-1

    lista [i] = aux

lst = [3,9,1,2,0,10]
organiza(lst,1)
organiza(lst,2)
organiza(lst,3)
print(lst)
    