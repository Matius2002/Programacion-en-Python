#Funciones binarias
#Nota: Binario tiene base 2 y hexadecimal tiene 16
n = bin(10)#Convertimos el numero a binario
m = hex(12)#Convertimos el numero a hexadecimal
j = int("0b1010",2)#Convertimos el numero binario a entero
a = int("0xc",16)#Convertimos el numero haxadecimal a entero 
k = abs(8)#El valor absoluto es su distancia desde cero en una recta numérica
r = round(5.6)#Redondea el numero mas cercano
e = len("Mateo Alejandro")#Cuenta los caracteres 

print("\nNumero binario: ",n)
print("Numero hexadecimal: ",m)
print("Convertimos un numero binario a entero: ",j)
print("Convertimos un numero hexadecimal a entero: ",a)
print("Valor absoluto: ",k)
print("Redondeo del numero: ",r)
print("Numero de caracteres: ",e)