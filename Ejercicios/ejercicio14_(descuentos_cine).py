edad = int(input("Ingresar edad: "))
if edad <= 5 or edad >= 65:
    print("Entrada gratis")
else:
    estudiante = input("¿Es estudiante? (si/no): ").strip().lower()
    if (estudiante == ("si")):
        print("50% de descuento aplicable")
    else:
        print("Sin descuento aplicable")