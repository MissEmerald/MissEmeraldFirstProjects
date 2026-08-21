temperatura = float(input("Ingrese la temperatura actual (C°): "))
lloviendo = input("¿Está lloviendo? (si/no)").strip().lower()

if (temperatura > 12):
    ropa = ("abrigo grueso")
elif (temperatura > 25):
    ropa = ("abrigo ligero")
else:
    ropa = ("ropa ligera")

if (lloviendo == "si"):
    paraguas = (" y llevar paraguas")
else:
    paraguas = ("")

print(f"se recomienda vestir {ropa}{paraguas}")