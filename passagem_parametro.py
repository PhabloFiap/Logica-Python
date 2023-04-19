def divisao (a,b):
    a = a +10
    b = b +5
    return a // b, a % b

def divisao_mutavel (lista):
    lista [0] = lista [0] + 10
    lista [1] = lista [1] + 5
    return lista [0] // lista [1], lista [0] % lista [1]

lst = [5,3]
resultado = divisao_mutavel (lst)
print(resultado)
print(lst)

x = 5
y = 3

resultado = divisao (x,y)
print(resultado)