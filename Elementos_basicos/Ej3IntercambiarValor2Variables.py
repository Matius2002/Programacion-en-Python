"""
Ejercicio 3: Hacer un programa para intercambiar el valor de 2 variables
Ejemplo:    a = 10  a = 5
            b = 5   b = 10
"""

a = int(input("\nDigite el valor de A: "))
b = int(input("Digite el valor de B: "))

a, b = b, a #Cambiamos el valor

print(f"\nEl valor de A es: {a}")
print(f"El valor de B es: {b}")
