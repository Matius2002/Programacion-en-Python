"""
Ejercicio 4: Desarrollar un programa para calcular el factorial de un número
con ayuda de una función recursiva.
Nota: No se puede calcular un número grande por que su factorial es un numero muy exagerado
"""
def factorial_numero(numero):
    if numero > 0:
        resultado = numero * factorial_numero(numero - 1)
    else:
        resultado = 1

    return resultado

numero = int(input("DIGITE UN NÚMERO PARA SABER SU FACTORIAL: "))

while numero<0:
    print("\nERROR, -> EL NÚMERO TIENE QUE SER POSITIVO")
    numero = int(input("\nDIGITE UN NÚMERO PARA SABER SU FACTORIAL: "))
    
valor = factorial_numero(numero)
print(f"\nEL FACTORIAL DEL NÚMERO: {numero}, ES: {valor}")


