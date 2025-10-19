# Este es el archivo n�mero 92
saldo = 100000
while True:
    print("\n1. Consultar saldo\n2. Retirar\n3. Salir")
    felipe_mendieta = input("Seleccione una opción: ")

    if felipe_mendieta == "1":
        print("Saldo actual:", saldo)
    elif felipe_mendieta == "2":
        retiro = int(input("Ingrese el monto a retirar: "))
        if retiro <= saldo:
            saldo -= retiro
            print("Retiro exitoso. Nuevo saldo:", saldo)
        else:
            print("Saldo insuficiente.")
    elif felipe_mendieta == "3":
        print("Gracias por usar el cajero 💳")
        break
    else:
        print("Opción inválida.")
