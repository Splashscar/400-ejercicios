# Este es el archivo n�mero 13
class felipe_mendieta:
    def __init__(self, horas, pago_hora):
        self.horas = horas
        self.pago_hora = pago_hora

    def salario(self):
        return self.horas * self.pago_hora

empleado = felipe_mendieta(48, 8000)
print("Salario:", empleado.salario())
