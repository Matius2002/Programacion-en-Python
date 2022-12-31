"""
Errores
Principales excepciones definidas en Python:
-TypeError: Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado
-ZeroDivisionError: Ocurre cuando se intenta dividir por cero
-OverflowError: Ocurre cuando un cálculo excede el límite para un tipo de dato numérico
-IndexError: Ocurre cuando se intenta acceder a una secuencia con un índice que no existe
-KeyError: Ocurre cuando se intenta acceder a un diccionario con una clave que no existe
-FileNotFoundError: Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada
-ImportError: Ocurre cuando falla la importación de un módulo
"""
numero = int(input("Digite un número: "))

print(f"La suma es: {numero+10}")