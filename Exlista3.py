
def divisivel (a,b):
    if (a%b) >0:
        print(str (a) + " não é divisivel por "+ str (b))

    else:
        print (str (a) + "  é divisivel por "+ str (b))


divisivel (int (input("digite o primeiro numero")), int (input("Digite o segundo numero")))

