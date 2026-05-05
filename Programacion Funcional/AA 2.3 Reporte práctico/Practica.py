# =============================================================================
#  Sistema de pedidos: Comedor Escolar
# =============================================================================

# ── PASO 1 ──────────────────────────────────────────────────────────────────
# Funciones simples y de primera clase

def preparar_pizza():
    return "🍕 pizza"

def preparar_agua():
    return "🥤 agua fresca"

def preparar_tamal():
    return "🫔 tamal"


# ── PASO 2 ──────────────────────────────────────────────────────────────────
# Lógica condicional

def calcular_promocion(cantidad):
    if cantidad >= 3:
        return "🎁 postre gratis"
    else:
        return ""


# ── PASO 3 ──────────────────────────────────────────────────────────────────
# Función de Orden Superior, Comprensión de listas y map + lambda

def tomar_orden(preparar_alimento, cantidad, precio_unitario):
    # a) Comprensión de listas: Llama a la función la cantidad de veces requerida
    porciones = [preparar_alimento() for _ in range(cantidad)]
    
    # b) map() + lambda para precios: Asigna el precio_unitario a cada elemento
    precios = list(map(lambda x: precio_unitario, porciones))
    
    # c) Promoción: Evalúa si le toca postre
    promocion = calcular_promocion(cantidad)
    
    # d) Devuelve los tres valores en una tupla
    return porciones, precios, promocion


# ── PASO 4 ──────────────────────────────────────────────────────────────────
# Entrada del usuario y ejecución

cantidad_pizzas  = int(input("¿Cuántas pizzas deseas ordenar? "))
cantidad_aguas   = int(input("¿Cuántas aguas frescas deseas ordenar? "))
cantidad_tamales = int(input("¿Cuántos tamales deseas ordenar? "))

# Llama a tomar_orden usando las funciones como callbacks
orden_pizza  = tomar_orden(preparar_pizza,  cantidad_pizzas,  25)
orden_agua   = tomar_orden(preparar_agua,   cantidad_aguas,   10)
orden_tamal  = tomar_orden(preparar_tamal,  cantidad_tamales, 15)


# ── PASO 5 ──────────────────────────────────────────────────────────────────
# Resumen del pedido

print("\n========== RESUMEN DEL PEDIDO ==========")

# Desempaqueta cada tupla
porciones_pizza,  precios_pizza,  promo_pizza  = orden_pizza
porciones_agua,   precios_agua,   promo_agua   = orden_agua
porciones_tamal,  precios_tamal,  promo_tamal  = orden_tamal

# Imprime los resultados (Uso de condicional inline para imprimir "sin promoción")
print(f"\n🍕 PIZZAS   → {porciones_pizza}")
print(f"💲 Precios  → {precios_pizza}")
print(f"🎁 Promo    → {promo_pizza if promo_pizza else 'sin promoción'}")

print(f"\n🥤 AGUAS    → {porciones_agua}")
print(f"💲 Precios  → {precios_agua}")
print(f"🎁 Promo    → {promo_agua if promo_agua else 'sin promoción'}")

print(f"\n🫔 TAMALES  → {porciones_tamal}")
print(f"💲 Precios  → {precios_tamal}")
print(f"🎁 Promo    → {promo_tamal if promo_tamal else 'sin promoción'}")

print("\n========================================")