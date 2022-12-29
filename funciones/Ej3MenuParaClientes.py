"""
Ejercicio 3: Crear un programa que tenga una lista de clientes, cada cliente tiene su Nombre,
Apellido y CC. El programa tendrá el siguiente menú de opciones:
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por CC
4. Eliminar cliente
5. Salir

PD: Cada opción de menú se realizará con una función
"""
def agregar_cliente(clientes,nombre,apellido,cc):
    cliente = {}
    cliente['nombre'] = nombre
    cliente['apellido'] = apellido
    cliente['cc'] = cc
    clientes.append(cliente)

def mostrar_clientes(clientes):
    for i in clientes:
        print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, CC: {i['cc']}")

def mostrar_cliente(clientes,cc):
    for i in clientes:
        if i['cc'] == cc:
            print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, CC: {i['cc']}")
            return True
    return False

def eliminar_cliente(clientes,cc):
    for i in clientes:
        if i['cc'] == cc:
            clientes.remove(i)
            return True
    return False
    

clientes = []#Creamos una lista

while True:
    print("""\t.:MENÚ:.
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por CC
4. Eliminar cliente
5. Salir""")
    opcion = int(input("Digite una opción: "))

    print()

    if opcion == 1:
        nombre = input("Nombre del cliente -> ")
        apellido = input("Apellido de cliente -> ")
        cc = input("CC del cliente -> ")
        agregar_cliente(clientes, nombre, apellido, cc)

    elif opcion == 2:
        mostrar_clientes(clientes)

    elif opcion == 3:
        cc = input("CC del cliente -> ")
        if mostrar_cliente(clientes, cc):
            print("Cliente encontrado")
        else:
            print("Clinete no encontrado")
    
    elif opcion == 4:
        cc = input("CC del cliente -> ")
        if eliminar_cliente(clientes, cc):
            print("Cliente eliminado")
        else:
            print("Cliente no encontrado")

    elif opcion == 5:
        print("\nSALIDA CON EXITO")
        break

    else:
        print("Error, se equivocó de opción de menú")

    print()



