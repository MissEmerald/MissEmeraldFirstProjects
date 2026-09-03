import random
random_num = random.randint(1, 10)

intento = int(input("Adivina el número del 1 al 10: "))
num_intento = 1

while (intento != random_num):
    num_intento += 1
    if (intento > 10) or (intento < 1):
        intento = int(input("Número no válido, intenta otra vez: "))
        continue
    elif (random_num < intento):
        cercanidad = "menor"
    elif (random_num > intento):
        cercanidad = "mayor"
    intento = int(input(f"Incorrecto, el numero secreto es {cercanidad} al número ingresado. \nNuevo intento: "))

print(f"Felicidades! Numero adivinado! \nNúmero de intentos usados: {num_intento}")