"""Ejercicio 3: costo total de una pieza (inicio del proyecto).

Pide peso, precio del kilo de filamento y horas de impresión, y calcula
el costo de material, el de electricidad, el costo total y el precio de
venta con margen.
"""

GRAMOS_POR_KILO = 1000
CONSUMO_IMPRESORA_KW = 0.4   # potencia media de la impresora
PRECIO_KWH = 200             # pesos por kWh
MARGEN = 0.60                # 60 % sobre el costo

peso_gramos = float(input("Ingresá el peso de la pieza en gramos: "))
precio_kg_filamento = float(input("Ingresá el precio del kilo de filamento: "))
horas_impresion = float(input("Ingresá las horas de impresión: "))

respuesta = input("¿Lleva material adicional? (s/n): ")
lleva_material_adicional = respuesta.strip().lower() == "s"

if lleva_material_adicional:
    costo_material_adicional = float(input("Ingresá el costo del material adicional: "))
else:
    costo_material_adicional = 0.0

costo_material = peso_gramos / GRAMOS_POR_KILO * precio_kg_filamento
costo_electricidad = horas_impresion * CONSUMO_IMPRESORA_KW * PRECIO_KWH
costo_total = costo_material + costo_electricidad + costo_material_adicional
precio_venta = costo_total * (1 + MARGEN)

print()
print("----- RESUMEN -----")
print(f"Material:           ${costo_material:>12,.2f}") # >12 alinea el número a la derecha en un ancho de 12 caracteres, así las cifras quedan encolumnadas
print(f"Electricidad:       ${costo_electricidad:>12,.2f}")
print(f"Material adicional: ${costo_material_adicional:>12,.2f}")
print(f"Costo total:        ${costo_total:>12,.2f}")
print(f"Precio de venta:    ${precio_venta:>12,.2f}")