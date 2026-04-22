from os import system
if system ("clear") !=0: system ("cls")

print ("\n Funciones")

def saludar():
    print("Hola")

def saludar_a(nombre):
    print(f"Hola{nombre}!")

saludar_a("Estudiante")
saludar_a("Jefa")
saludar_a("Profesor")
saludar_a("Directora")
saludar_a("Estudiante")

def sumar (a, b):
    suma = a + b
    return suma

result = sumar (2,3)
print(result)

def restar (a, b):
    return a-b

def multiplicar (a,b=2):
    return a*b

print(multiplicar(2))
print(multiplicar(2,3))

def describir_persona(nombre: str, edad: int, sexo: str):
    print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

describir_persona(1,25, "gato")
describir_persona("carlos",25, "pajaro")
describir_persona("persona","Ingeniero", "39")

describir_persona(sexo="perro", nombre="Reyes", edad=25)
describir_persona(sexo="mujer", nombre="Alejandra", edad="21")

def sumar_numeros (*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma

