"""
Ejercicio 5: Desarrollar un programa que permite sumar los digitos de un número
con ayuda de una función recursiva.
Ejemplo: 
Entrada = 123
Salida = 6
"""
def sumarDigitos(num):
    if num == 0: #Caso base
        resultado = 0
    else: #Caso recursivo
        resultado = sumarDigitos(int(num/10)) + (num%10)

    return resultado

numero = int(input("\nDIGITE UN NÚMERO ENTERO: ")) 
valor = sumarDigitos(numero)

print(f"\nLA SUMA DE lOS DIGITOS DEL NUMERO ES: {valor}")