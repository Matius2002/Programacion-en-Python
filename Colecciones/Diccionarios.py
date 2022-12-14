"""
Diccionarios
Nota: Nos permiten almacenar una serie de mapeos entre conjuntos de elementos,
llamados keys and values (Claves y Valores).
-Tienen valores desordenados.
-Tienen clave y valor.
-Se pueden almacenar otras colecciones y diccionarios 
"""
print()
#diccionario = {"Mateo":[22,1.77],"Jose":[21,1.75],"Maria":[22,1.67]}
equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo",17:"Mario Mandzukic"}


#diccionario["azul"] = "BLUE"#Modificar un elemento
#del(diccionario["verde"])#Eliminar una clave y valor

#print(equipo.keys())#Muestras solo las claves de nuestro diccionario
#print(equipo.values())#Muestra solo los valores de nuestro diccionario
print(equipo.items())#Muestra todas las claves y valores de nuestro diccionario

#print(equipo.get(7,"No existe un jugador con ese dorsal"))#Cuando no encuentra la clave, muestra el mensaje
#print(diccionario["rojo"])#Si se quiere sabe el valor de una clave
#print(diccionario["Mateo"])