"""
Conjuntos
-Es un conjunto de elementos desordenados
-No pueden haber elementos duplicados
-No puede haber una coleccion dentro un conjunto
-Diccionarios y conjuntos tienen los mismos {}
"""
#conjunto = set()#Conjunto vacio
conjunto1 = frozenset({1,2,3})#No se puede agregar por frozenset no se modificar o eliminar
conjunto2 = {3,4,5}


#c = conjunto1 | conjunto2 #Union de conjuntos
#c = conjunto1 & conjunto2 #Interseccion de conjuntos
#c = conjunto1 - conjunto2 #Diferencia de conjuntos
#c = conjunto1 ^ conjunto2 #Diferencia cimetrica
c = {1,2,3,4,5}

#conjunto.add(5)#Agrega un elemento
#conjunto.discard("Hola")#Elimina un elemento
#conjunto.clear()#Eliminamos el conjunto


#print(3 not in conjunto)#Sabemos si un elemento no esta en el conjunto
#print(conjunto1.issubset(c))#Si es un subconjunto
#print(c.issuperset(conjunto2))#Si es un super conjunto
#print(conjunto1.isdisjoint(conjunto2))#Disconexos
print(conjunto1)