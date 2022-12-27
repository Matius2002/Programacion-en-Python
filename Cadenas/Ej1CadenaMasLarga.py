"""
Ejercicio 1: Hacer un programa donde se deberá imprimir por la consola la palabra con más caracteres
de dos palabras dadas. En el caso de que ambas palabras tengan la misma cantidad de caracteres, deberás
mostrar el mensaje "Son iguales".
"""
cadena = input("Digite una frase: ")
cadena2 = input("Digite otra frase: ")

if len(cadena)>len(cadena2):
    print(f"\nLa palabra con mas caracteres: \n-{cadena}",f"\n-{len(cadena)} caracteres")
elif len(cadena)<len(cadena2):
    print(f"\nLa palabra con mas caracteres: \n-{cadena2}",f"\n-{len(cadena2)} caracteres")
else:
    print("\nAmbas palabras tienen los mismos caracteres")

