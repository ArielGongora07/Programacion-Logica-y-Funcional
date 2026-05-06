numeros = [1,2,3,4,5,6,7,8,9,10]

doble = []

for n in numeros:
    doble.append(n*2)

print (doble)

#Generar otra lista de los cuadrados de los numeoos en la lista numeros
cuadrados = [num ** 2 for num in numeros]

lista_cuadruple = list (map(lambda x: x*4, numeros))
print(lista_cuadruple)

#Genera  otra lista con el cubo
cubo=[elemento ** 3 for elemento in numeros]

cadena = []
