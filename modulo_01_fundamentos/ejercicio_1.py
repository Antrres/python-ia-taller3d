# Ejercicio 1: tipos.
# Crear cuatro variables sobre una pieza y mostrar el valor y el tipo de cada una.

nombre_pieza = "Chop 500 ml"
peso_gramos = 300
horas_impresion = 8
lleva_soportes = False

print(f"nombre_pieza:    {nombre_pieza} -> {type(nombre_pieza)}")
print(f"peso_gramos:     {peso_gramos} -> {type(peso_gramos)}")
print(f"horas_impresion: {horas_impresion} -> {type(horas_impresion)}")
print(f"lleva_soportes:  {lleva_soportes} -> {type(lleva_soportes)}")

texto_soporte = "lleva soporte" if lleva_soportes else "no lleva soporte"
print(
    f"La pieza {nombre_pieza} pesa {peso_gramos} g, "
    f"tarda {horas_impresion} h de impresión y {texto_soporte}."
)