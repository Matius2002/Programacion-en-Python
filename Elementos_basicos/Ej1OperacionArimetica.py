#Ejercicio 1: Escribir la siguiente expresión en forma de expresión algoritmica.
# a**3 * (b**2 - 2*a*c) / 2*b

a = float(input("Digite el valor de A: "))
b = float(input("Digite el valor de B: "))
c = float(input("Digite el valor de C: "))

expresion = (a**3 * (b**2 - 2*a*c)) / (2*b)

print(f"El resultado es: {expresion}")