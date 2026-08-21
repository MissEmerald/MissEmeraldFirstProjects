lado1 = float(input("Ingrese la longitud del primer lado del triagulo: "))
lado2 = float(input("Ingrese la longitud del segundo lado del triagulo: "))
lado3 = float(input("Ingrese la longitud del tercer lado del triagulo: "))

if (lado1 == lado2 == lado3):
    triangulo = ("Equilatero")
elif (lado1 == lado2) or (lado2 == lado3):
    triangulo = ("Isóceles")
else:
    triangulo = ("Escaleno")

print(f"El triangulo es de tipo: {triangulo}")