"""
Ejercicio 2: Llenar una lista con los números del 1 al 10,
luego modificar los elementos de la lista multiplicándolos
por un valor que el usuario digite.
"""
lista = list(range(1,11))
print("La lista original")
for i in lista:
    print(i,end="-")

valor = int(input("\nDigite el numero: "))

#Multiplicamos los elementos

for indice,i in enumerate(lista):
    lista[indice] *= valor

print(f"\nLista final con los elementos multiplicados por {valor}")
for i in lista:
    print(i,end="-")