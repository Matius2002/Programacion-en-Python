"""
Ejercicio 5: Una tienda ofrece un descuento del 15%
sobre el total de la compra y un cliente desea 
saber cuánto deberá pagar finalmente por su compra.
"""
precio = float(input("\nDigite el valor del precio de la compra: "))

descuento = precio * 0.15
total_compra = precio - descuento

print(f"El total de la compra es: {total_compra}")