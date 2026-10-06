print("CLASIFICADOR DE UNA IMPRESION \n") 

horas_impresion = float(input("Ingrese las horas de impresión: "))
soporte = input("¿La pieza lleva soporte? (s/n): ")

lleva_soporte = soporte.strip().lower() == "s"

if horas_impresion < 2:
        print("Categoria Corta")
elif 2 <= horas_impresion <= 8:
        print("Categoria Media")
else:
        if lleva_soporte:
            print("Categoria larga\n")
            print("La pieza lleva soportes\n")
            print("Revisar la primera capa antes de dejarla sola\n")

        else:
            print("Categoria larga")