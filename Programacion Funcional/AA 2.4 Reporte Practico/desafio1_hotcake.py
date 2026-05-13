"""HECHO POR ARIEL ALONSO GONGORA TZIU"""


def preparar_hotcakes():
    return "🥞"

def ordenar_hotcakes(numero_piezas):
    piezas_hotcakes = [preparar_hotcakes() for _ in range(numero_piezas)]
    return piezas_hotcakes

hot_cakes_familia = ordenar_hotcakes (int(input('cuantos son en tu familia: ')))
print(hot_cakes_familia)