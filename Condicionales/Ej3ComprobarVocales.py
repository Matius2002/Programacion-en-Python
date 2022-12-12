"""
Ejercicio 3: Hacer un programa que pida un carácter
e indique si es una vocal o no.
"""
letra = input("\nDigite un caratcer: ").lower() #Metodo que transforma en minuscula

if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print("Es vocal\n")
else:
    print("No es vocal\n")