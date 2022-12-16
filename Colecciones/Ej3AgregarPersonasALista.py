"""
Ejercicio 3: Escriba un programa donde cree una lista con los siguientes
personajes del anime My Hero Academia.
-----------------------
Nombre: Enji Todoroki
Don: Hell Flame
Rango: 1
----------------------
Nombre: Keigo Takami
Don: Alas Rígidas
Rango: 2
----------------------
Nombre: Tsunagu Hakamada
Don: Fiber Master
Rango: 3
----------------------
Nombre: Shinya Kamihara
Don: Cuerpo de papel
Rango: 4
----------------------
Nombre: Rumi Usagiyama
Don: Conejo
Rango: 5
"""
personajes = []#Creamos una lista vacia
p = {"Nombre":"Enji Todoroki","Don":"Hell Flame","Rango":"1"}
personajes.append(p)#Agregamos a la lista el primer personaje

p = {"Nombre":"Keigo Takami","Don":"Alas Rígidas","Rango":"2"}
personajes.append(p)#Agregamos a la lista el segundo personaje

p = {"Nombre":"Tsunagu Hakamada","Don":"Fiber Master","Rango":"3"}
personajes.append(p)#Agregamos a la lista el tercero personaje

p = {"Nombre":"Shinya Kamihara","Don":"Cuerpo de papel","Rango":"4"}
personajes.append(p)#Agregamos a la lista el cuarto personaje

p = {"Nombre":"Rumi Usagiyama","Don":"Conejo","Rango":"5"}
personajes.append(p)#Agregamos a la lista el quinto personaje

print(personajes)