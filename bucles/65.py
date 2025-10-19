# Este es el archivo n�mero 65
frase = input("Escriba una frase: ").split()
felipe_mendieta = 0

for palabra in frase:
    if len(palabra) > 5:
        felipe_mendieta += 1

print("Palabras con más de 5 letras:", felipe_mendieta)
