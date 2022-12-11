#Ejercicio 4: Hacer un programa para ingresar el radio de un circulo y se reporte su área y la longitud de la circunferencia
import math

r = float(input("\nDigite el radio: "))

area = math.pi*r**2
longitud = 2*math.pi*r

print(f"\nEl área es: {area:.3f}")
print(f"La longitud es: {longitud:.3f}")
