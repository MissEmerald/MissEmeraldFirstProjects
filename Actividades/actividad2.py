precio_total = 0

num_visitantes = int(input("¿Cuantas entradas desea?: "))

for visitante in range(num_visitantes):
    es_niño = False
    es_mayor_edad = False
    es_profesor = False
    es_estudiante = False
    es_adulto_mayor = False
    num_boleto = (visitante + 1)

    if num_visitantes <= 0:
        break

    es_niño = ((input(f"¿La persona de la entrada {num_boleto} es menor a 3 años? (si/no): ").lower().strip()) == "si")
    
    if es_niño == True:
        continue

    es_mayor = ((input(f"¿La persona de la entrada {num_boleto} es mayor de edad? (si/no): ").lower().strip()) == "si")
    if es_mayor == True:
        es_adulto_mayor = ((input(f"¿La persona de la entrada {num_boleto} es adulto mayor? (si/no): ").lower().strip()) == "si")
        if es_adulto_mayor == False:
            es_profesor = ((input(f"¿La persona de la entrada {num_boleto} es profesor(a)? (si/no): ").lower().strip()) == "si")
    elif es_mayor == False:
        es_estudiante = ((input(f"¿La persona de la entrada {num_boleto} es alumno(a)? (si/no): ").lower().strip()) == "si")

    if es_mayor == True:
        precio_base = 45
    else:
        precio_base = 30

    if es_adulto_mayor == True and es_profesor == False and es_estudiante == False:
        descuento = 0.12
    elif es_profesor == True and es_adulto_mayor == False and es_estudiante == False:
        descuento = 0.10
    elif es_estudiante == True and es_adulto_mayor == False and es_profesor == False:
        descuento = 0.10
    else:
        descuento = 0.0

    precio_boleto = precio_base * (1 - descuento)
    precio_total += precio_boleto

print(f"\nPrecio total: ${precio_total:.2f}")