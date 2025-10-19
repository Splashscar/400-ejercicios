# Este es el archivo n�mero 55
class felipe_mendieta:
    def __init__(self):
        self.archivos = []

    def crear_archivo(self, nombre):
        self.archivos.append(nombre)
        return f"Archivo '{nombre}' creado."

    def listar(self):
        return f"Archivos: {', '.join(self.archivos)}"

gestor = felipe_mendieta()
gestor.crear_archivo("reporte.txt")
print(gestor.listar())
