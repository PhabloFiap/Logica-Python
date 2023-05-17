import random
def consulta_paciente(st,lista):
    i =0
    while i<len(lista):
        if lista[i+6]==st:
            print(lista[i], lista [i+1], lista [i+2])
        i+= 7
def cadastra_paciente(lista):
    nome = input("Nome: ")
    idade = random.randint(15,60)
    peso = random.randint(50,100)
    altura = random.random() +1
    pressao = input ("Pressao: ")
    temperatura = input ("temperatura:")
    lista.append(nome)
    lista.append(idade)
    lista.append(peso)
    lista.append(altura)
    lista.append(pressao)
    lista.append(temperatura)
    lista.append(1)

def recupera_paciente (lista):
    i=0
    while i< len(lista):
        if lista [i+6] == 1:
            return i
        i+=7
    return -1