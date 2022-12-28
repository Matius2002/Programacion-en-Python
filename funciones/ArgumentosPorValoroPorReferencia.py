"""
Argumentos por valor o por referencia
"""
def doblar_valor(numero):
    return numero * 2

n = 5
n = doblar_valor(n)#Argumentos por valor

print(n)

def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

n = [5,10,15,20]
doblar_valores(n[:])#Por valor (n[:]) | Por (n) referencia 

print(n)