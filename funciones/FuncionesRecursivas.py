"""
Funciones recursivas
"""
def cuenta_regresiva(num):
    if num > 0:
        print(num)
        cuenta_regresiva(num - 1)#Se vuelve a llamar la función
    else:
        print("Booom!!!")

cuenta_regresiva(10)