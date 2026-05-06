# 1. Crear una funcion que no tome ningun argumento y devuelva la cadena de texto "cafe". para simular la preparacion de uno

""""2. Crear funcion para tomar la orden del cafe  que toma un argumento numero_taza, que indica cunatas tazas de cafe se desean
dentro de la funcion
---Alamacena los resultados en una lista llamada taza_cafe
---Utlliza una lista para compresion para llamar a la funcion preparpar_cafe segun
el numero_tazas proporcionado. Ir archivo compresionLista.py
---Finalmente devuelve la lista tazas_cafe

3.- Llama a la 2da funcion con el numero de tazas que requiere y almacenar en una varible cafe_para_grupo

4.- Imprimir el contenido de la variable cafe__para_grupo, es decir, la lista de la de la cadena 

"""

def preparar_cafe():
    return "Cafe"

def ordernar_cafe(numero_tazas):
    tazas_cafe = [preparar_cafe() for _ in range (numero_tazas)]
    return tazas_cafe

cafe_para_grupo = ordernar_cafe(10)
print(cafe_para_grupo)
