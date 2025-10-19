# Este es el archivo n�mero 75
class felipe_mendieta:
    def __init__(self, contraseña):
        self.contraseña = contraseña

    def es_segura(self):
        return len(self.contraseña) >= 8 and any(c.isdigit() for c in self.contraseña)

p = felipe_mendieta("python123")
print("¿Contraseña segura?", p.es_segura())
