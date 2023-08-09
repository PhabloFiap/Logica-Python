import random

def cria():
    monte =[]
    for v in range (1,14):

        monte.append((v,'p'))    
        monte.append((v,'c'))    
        monte.append((v,'o'))    
        monte.append((v,'e'))    

    return monte
    
def compra (monte: list):
    return monte.pop() #retira o ultimo da lista


def distribui (monte:list, qtd: int):
    mao = []
    while qtd >0:
        c= compra (monte)#chama a função para retirar da lista
        mao.append(c) # adiciona o item retirado
        qtd -=1 #diminui até ficar zero
    return mao

def embaralha (monte: list):
    random.shuffle(monte)#funcao para embaralhar lista


deck = cria()
#print (deck)
#card = compra(deck)
#print (card)
embaralha (deck)
print (deck)