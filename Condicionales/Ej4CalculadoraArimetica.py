"""
Ejercicio 4: Construir un programa que simule el 
funcionamiento de una calculadora que puede realizar
las cuatro operaciones ariméticas básicas (suma, 
resta, multiplicacion y división). El usuario debe 
especificar la operación con el primer caracter del
nombre de la operación
"""
num1 = float(input("\nDigite el primer numero: "))
num2 = float(input("Digite el segundo numero: "))
operacion = input("Digite la letra de la operacion: ").upper()

if operacion=='S':
    suma = num1 + num2
    print(f"La suma es: {suma}")
elif operacion=='R':
    resta = num1 - num2
    print(f"La resta es: {resta}")
elif operacion=='P' or operacion=='M':
    multiplicacion = num1 * num2
    print(f"La multiplicacion es: {multiplicacion}")
elif operacion=='D':
    division = num1 / num2
    print(f"La division es: {division:.2f}")
else:
    print("Letra fuera de rango")