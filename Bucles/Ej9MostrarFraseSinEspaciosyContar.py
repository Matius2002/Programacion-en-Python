"""
Ejercicio 9: Hacer un porgrama donde el usuario ingrese una frase, se le
devolverá la misma frase pero sin espacios en blanco y además un contador
de cuántos caracteres tiene la frase (sin contar los espacios en blanco).
Frase: Hola que tal?
Frase final: Holaquetal?
N° de caracteres: 11
"""
frase = input("Digite una frase: ")#Se digita la frase
frase2 = ""#Cadena vacia

for i in frase:
    if i != " ":
        frase2 += i#Guarda la cadena sin espacios en frase2

frase = frase2#Se pasa a la variable principal


print(f"\nLa frase final: {frase}")
print(f"N° de carcteres: {len(frase)}")