lista_numeros = [12, 5, 8, 19, 21, 4, 10, 3]

contador_pares = 0

for numero in lista_numeros:
    if (numero % 2 == 0):
        contador_pares += 1
        print(numero)
    continue

print(f"Cantidad de números par encontrados: {contador_pares}")