import math

a = float (input("A: "))
b = float (input ("B: "))
c = float (input ("C: "))

delta = b *b - 4 *a *c 

if delta <0:
    print ("impossivel calcular as raizes da equacao")

else:
    x1 = (-b + delta ** 0.5) / (2*a)
    x2 = (-b- math.sqrt (delta)) /(2*a)
    print ( "As raizes sao {x1} e {x2} % {{}}")
    #Uma equação de 2º grau é da forma: ax2 + bx + c = 0, onde a 6= 0. Escreva um algoritmo
#que recebe os três coecientes da equação, calcula e imprime as raízes reais se for possível.
#Use a seguinte fórmula para resolver a equação:##