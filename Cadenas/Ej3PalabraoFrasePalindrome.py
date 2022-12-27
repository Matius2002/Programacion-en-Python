"""
Ejercicio 3: Hacer un programa que determine si una palabra o frase es palíndroma. 
Una cadena palíndromo se lee igual de izquierda a derecha que de derecha a izquierda.
Ejemplo:
1. oso
2. reconocer
3. anita lava la tina
"""

cadena = input("Digite una palabra palíndroma: ").lower()

#Primero, quitamos los espacios blancos de la cadena
cadena = cadena.replace(" ","")

#Segundo, invertimos la cadena
cadena2 = cadena[::-1]

print(f"\nLa cadena invertida es: {cadena2}")
print(f"La cadena1 es: {cadena}")

if cadena == cadena2:
    print("\n-LA CADENA ES UN PALINDROMO")
else:
    print("\n-LA CADENA NO ES UN PALINDROMO")