# Este es el archivo n�mero 93
class felipe_mendieta:
    def verificar(self, velocidad):
        if velocidad <= 60:
            return "Conduces a velocidad segura 🚙"
        elif velocidad <= 100:
            return "Precaución ⚠️"
        else:
            return "¡Multa por exceso de velocidad! 🚓"

auto = felipe_mendieta()
print(auto.verificar(110))
