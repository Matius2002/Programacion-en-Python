"""
Ejercicio 1: Llenar una lista con los números del 1 al 50,
luego mostrar la lista con un bucle for, los elementos deben
mostrarse de la siguiente forma:
1-2-3-4-5...-50
"""
#lista = []

#Agregamos los numeros del 1 al 50 a la lista
#i = 1

#while i<=50:
    #lista.append(i)
    #i+=1

lista = list(range(1,51))#Segunda forma de hacerlo

#Imprimimos los lementos de la lista
for i in lista:
    print(i,end="-")