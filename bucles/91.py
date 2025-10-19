# Este es el archivo n�mero 91
suma = 0
contador = 0

while True:
    entrada = input("Ingrese una nota (o 'fin' para terminar): ")
    if entrada.lower() == "fin":
        break
    felipe_mendieta = float(entrada)
    suma += felipe_mendieta
    contador += 1

if contador > 0:
    print("Promedio final:", suma / contador)
else:
    print("No se ingresaron notas.")
