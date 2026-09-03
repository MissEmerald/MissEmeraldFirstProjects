correos = ["ana@gmail.com", "pedro@hotmail.com", "marta@gmail.com", "luis@yahoo.com"]

for correo in correos:
    if "@" in correo and (correo.split("@")[1] == "gmail.com"):
        print(correo)