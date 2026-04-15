from os import system
if system ("clear")!=0: system ("cls")

print ("\n Bucle for")

frutas =  ["Manzanas", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

cadena = "estudiante"
for caracter in cadena:
    print(caracter)

frutas =  ["Manzanas", "pera", "mandarina"]
for idx, value in enumerate (frutas):
    print (f"El indice es {idx} y la fruta es {value}")

letras = ["A", "B", "C"]
numeros = ["1", "2", "3"]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

print ("\n Break:")
animales = ["Perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate (animales):
    print(animal)
    print(f"El loro esta encido en el indice {idx}")
    break

animales = ["Perro", "gato", "raton", "loro", "pez", "canario"]  
animales_mayus = [animal.upper() for amimal in animales]  
print

print ("\n Continue:")
animales = ["Perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate (animales):
    if  animal == "loro": continue

    print(animal)

animales = ["Perro", "gato", "raton", "loro", "pez", "canario"]  
animales_mayus = [animal.upper() for amimal in animales]  
print(animales_mayus)

pares =  [num for num in [1,2,3,4,5,6 ]if  num % 2 ==0 ]
print(pares)

