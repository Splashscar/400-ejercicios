# Este es el archivo n�mero 46
class felipe_mendieta:
    def __init__(self):
        self.propiedades = []

    def agregar_propiedad(self, tipo, precio):
        self.propiedades.append({"tipo": tipo, "precio": precio})

    def mostrar_propiedades(self):
        for p in self.propiedades:
            print(f"{p['tipo']} en venta por ${p['precio']}")

inmo = felipe_mendieta()
inmo.agregar_propiedad("Casa", 250000000)
inmo.agregar_propiedad("Apartamento", 180000000)
inmo.mostrar_propiedades()
