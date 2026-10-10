# EJERCICIO 2: DESCUENTO POR CANTIDAD

LIMITE_CANTIDAD_DESCUENTO_1 = 9
LIMITE_CANTIDAD_DESCUENTO_2 = 49
ANCHO_TEXTO = 38
ANCHO_VALOR = 17

precio_unitario = float(input("Ingrese el precio unitario: "))
cantidad_piezas = int(input("Ingrese la cantidad de piezas: "))

subtotal = float(precio_unitario * cantidad_piezas)


# Determinamos porcentaje de descuento
if LIMITE_CANTIDAD_DESCUENTO_1 < cantidad_piezas <= LIMITE_CANTIDAD_DESCUENTO_2:  
    descuento = 0.10
elif cantidad_piezas > LIMITE_CANTIDAD_DESCUENTO_2:
    descuento = 0.20
else:
    descuento = 0

monto_descontado = subtotal * (descuento)
total = subtotal - monto_descontado

# Formato del detalle de operación

print("\n" + "*" * 55)
print("DETALLE DE LA OPERACIÓN".center(55))
print("\n" + "*" * 55)
print(f"{'El subtotal es:':<{ANCHO_TEXTO}}{subtotal:>{ANCHO_VALOR}.2f}")
print(f"{'El descuento aplicado es:':<{ANCHO_TEXTO}}{descuento:>17.0%}")
print(f"{'El monto descontado es: ':<{ANCHO_TEXTO}}{monto_descontado: {ANCHO_VALOR}}")

print("-" * 55)
print(f"{'El total a abonar es: ':<{ANCHO_TEXTO}}{total:{ANCHO_VALOR}.2f}")
print("-" * 55)