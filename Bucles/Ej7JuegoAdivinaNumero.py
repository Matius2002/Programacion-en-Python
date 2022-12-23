"""
Ejercicio 7: Realizar un juego para adivinar un número. Para ello generar un número
aleatorio entre 0-100, y el juego ir pidiendo números indicando "es mayor" o "es menor"
según sea mayor o menor con respecto a N. El proceso termina cuando el usuario acierta
y mostrar el número de intentos.
"""
import random

aleatorio = random.randint(0, 100)#Generamos un número aleatorio
print("\t.:Juego adivina el número:.")
contador = 0

while True:
    numero = int(input("Digite un número: "))
    contador += 1
    if numero>aleatorio:
        print("\tNo es el número, digita un número menor")
    elif numero<aleatorio:
        print("\tNo es el número, digita un número mayor")
    else:
        print(f"\tFelicidades, acabas de adivinar el número {aleatorio}")
        break

print(f"\nNúmero de intentos: {contador}")