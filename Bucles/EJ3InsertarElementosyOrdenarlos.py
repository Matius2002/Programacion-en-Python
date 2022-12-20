"""
Ejercicio 3: Pide numeros y metelos en una lista, cuando el usuario
meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.
"""
lista = []

salir = False

while not salir:#Si es True no entra al ciclo3
    numero = int(input("Digite un numero: "))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)

lista.sort()

print(f"\nLista ordenada: \n{lista}")