num_nota = 1
total = 0
separador = "-" * 27

print(f"{separador}\nBienvenida a la calculadora de calificaciones\nIngrese -1 cuando termine de ingresar datos\n{separador}")
while True:
    nota = float(input(f"Ingrese calificación {num_nota}: "))
    if (nota == -1):
        break
    if (nota > 10) or (nota < 0):
        print("Inormación no válida, intente de nuevo.")
        continue
    num_nota += 1
    total += nota

num_nota -= 1
promedio = (total / num_nota)

print(f"{separador}{separador}\nEl promedio de las {num_nota} calificaciones ingresadas es: {promedio}\n{separador}{separador}")
