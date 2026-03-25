#Entrada de usuario 

from os import system
if system ("clear") !=0: system("cls")

nombre= input("Hola, ¿Como te llamas?\n")
print(f"Hola{nombre}, escantado de conocerte")

#-----------------
age=input("¿Cuantos años tienes?\n")
age=int(age)
print(f"Tienes{age} años")

#------------------------
print("Obtener multiples valores ala vez")
coutry, city = input ("¿En que pais y cuidad vives?\n").split()

print(f"Vives en {coutry}, {city}")