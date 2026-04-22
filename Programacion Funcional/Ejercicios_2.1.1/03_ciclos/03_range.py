#03 -range ()
#Permite crear una secuencia de numeros.Puede ser util

from os import system
if system ("clear") !=0: system ("cls")

print ("\n Range()")

for num in range (10):
    print(num)

for num in range (5,10):
    print(num)

for num in range (0,100,5):
    print(num)

for num in range (-5,0):
    print(num)

for num in range (10,0,-1):
    print(num)

for num in range (0,444):
    print(num)

nums = range(10)
list_of_nums = list (nums)
print (list_of_nums)

for _ in range(5):
    print("hacer cinco veces algo")

