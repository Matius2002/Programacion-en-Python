"""
Conjuntos
Nota: Es una coleccion no ordenada de objetos unicos. No existe, por tanto, una
relacion de orden y resulta imposible encontrar dos elementos identicos.
-Es un conjunto de elementos desordenados.
-No muestra los elementos duplicados.
-No se puede almacenar otra coleccion dentro del conjunto.
-Diccionarios y conjuntos tienen los mismos {}
"""
#La clase set() es para establecer que es un conjunto vacio y no confundir a python en los dicconarios
#Pero si se colocan valores de una en los {1,2,3} python entiende que son conjuntos
#conjunto = set()
conjunto1 = frozenset({1,2,3})#La clase frozenset() limita la modificacion o eliminacion de elementos mediante metodos
conjunto2 = {3,4,5}
conjunto3 = {1,2,3,4,5}

#Operaciones con conjuntos
#conjunto3 = conjunto1 | conjunto2#Union de conjuntos
#conjunto3 = conjunto1 & conjunto2#Interseccion de conjuntos
#conjunto3 = conjunto1 - conjunto2#Diferencia de conjuntos
#conjunto3 = conjunto1 ^ conjunto2 #Diferencia simetrica

#Metodo para insertar
#conjunto3.add(6)#Metodo para insertar un elemento en la ultima posicion

#Metodos para eliminar
#conjunto2.discard(5)#Metodo para eliminar un elemento
#conjunto3.clear()#Metodo para eliminar todos los elementos

#Funcion
print()
print(conjunto3)
#print(3 not in conjunto)#Muestra si un elemento no esta
#print(conjunto1.issubset(conjunto3))#Metodo para comprobar si es subconjunto
#print(conjunto3.issuperset(conjunto2))#Metodo para comprobar si es un superconjunto
#print(conjunto1.isdisjoint(conjunto2))#Metodo para comprobar si es un conjunto disconexos
