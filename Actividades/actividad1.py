nombre = input("Ingrese su nombre: ")
tiempo_instagram = float(input("Ingrese su tiempo registrado hoy en Instragram: "))
tiempo_tiktok = float(input("Ingrese su tiempo registrado hoy en Tiktok: "))
tiempo_youtube = float(input("Ingrese su tiempo registrado hoy en YouTube: "))
tiempo_netflix = float(input("Ingrese su tiempo registrado hoy en Netflix: "))
tiempo_crunchyrrol = float(input("Ingrese su tiempo registrado hoy en Crunchyrrol: "))

tiempo_total = float(tiempo_instagram + tiempo_tiktok + tiempo_youtube + tiempo_netflix + tiempo_crunchyrrol)
pocentaje_dia = float(tiempo_total / 24 * 100)

separador = "-" * 38

print(f"{separador} \nNombre del usuario: {nombre} \nTiempo total invertido: {tiempo_total:.2f} horas \nPorcentaje del día invertido: {pocentaje_dia:.2f}% \n{separador}")