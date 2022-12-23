"""
Ejercicio 8: Hacer un programa que simule un cajero automático con un saldo inicial de $1000 y tendrá el siguiente
menú de opciones:
1. Ingresar dinero a la cuenta
2. Retirar dinero a la cuenta
3. Mostrar dinero disponible
4. Salir
"""
saldo = 1000
while True:
    print("\t.:MENU:.")
    print("1. Ingresar dinero en la cuenta ")
    print("2. Retirar dinero en la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opcion de menu: "))

    print()

    if opcion==1:
        extra = float(input("Cuanto dinero desea ingresar: "))
        saldo += extra
        print(f"Dinero en la cuenta es: ${saldo}")
    elif opcion==2:
        retiro = float(input("Cuanto dinero desea retirar: "))
        if retiro>saldo:
            print("No tiene esa cantidad de dinero\n")
        else:
            saldo -= retiro
            print(f"Dinero en la cuenta: ${saldo}")
    elif opcion==3:
        print(f"Su saldo es: ${saldo}")
    elif opcion==4:
        print("Salida con exito\n")
        break
    else:
        print("Opcion de menu incorreccto\n")

    print()