# Costo de material. Pedí por teclado el peso de la pieza y el precio del kilo de filamento, y mostrá el costo de material con 2 decimales.

peso_pieza = float(input("Ingresa el peso de la pieza en gramos: "))
precio_kilo_filamento = float(input("Ingrese el precio del kilo de filamento: "))
costo_material = (peso_pieza * precio_kilo_filamento) / 1000


print(f"El costo del material es {costo_material:.2f}")