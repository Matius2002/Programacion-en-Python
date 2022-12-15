"""
Colas
"""
#from collections import deque #Otra forma de simular las colas
cola = ["Mateo","Maria","Marta","Jose"]

#Agregamos elementos al final de la cola
cola.append("Karla")
cola.append("Juan")

print(cola)

#Sacando elementos por el principicio de la cola
n = cola.pop(0)
print(f"Atendiendo a {n}")

n = cola.pop(0)
print(f"Atendiendo a {n}")

print(cola)