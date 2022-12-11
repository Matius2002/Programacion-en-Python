"""
Ejercicio 2: Determinar la solución lógica de la siguiente operación: 
((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)
"""

a = float(input("\nDigite el valor de A: "))
b = float(input("Digite el valor de B: "))

operacion = ((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)

print(f"La solución logica es: {operacion}")