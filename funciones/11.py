# Este es el archivo n�mero 11
class felipe_mendieta:
    def __init__(self, palabras):
        self.palabras = palabras
    def imprimir_palabras(self):
        for i, palabra in enumerate(self.palabras, start=1):
            print(f"{i}: {palabra}")    
lista_de_palabras = ["manzana", "banana", "cereza", "durazno"]
imprimidor = felipe_mendieta(lista_de_palabras)
imprimidor.imprimir_palabras()
