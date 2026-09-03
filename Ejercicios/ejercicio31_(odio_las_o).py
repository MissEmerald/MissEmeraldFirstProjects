palabra = input("Ingrese una palabra: ")

for letra in palabra:
    if letra in ("o", "O"):
        print("Letra 'o' encontrada, apagando sistema...")
        break
    print(letra)