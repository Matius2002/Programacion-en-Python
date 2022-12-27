"""
Ejercicio 2: Hacer un programa para detectar si una frase introducida por el usuario finaliza con un punto '.'
o no. Deberás imprimir por la consola una de las siguientes opciones; 'Termina con un punto' o por el contrario
'No termina con un punto'.
"""
cadena = input("Digite una frase: ").endswith(".")#Si termina en punto

if cadena==True:
    print("\n-Termina con un punto\n")
else:
    print("\n-No termina con un punto\n")