def menor (lista, pos):
    p_min = pos
    while pos<len(lista):
        if lista[pos] <lista[p_min]:
            p_min = pos
        pos = pos +1

    return p_min

def selection_sort(lista):
    for i in range (len(lista)):
        j = menor (lista, i)
        aux = lista[j]
        lista [j] = lista[i]
        lista[i] = aux

lista = [2.5,4.9,1.6,7,0,8.5]

selection_sort(lista)


print (lista)