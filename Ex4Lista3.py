

diautil = int (input("Digite quantos dias uteis tem o mes"))
totalhoras = int (input("Digite o total de  horas trabalhas pelo o trabalhador"))
recebhoras = int (input("Digite quanto o trabalhador recebe por horas"))

horaextra= float (0)

if (diautil*8 )<totalhoras:
    horaextra = (totalhoras-(diautil*8))* (recebhoras*1.5)
    print("Suas horas extras são R$ "+ str (horaextra))

else:
    print("Não recebe hora extra")



