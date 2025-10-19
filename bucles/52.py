# Este es el archivo n�mero 52
for felipe_mendieta in range(2, 21):
    es_primo = True
    for i in range(2, felipe_mendieta):
        if felipe_mendieta % i == 0:
            es_primo = False
            break
    if es_primo:
        print(felipe_mendieta)
