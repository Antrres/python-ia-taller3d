# EJERCICIO 2: DESCUENTO POR CANTIDAD

CANTIDAD_MIN_DESCUENTO_BAJO = 10
CANTIDAD_MIN_DESCUENTO_ALTO = 50
DESCUENTO_BAJO = 0.10
DESCUENTO_ALTO = 0.20

ANCHO_TEXTO = 38
ANCHO_VALOR = 17
ANCHO_TOTAL = ANCHO_TEXTO + ANCHO_VALOR

precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad_piezas = int(input("Ingrese la cantidad de piezas: "))

subtotal = precio_unitario * cantidad_piezas


# Determinamos porcentaje de descuento
if cantidad_piezas >= CANTIDAD_MIN_DESCUENTO_ALTO:  
    porcentaje_descuento = DESCUENTO_ALTO
elif cantidad_piezas >= CANTIDAD_MIN_DESCUENTO_BAJO:
    porcentaje_descuento = DESCUENTO_BAJO
else:
    porcentaje_descuento = 0.0

monto_descontado = subtotal * porcentaje_descuento
total = subtotal - monto_descontado

# Formato del detalle de operación

print("\n" + "*" * ANCHO_TOTAL)
print("DETALLE DE LA OPERACIÓN".center(ANCHO_TOTAL))
print("\n" + "*" * ANCHO_TOTAL)
print(f"{'El subtotal es:':<{ANCHO_TEXTO}}{subtotal:>{ANCHO_VALOR}.2f}")
print(f"{'El descuento aplicado es:':<{ANCHO_TEXTO}}{porcentaje_descuento:>{ANCHO_VALOR}.0%}")
print(f"{'El monto descontado es: ':<{ANCHO_TEXTO}}{monto_descontado: {ANCHO_VALOR},.2f}")

print("-" * ANCHO_TOTAL)
print(f"{'El total a abonar es: ':<{ANCHO_TEXTO}}{total:{ANCHO_VALOR}.2f}")
print("-" * ANCHO_TOTAL)