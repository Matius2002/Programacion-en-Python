"""
Pilas
"""
pila = [1,2,3]

#Agregamos elementos por el final
pila.append(4)
pila.append(5)

print(pila)

#Sacamos elementos por el final
n = pila.pop()
print(f"Sacando el elemento {n}")
n = pila.pop()
print(f"Sacando el elemento {n}")

print(pila)