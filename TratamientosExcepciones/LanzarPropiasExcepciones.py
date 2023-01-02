"""
Lanzar propias excepciones
"""
def verificandoEdad(edad):
    if edad < 0: #La edad es negativa
        raise ValueError("La edad no puede ser negativa")
    elif edad < 18:
        print("Eres menor de edad")
    elif edad < 30:
        print("Eres joven")
    elif edad < 50:
        print("Eres un un adulto")

edad = int(input("Digite su edad: "))
try:
    verificandoEdad(edad)
except ValueError as EdadNegativa:
    print(EdadNegativa)

print("Programa terminado\n")
