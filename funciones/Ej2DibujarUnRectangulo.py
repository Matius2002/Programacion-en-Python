"""
Ejercicio 2: Hacer un porgrama que pida la anchura y altura de un rectángulo
y con ayuda de una función lo dibuje con *.
Ejemplo:
ancho = 7   
alto = 3

          Demostración

            *******
            *******
            *******

"""
def dibujar(ancho,alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ",end="")
        print()

ancho = 5
alto = 3

ancho = int(input("Digite el ancho: "))
alto = int(input("Digite el alto: "))

print()
dibujar(ancho, alto)


