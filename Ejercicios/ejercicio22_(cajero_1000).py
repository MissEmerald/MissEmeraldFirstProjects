saldo = 1000

print("Bienvenidx al cajero automático")
print(f"Tu saldo inicial es: ${saldo}")
print("Instrucciones: Ingresa el monto a retirar o escribe '0' para salir.\n")

while (saldo > 0):
    retirar = float(input("Ingrese saldo a retirar: "))
    if (retirar < 0) or (retirar > saldo):
        print ("Acción no válida")
        continue
    elif (retirar == 0):
          print("Cerrando sesión. Hasta la próxima")
          break
    else:
        print(f"Haz retirado ${retirar}")
        saldo -= retirar
        print(f"El saldo actual es ${saldo}")
        if (saldo == 0):
             print("Se ah quedado sin saldo \nCerrando sesión. Hasta la próxima")
             break
        continue