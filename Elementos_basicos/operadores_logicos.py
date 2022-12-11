#Operadores Lógicos
'''
Prioridad de los operadores lógicos
1. NOT
2. AND
3. OR

a = 10,b = 12,c = 13,d = 10
((a>b) or (a<c)) and ((a==c) or (a>b))
'''
a = 10
b = 12
c = 13
d = 10
#                              False
#              not(True)False       not(False)True
#           Flase    True       False       False
resultado = not((a>b) or (a<c)) and not((a==c) or (a>b))


print("El resultado es: ",resultado)