""""
num = 10

while num >= 1:
    print(num)
    num -= 1

    

num = 1
suma = 0

while num <= 20:
    if num % 2 == 0:
        suma += num
    num += 1

print("La suma es:", suma)

num = int(input("Ingresa un número: "))
factorial = 1
contador = 1

while contador <= num:
    factorial *= contador
    contador += 1

print("El factorial es:", factorial)


password = input("Ingresa una contraseña: ")

while len(password) < 8:
    password = input("Muy corta, intenta de nuevo: ")

print("Contraseña válida")

num = int(input("Ingresa un número: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

n = int(input("Ingresa un número: "))
num = 2

while num <= n:
    es_primo = True
    i = 2

    while i < num:
        if num % i == 0:
            es_primo = False
        i += 1

    if es_primo:
        print(num)

    num += 1

    """

"""Bucle FOR"""
""""
for num in range(2, 21, 2):
    print(num)

numeros = [10, 20, 30, 40, 50]
suma = 0

for n in numeros:
    suma += n

media = suma / len(numeros)
print("La media es:", media)


numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]

for n in numeros:
    if n > maximo:
        maximo = n

print("El número máximo es:", maximo)

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
resultado = []

for palabra in palabras:
    if len(palabra) > 5:
        resultado.append(palabra)

print(resultado)
"""

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
resultado = [p for p in palabras if len(p) > 5]

print(resultado)

palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
letra = input("Ingresa una letra: ").lower()
contador = 0

for palabra in palabras:
    if palabra.lower().startswith(letra):
        contador += 1

print("Cantidad:", contador)
