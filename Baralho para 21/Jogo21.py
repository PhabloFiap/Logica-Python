import Baralho

def imprime (mao):
    info = ""
    for c in mao:
        info = info + str (c[0]) + c[1]
    print (info)

def pontos (mao):
    valor = 0
    for c in mao:
        if c [0]>10:
            valor += c[0]
        else:
            valor += c[0]
    return valor

def querCarta (mao:list):
    imprime (mao)
    print ("Pontos: ", pontos (mao))
    escolha = input ("quer carta (s/n)?")
    if escolha == 's':
        return True
    else:
        return False


deck = Baralho.cria()
Baralho.embaralha(deck)

maoJogador = Baralho.distribui (deck,2)
maoCpu = Baralho.distribui (deck,2)

while querCarta(maoJogador) == True:
    c = Baralho.compra(deck)
    maoJogador.append(c)

while pontos(maoCpu) <16:
    c = Baralho.compra(deck)
    maoCpu.append(c)


print ("Jogador: ")
imprime (maoJogador)
print ("Pontos: " , pontos(maoJogador))

print ("CPU: ")
imprime (maoJogador)
print ("Pontos: " , pontos(maoJogador))