# Este es el archivo n�mero 75
class felipe_mendieta:
    def __init__(self):
        self.gastos = []

    def agregar(self, descripcion, monto):
        self.gastos.append((descripcion, monto))

    def total(self):
        print("Gasto total:", sum(m for _, m in self.gastos))

app = felipe_mendieta()
app.agregar("Comida", 30000)
app.agregar("Transporte", 15000)
app.total()
