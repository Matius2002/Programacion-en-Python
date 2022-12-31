#Excepciones
while True:
    try:
        numero = int(input("Digite un número: "))
        print(f"El numero es {numero}")

    except:
        print("\nError, -> Digite un número entero ")
    
    else:
        print("Porgrama finalizado correctamente")
        break

    finally:
        print("Iteración finalizada")
