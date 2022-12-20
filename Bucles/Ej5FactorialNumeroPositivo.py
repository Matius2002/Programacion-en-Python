"""
Ejercicio 5: Hacer un programa para calcular el factorial
de un número positivo.
-No se puede sacar un factorial a un numero negativo
"""
numero = int(input("\nDigite el numero a calcular el factorial: "))

while numero<0:#Asegurarnos que no sea negativo
    print("Error -> El numero tiene que ser positivo")
    numero = int(input("\nDigite el numero a calcular el factorial: "))

#Calcular el factorial
factorial = 1
for i in range(1,numero+1):
    factorial *= i #Sacamos el factorial

print(f"El factorial del número {numero} es: {factorial}")