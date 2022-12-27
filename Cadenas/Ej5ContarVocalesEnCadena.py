"""
Ejercicio 5: Hacer un programa donde se cuente cada una de las vocales en una cadena,
mostrar el conteo de las apariciones de cada vocal.
"""
#Primera forma de hacer el ejercicio
cadena = input("Digite una frase: ").lower()
contaVocales = 0

for i in cadena:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        contaVocales += 1

print(f"\n-LA CADENA ES: \n{cadena}")
print(f"\n-LA CATIDAD DE VOCALES ES: {contaVocales}")

#Segunda forma de hacer sin recorrer la cadena, solo itilizando los metodos
print(f"\nVocal a: {cadena.count('a')}")
print(f"Vocal e: {cadena.count('e')}")
print(f"Vocal i: {cadena.count('i')}")
print(f"Vocal o: {cadena.count('o')}")
print(f"Vocal u: {cadena.count('u')}")
