#Condiciones combinados
#No existen condicionales multiples
edad = int(input("\nDigite su edad: "))

if 0<edad<110: #Mayor a 0 y menor de 110
    print("Edad correcta")
    if edad>=18:
        print("Es mayor de edad")
    elif edad <18:
        print("Es menor de edad")
else:
    print("Edad incorrecta")