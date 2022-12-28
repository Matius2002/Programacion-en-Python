"""
Ejercicio 1: Desarrollar un programa que pueda calcular el valor del tipo de cambio de moneda 
(de tu moneda - hacia dólar y viceversa).
"""
def cambio_cop_dolares(cop):
    return cop / 4.77349

def cambio_dolares_cop(dolares):
    return dolares * 4.77349

while True:
    print("""\t.:MENU:.
1. Convertir COP a Dólares
2. Convertir Dólares a COP
3. Salir""")
    opcion = int(input("Digite una opcion (1-3): "))

    if opcion == 1:
        cop = float(input("\nDigite la cantidad de COP: "))
        print(f"\nDólares -> ${cambio_cop_dolares(cop):.2f}")
    elif opcion == 2:
        dolares = float(input("\nDigite la cantidad de USD: "))
        print(f"\nCOP -> ${cambio_dolares_cop(dolares):.5f}")
    elif opcion == 3:
        break
    else:
        print("\nError, se quivoco de opcion de menu")
    
    print()