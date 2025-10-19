# Este es el archivo n�mero 7
class felipe_mendieta:
    def __init__(self, calificaciones):
        self.calificaciones = calificaciones
    def calcular_promedio(self):
        suma = sum(self.calificaciones)
        promedio = suma / len(self.calificaciones)
        return promedio
    
calificaciones = [85, 90, 78, 92, 88]
estudiante = felipe_mendieta(calificaciones)
promedio_calificaciones = estudiante.calcular_promedio()
print(f"El promedio de las calificaciones es: {promedio_calificaciones}")