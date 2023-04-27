n = int (input("qtd de alunos: "))

contador = 0
soma = 0
notamenor = 0
notamaior = 0
while n > contador:
    nota = int (input("Digite a nota do aluno"))
    soma = soma + nota
    contador = contador + 1
    if nota <6:
        notamenor = notamenor+ 1
    else:
        notamaior= notamaior +1

media = soma / n
print(media)
print(notamenor)
print(notamaior)