num = int(input("Ingrese un número para ver su tabla de multiplicación: "))

contador = 0 

while (contador < 10):
    contador += 1
    resultado = (num * contador)
    print(f"{num} x {contador} = {resultado}")