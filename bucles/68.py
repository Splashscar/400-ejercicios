# Este es el archivo n�mero 68
palabra = input("Ingrese una palabra: ").lower()
felipe_mendieta = palabra[::-1]

if palabra == felipe_mendieta:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
