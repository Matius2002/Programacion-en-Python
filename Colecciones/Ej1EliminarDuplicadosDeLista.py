"""
Ejercicio 1: Escriba un programa donde tenga una lista y que,
a continuación, elimine los elementos repetidos, por último 
mostrar la lista.
"""
lista = [1,2,3,4,1,2,4,7,"Sebastian Gongora","Mateo Mora","Gina Hernández","Alexander Mora","Mateo Mora"]

lista = list(set(lista))

print(lista)