intento = int(input("Adivina el número secreto entre el 1 y el 10: "))

while (intento != 7):
    if (intento > 10) or (intento < 1):
        print("Ese número ni si quiera es válido, baka!")
    intento = int(input("Número incorrecto! Intenta de nuevo: "))
print("F-felicidades! Acertaste el número")