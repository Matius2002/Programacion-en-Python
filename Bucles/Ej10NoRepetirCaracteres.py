"""
Ejercicio 10: Hacer un programa que pida una cadena por teclado, luego meta los caracteres
en una lista sin repetir caracteres.
Nota:
-Sin espacios la cadena
-No repite los caracteres
"""
cadena = input("Digite una frase: ").lower()
lista = []
lista2 = []

for i in cadena:#Recorre la cadena
    if i not in lista2:#Si el caracter aun no esta en la lista
        if i != " ":#Eliminamos los espacios en la lista
            lista2.append(i)#Lo agregamos a la lista
    
lista = lista2#Convertimos lo almacena a la lista original

print(f"\nLista de carcteres sin repetir \n{lista}")