interruptor ="1"
total = 0

while (interruptor != 0):
    sumar = float(input("Ingrese número a sumar (0 para terminar): "))
    if sumar == 0:
        interruptor = 0
    else:
        total += sumar
print(f"El total es: {total}")