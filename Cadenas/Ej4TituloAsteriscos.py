"""
Ejercicio 4: Hacer un programa donde se reemplacen todos los espacios de una cadena
por asteriscos y además cada palabra comience por mayúsculas.
"""
cadena = input("Digite una frase: ").title()#Segundo, convertimos las primeras letras de cada palabras a mayusculas

#Primero, reemplazamos los espacios blancos por *
cadena = cadena.replace(" ", "*")

print(f"\nLA CADENA FINALIZADA ES: \n{cadena}")