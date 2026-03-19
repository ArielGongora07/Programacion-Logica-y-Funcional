from os import system

if system ("clear") !=0: system("cls")


"""
El comando Type() devuelve el tipo de un objecto en Python

"""

print ("int:") #Enteros numero si parte decimal
print(type(10)) #Numero entero positivo
print(type(0)) #El numero cero tambien es un entero
print(type(-5)) #Numero entero negativo
print(type(77773773723723282823324246534))#Python permite enteros de gran tamaño



print ("float:") 
print(type(3.14)) 
print(type(1.0)) 
print(type(1e3)) 


print ("complex:")
print(type(1+2j)) 

print ("str:")
print(type("Hola")) 
print(type("")) 
print(type("123")) 
print(type(""" 
    Multilinea
""")) 

print ("bool:")
print(type(True)) 
print(type(False)) 
print(type(1<2)) 

print ("NoneType:")
print(type(None)) 
