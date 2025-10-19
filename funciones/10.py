# Este es el archivo n�mero 10
class felipe_mendieta:
    def __init__ (self, gatos):
        self.gatos = gatos
    def contar_gatos(self): 
        for i in range(1, self.gatos + 1):
            print(f"Gato número {i}")
            
numero_de_gatos = 4
contador = felipe_mendieta(numero_de_gatos) 
contador.contar_gatos()
