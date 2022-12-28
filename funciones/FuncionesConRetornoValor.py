"""
Funciones con retorno de valor
"""
def multiplicar(num1,num2):
    mult = num1 * num2
    return mult

def prueba():
    return "hola",45,[1,2,3]

c,n,l = prueba()

print(multiplicar(3,4))
print(prueba())
#Imprimimos los elementos de la función 1 por 1
print(c)
print(n)
print(l)