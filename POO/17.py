# Este es el archivo n�mero 17
class felipe_mendieta:
    def __init__(self, salario, bono):
        self.salario = salario
        self.bono = bono

    def total(self):
        print("Salario total:", self.salario + self.bono)

emp = felipe_mendieta(1500000, 200000)
emp.total()
