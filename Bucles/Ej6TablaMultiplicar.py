"""
Ejercicio 6: Hacer un programa que pida un número por teclado y guarde en una lista
su tabla de multiplicar hasta el 10. Por ejemplo, si digita el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50
"""
lista = []

numero = int(input("\nDigite un número entero para conocer su tabal de multiplicar: "))

print("\nPRIMERA FORMA DE HACER LA TABLA")
for i in range(1,11):
    lista.append(numero*i)
    print(f"{numero} * {i} = {numero*i}")
    
print("\nSEGUNDA FORMA DE HACER LA TABLA")
print(lista)