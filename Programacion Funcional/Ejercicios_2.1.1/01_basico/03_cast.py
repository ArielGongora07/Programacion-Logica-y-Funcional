#Transformar un tipo de un valor a otro

from os import system
if system ("clear") !=0: system("cls")

print ("Conversion de tipos")

#Convertir una cadena que contiene un numero a un entero
print(int("100")+2)# covertir 100

#Convertir entero a cadena para concatnarlo con otra caena
print("100" + str (2))

#Convertir una cadena con un numero decimal a tipo float
print(type(float("3.1416")))# Convierte 3.1416 a float y muestra su tipo

#Convertir un numero decimal a entero (se trunca la parte decimal)
print(int(3.1416))#convirtte 3.1416 a 3 elimando la parte decimal

#Evaluar valores numericos con boolenas
print(bool(3))#Cualquier numerico distintinto de o es true
print(bool(0))#0 es false
print(bool(-1))#Numerico negativo tambien son true

#Evaluar cadenas como  boolenaos
print(bool(""))#Una cadena vacia es false
print(bool(" "))#Una cadena con espacios 
print(bool("False"))#Una cadena con texto, aun que sea True

#Redondear un numero decimal
print(round(2.51))#Redondea 2.51 al entero

#Este genera un error y se comenta para evitar conflicto en la ejecucionn
#Print(int("Hola Mundo"))#Esto genera un ValuError porque "Hola mundo" no es numerico