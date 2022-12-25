"""
Cadenas de caracteres
Nota: Se pueden colocar '' o "" para las cadenas
- \palabra\ se agrega "" en las cadenas
- \n salto de linea
- \t Deja espacio en una cadena
- r Guarda la cadena en crudo
"""

cadena = r"Estoy \n\"estudiando\" \tprogramación en Python" #Se puede '' o ""
cadena2 = """Hola
que tal mi nombre es Mateo Mora
"""
cadena3 = "Wello "
cadena4 = "World"

print()#Salto de línea
print(cadena)
print(cadena2)
print("""Hola que 
tal amigo""")
print(cadena3 + cadena4)