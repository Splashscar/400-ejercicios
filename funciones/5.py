# Este es el archivo n�mero 5
class felipe_mendieta:
    def __init__(self, limite):
        self.limite = limite
    def sumar_pares(self):
        suma = 0
        for i in range(2, self.limite + 1, 2):
            suma += i
        return suma
limite = 10
suma_pares = felipe_mendieta(limite)
resultado = suma_pares.sumar_pares()
print(f"La suma de los números pares hasta {limite} es: {resultado}")