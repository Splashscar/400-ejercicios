# Este es el archivo n�mero 13
class felipe_mendieta:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}")

producto = felipe_mendieta("Mouse", 75000)
producto.mostrar()
