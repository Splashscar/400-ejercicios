# Este es el archivo n�mero 16
class felipe_mendieta:
    def __init__(self, peso):
        self.peso = peso

    def costo_envio(self):
        return 5000 + (self.peso * 300)

paquete = felipe_mendieta(4)
print("Costo de envío:", paquete.costo_envio())
