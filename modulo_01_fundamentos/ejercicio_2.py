# Ejercicio 2: costo de material.
# Pedir por teclado el peso de la pieza y el precio del kilo de filamento,
# y mostrar el costo de material con 2 decimales.

GRAMOS_POR_KILO = 1000

peso_gramos = float(input("Ingrese el peso de la pieza en gramos: "))
precio_kg_filamento = float(input("Ingrese el precio del kilo de filamento: "))

costo_material = peso_gramos / GRAMOS_POR_KILO * precio_kg_filamento

print(f"El costo del material es ${costo_material:,.2f}")