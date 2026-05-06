#Ejemplo funcion primera clase

def saludo():
    return "Hola"

mi_variable = saludo()
print(mi_variable)

def saludo2():
    return "Que tal"

mi_variable2 = saludo2
print(mi_variable2())

#EJEMPLO FUNCION DE ORDEN SUPERIOR

def elegir_operacion(operacion):
    def multiplicar(x):
        return x * 2
    def dividir (x):
        return x/2
    
    if operacion == "Multiplicar":
        return multiplicar
    else:
        return dividir
    

doble = elegir_operacion("multiplicar")
print(doble(10))
divide2 = elegir_operacion("dividir")
print(divide2(10))


#EJEMPLO FUNCION ANOMINA =LAMBA

doble = lambda x: x*2
print(doble(5))

numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x*2, numeros))
print(dobles)

alunmos = ['Alejandro','Miguel','Vinicio','Rodney','Marcial']
saludar_alumnos = list(map(lambda nombre: 'Hola'+ nombre, alunmos))

print(saludar_alumnos)

#Sin lamba

def saludar (nombre):
    return'Hola' + nombre

#Usamos map con la funcion saludar

listas_saludar = list (map(saludar,alunmos))

#print(listas_saludar)