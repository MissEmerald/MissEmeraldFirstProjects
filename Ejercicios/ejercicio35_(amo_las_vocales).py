cuenta_letras = 0

frase = input("Ingrese frase o palabra: ")

for letra in frase:
    if letra in("a", "e", "i", "o" , "u", "A", "E", "I", "O", "U"):
        cuenta_letras += 1
    else:
        continue

print(f"Cantidad de vocales en la frase ingresada: {cuenta_letras}")