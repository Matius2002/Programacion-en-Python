#Metodos de caracteres

print()

cadena = "hola mundo".upper()#Todas mayusculas
print(cadena)

cadena = "WELLO world".lower()#Todas minusculas
print(cadena)

cadena = "hola mundo".capitalize()#La primera letra en mayusculas
print(cadena)

cadena = "Wello world".title()#Las primeras latras de cada palabra
print(cadena)

cadena = "hola mundo mundo mundo".count('mundo')#Cuenta cuantas letras hay en la cadena
print(cadena)

cadena = "hola mundo".find('mundo')#Busca en que posicion esta la letra buscada
print(cadena)

cadena = "hola mundo mundo mundo".rfind('mundo')#Busca la ultima ultima posicion de la letra buscada
print(cadena)

cadena = "0".isdigit()#Comprueba si la cadena todos sus valores son numericos
print(cadena)

cadena = "asssjsand".isalpha()#Comprueba que solo sean caracteres
print(cadena)

cadena = "dnasj12".isalnum()#Comprueba que solo sean caracteres y numericos
print(cadena)

cadena = "hola mundo".islower()#Comprueba si todo esta en minuscula
print(cadena)

cadena = "Holal Mundo".istitle()#Comprueba que si cada palabra esta en mayuscula
print(cadena)

cadena = "   n  ".isspace()#Comprueba si la cadena esta vacia
print(cadena)

cadena = "hola mundo".startswith('h')#Si comienza con cierta letra
print(cadena)

cadena = "hola mundo".endswith('d')#Si termina con cierta letra
print(cadena)

cadena = "hola,mundo".split(',')#Separa los elementos en una lista
print(cadena)

cadena = " ".join("mateo")#Separa la palabra con lo introducido
print(cadena)

cadena = "...hola...".strip('.')#Elimina los espacios
print(cadena)

cadena = "hola mundo".replace('o', 'x')#Remplaza las letras con otras
print(cadena)

