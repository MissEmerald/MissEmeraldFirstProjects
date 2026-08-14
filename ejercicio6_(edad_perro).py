nombre = input("Ingrese el nombre de la mascota: ")
especie = input("Ingrese la especie de la mascota: ")
edad_perro = int(input("Ingrese la edad (en años) de la mascota: "))
edad_humana = (edad_perro * 7)

linea = "-" * 30

print(f"{linea} \n FICHA DE DATOS DE LA MASCOTA \n Nombre: {nombre} \n Especie: {especie} \n Edad humana: {edad_humana}")