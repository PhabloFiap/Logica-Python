n = int (input("qtd de alunos: "))

contador = 0
soma = 0
while contador <n:
    nota = float(input ("nota do aluno: "))
    soma = soma + nota
    contador = contador +1

print (f"a soma vale:  {soma/n}")
