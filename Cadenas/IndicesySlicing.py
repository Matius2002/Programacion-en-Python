"""
Indices y Slicing
-Las cadenas son inmutables
"""

cadena = "Mateo"
# cadena[0] = 'm'#Son inmutables
cadena = 'm' + cadena[1:]

print()
print(cadena[1:4])#Slicing es permitido en las cadenas
print(cadena)
print(len(cadena))#Cantidad de valores 