"""costo total (inicio del proyecto). Pedí peso, precio del kilo y horas de impresión. Calculá:

    costo de material
    costo de electricidad = horas * consumo de la impresora en kW * precio del kWh (definí los dos últimos como constantes; valores de ejemplo: 0.15 kW y $120)
    costo total
    precio de venta con un 60% de margen sobre el costo
"""
peso_gramos = float(input("Ingrese el peso de la pieza en gramos: "))
precio_kilo = float(input("Ingrese el precio de kilo de filamento: "))
hora_impresion = float(input("Ingrese las horas de impresión: "))



CONSUMO_IMPRESORA = 0.4 # Consumo en KiloWatts
PRECIO_KWh = 200 # Precio KWh
material_adicional = bool(input("¿Existe material adiconal? (s/n)"))

if material_adicional == False:
    costo_material_adicional = 0
else:
    costo_material_adicional = float(input("Ingrese el costo del material adicional: "))

costo_base = 0

costo_material = (peso_gramos * precio_kilo) / 1000
costo_electricidad = (hora_impresion * CONSUMO_IMPRESORA) * PRECIO_KWh


if material_adicional == False:
    costo_base = costo_material + costo_electricidad + costo_material_adicional
    print(f"El costo base es {costo_base}")
else:
    costo_base = costo_material + costo_electricidad + costo_material_adicional
    print(f"El costo base es {costo_base}") 

margen = 1.6
costo_final = (margen * costo_base)  
print(f"COSTO FINAL CON 60% DE MARGEN es {costo_final}")