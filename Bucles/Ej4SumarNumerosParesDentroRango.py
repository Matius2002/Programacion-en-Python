"""
Ejercicio 4: Hacer un programa para sumar números pares dentro de un rango.
Ejemplo: Suma de números pares del 2 al 30
Suma = 240
"""
a = int(input("Digite de donde va a comenzar a sumar: "))
b = int(input("Digite de donde quiere llegar a sumar: "))
suma = 0

for i in range(a,b+1):
    if i%2==0: #Si el numero es par
        suma += i
        print(f"La suma ve en: {suma}")

print(f"\nLa suma de pares dentro del rango es: {suma}")
