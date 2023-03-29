dia = int(input("Informe o dia: "))
mes = int(input("Informe o mes: "))
ano = int(input("Informe o ano: "))

if dia >= 1 and dia <= 30 and mes >= 1 and mes <= 12 and mes != 2:
    print("Data valida!")

elif dia == 31 and (mes == 1 or mes == 3 or mes == 5 or 
                    mes == 7 or mes == 8 or mes == 10 or mes == 12):
    print("Data valida!")

elif mes == 2 and dia >= 1 and dia <= 28:
    print("Data valida!")

elif mes == 2 and dia == 29:
    #validacao de ano bissexto
    if ano % 400 == 0:
        print("Data valida!")
    elif ano % 100 == 0:
        print("Data invalida!")
    elif ano % 4 == 0:
        print("Data valida!")
    else:
        print("Data invalida!")

else:
    print("Data invalida!")    