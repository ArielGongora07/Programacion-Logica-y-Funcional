"""##
#01--- Sentencias condicionales (if,elif,else)
#Permitir ejecutar bloques de codigos solo si se cumple cieertas condiciones
##

from os import system
if system ("clear") !=0: system("cls")

print("\n Setencias simple condicional")
#Podemos usar la palaabra clave "if" para ejcutar un bloque de codigo
#solo si se cumple una condicion.

edad=18
if edad >= 18:
    print ("Eres mayor de edad")
    print("!Felicades!")

#Si no cumple la condicion, no se ejecuta el bloque de codigo
edad=15
if edad >= 18:
    print ("Eres mayor de edad")
    print("!Felicades!")

#Podemos usar el comando "else" para ejecutar un bloque de codigo
#si no se cumple la condicion anterior del if
print("\n Sentencia condicional con else")
edad=15
if edad >= 18:
    print ("Eres mayor de edad")
    print("!Felicades!")

print("\n Sentencia condicional con elif")
#Ademas de usar "if" y "else", podemos usar "elif" para determinar 
#multiples condiciones, ten en cuenta que solo se ejecutara en el primer bloque 
#de codigo que cumpla la condicion (o la del else, si esta presente)

nota = 5
if nota >= 9:
    print("!Sobresaliente!")
elif nota >=7:
    print("Notable!")
elif nota >=5:
    print("Aprobado!")
else:
    print("!No estas calificado!")

print("\n Codiciones multiples")
edad = 16
tiene_carnet = True

#Los operadores logicos en python son
#and: True si ambos operadores son verdaderos 
#or: True si al menos uno de los operadores es verdaderos 
#En JavaScript:
#&& seria and
#|| seria or

#En el caso que seas mayor de edad y tengas carnet..
#Entonces podras conducir

if edad >=18 and tiene_carnet:
    print("Puedes conducir🚗")
else:
    print("Policia !!!")

#En un pueblo de Isla Holbox son mas relajados y 
#te dejan conducir si eres mayor de edad o tienes carnet

if edad >= 18 or tiene_carnet:
    print("Puedes conducir en la Isla Holbox")
else:
    print("Paga al policia y te dejara conducir")

#Tambien tenemos el operador logico "not"
#que nos permite negar una condicion
es_fin_de_semana=False

#JavaScript-> !
if not es_fin_de_semana:
    print("!ISC, anda que hay que ir al tec")

#Podemos anidar condicionales, uno dentro del otro
#para determinar multiples condiciones auque 
#siempre  intentaremos evitar esto para simplificar
print("\n Anidar condicionales")
edad=20
tiene_dinero= True

if edad >=18:
    if tiene_dinero:
        print("Puedes ir a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la disco")

#Mas facil seria :
#if edad < 18:
#  print ("No puedes entar a la discoteca")
#elif tiene_dinero:
#  print ("Puedes ir ala discoteca")
#else:
#  print ("Quedate en casa")

#Ten en cuenta que hay valores que al usarlos como condiciones
#en python son evaluados como verdaderos o falsos
#por ejemplp, el numero 4, es true
#numero= 5
#if numero =#True
#   print("El numero no es cero")

# Pero el número 0 se evalúa como False
numero = 0
if numero: # False
    print("Aquí no entrará nunca")

# También el valor vacío "" se evalua como False
nombre = ""
if nombre:
    print("El nombre no es vacío")

# Ten cuidado con no confundir la asignación = con la comparación ==!
numero = 3 # asignación
es_el_tres = numero == 3 # comparacion

if es_el_tres:
    print("El número es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\n La condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)"""

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

"""num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if num1 > num2:
    print("El número mayor es:", num1)
elif num2 > num1:
    print("El número mayor es:", num2)
else:
    print("Ambos números son iguales")"""

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
"""n1 = float(input("\nIngresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")

if operacion == "+":
    print("Resultado:", n1 + n2)
elif operacion == "-":
    print("Resultado:", n1 - n2)
elif operacion == "*":
    print("Resultado:", n1 * n2)
elif operacion == "/":
    if n2 != 0:
        print("Resultado:", n1 / n2)
    else:
        print("Error: No se puede dividir entre cero")
else:
    print("Operación no válida")"""


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero
#no por 400.
"""""
an = int(input("\nIngresa un año: "))

if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")"""
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("\nIngresa una edad: "))

if edad >= 0 and edad <= 2:
    print("Es un bebé")
elif edad <= 12:
    print("Es un niño")
elif edad <= 17:
    print("Es un adolescente")
elif edad <= 64:
    print("Es un adulto")
elif edad >= 65:
    print("Es un adulto mayor")
else:
    print("Edad no válida")