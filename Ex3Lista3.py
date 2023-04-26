timea = input("Digite o time a")
timeb = input("Digite o time b")

gola = int (input("Digite quantos gols timeA fez"))
golb = int (input("Digite quantos gols timeB fez"))

if gola>golb:
    print(timea + " fez mais gols")

elif golb>gola:
    print (timeb +" fez  mais gols")

else:
    print("Empate")