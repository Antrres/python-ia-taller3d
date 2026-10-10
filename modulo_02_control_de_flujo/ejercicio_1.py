# Ejercicio 1: clasificar una impresión según sus horas.

HORAS_MAX_CORTA = 2
HORAS_MAX_MEDIA = 8

print("CLASIFICADOR DE UNA IMPRESION \n") 

horas_impresion = float(input("Ingrese las horas de impresión: "))
respuesta = input("¿La pieza lleva soporte? (s/n): ")
lleva_soporte = respuesta.strip().lower() == "s"

if horas_impresion < HORAS_MAX_CORTA:
        categoria = "Corta"
elif horas_impresion <= HORAS_MAX_MEDIA:
        categoria = "Media"
else:
        categoria = "Larga"

print(f"Categoría: {categoria}")

if categoria == "larga" and lleva_soporte:
    print("Revisar la primera capa antes de dejarla sola")